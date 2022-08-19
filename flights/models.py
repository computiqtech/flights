from django.db import models
# Create your models here.
class Airport(models.Model):
    name=models.CharField(max_length=64)
    code=models.CharField(max_length=3)

    def __str__(self) -> str:
        return f"code:{self.code}, Name:{self.name}"
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='origin')
    dest = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='dest')
    duration = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.origin}, {self.dest}, duration: {self.duration}"


class  Passenger(models.Model):
    first = models.CharField(max_length=32)
    last = models.CharField(max_length=32)
    flights = models.ManyToManyField(Flight,related_name='passengers')

    def __str__(self) -> str:
        return f"{self.first}, {self.last}"