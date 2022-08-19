from django.contrib import admin
from .models import Flight, Airport, Passenger
# Register your models here.
# admin.site.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('id','origin', 'dest','duration')

class PassengerAdmin(admin.ModelAdmin):
    list_display = ('id','first','last')

admin.site.register(Flight,FlightAdmin)
admin.site.register(Airport)
admin.site.register(Passenger, PassengerAdmin)
