from rest_framework import serializers
from .models import Property, State

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

from rest_framework import serializers
from .models import Property, State

from rest_framework import serializers
from .models import Property, State

class PropertySerializer(serializers.ModelSerializer):
    state_name = serializers.SerializerMethodField()  # Custom field for state name
    state = serializers.PrimaryKeyRelatedField(queryset=State.objects.all())  # Keep state as ID

    class Meta:
        model = Property
        fields = '__all__'  # Includes all fields + state_name
        extra_fields = ['state_name']

    def get_state_name(self, obj):
        return obj.state.name  # Fetch the state name
