
from django.db import models

class FitnessClass(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    spots_available = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.start_time.strftime('%Y-%m-%d %H:%M')})"

 #booking
class Booking(models.Model):
    fitness_class = models.ForeignKey(FitnessClass, on_delete=models.CASCADE, related_name='bookings')
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
      return f"{self.name} booked {self.fitness_class.name}"


