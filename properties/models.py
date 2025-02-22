from django.db import models

class State(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Property(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="properties", default=1)  # Default state ID
    img = models.URLField()
    property_name = models.CharField(max_length=255)
    acre_price = models.DecimalField(max_digits=10, decimal_places=2)
    acre = models.DecimalField(max_digits=5, decimal_places=2)
    available = models.BooleanField(default=True)
    road_width = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.property_name} - {self.state.name}"
