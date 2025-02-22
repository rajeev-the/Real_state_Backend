from rest_framework import viewsets
from .models import Property, State
from .serializers import PropertySerializer, StateSerializer
from google.oauth2 import service_account
import os
from googleapiclient.discovery import build


# Path to your service account key file
SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(__file__), './radiant-destiny-446418-e0-c44eba644671.json')
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Initialize the Google Sheets API client
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)

# Your Google Sheet ID
SPREADSHEET_ID = '1szKUG6Ca9Bw0PpnV-W1zl_jkbn-Mif2ZknUZiFY1S1w'

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        # Extract the data from the response
        property_data = response.data

        # Prepare the row to be inserted into the Google Sheet
        row = [
            property_data.get('img', ''),
            property_data.get('property_name', ''),
            property_data.get('acre_price', ''),
            property_data.get('acre', ''),
            property_data.get('available', False),
            property_data.get('road_width', ''),
        ]

        # Define the range where the data will be inserted
        range_name = 'Sheet1!A1:F1'  # Adjust the range as needed

        # Create the request body
        body = {
            'values': [row]
        }

        try:
            # Insert the data into the sheet
            service.spreadsheets().values().append(
                spreadsheetId=SPREADSHEET_ID,
                range=range_name,
                valueInputOption='RAW',
                body=body
            ).execute()
        except Exception as e:
            # Log the error or handle it as needed
            print(f"Error inserting data into Google Sheet: {e}")

        return response
