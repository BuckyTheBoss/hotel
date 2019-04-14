from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class RoomType(models.Model):
	name = models.CharField(max_length=30)
	capacity = models.IntegerField()
	price = models.IntegerField()
	desc = models.TextField()

class Room(models.Model):
	room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
	number = models.IntegerField()
	# number is the room number to display, XYY, X being floor, YY being room number on floor
	active = models.BooleanField(default=True)

class Booking(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	occupants = models.IntegerField()