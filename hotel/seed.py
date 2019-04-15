from visitor.models import *
from faker import Faker
from django.contrib.auth.models import User
import random

fake = Faker()



def gen_fname():
	return fake.first_name()

def gen_lname():
	return fake.last_name()

def gen_password():
	return fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)

def pick_user():
	return random.choice(User.objects.all())

def pick_room():
	return random.choice(Room.objects.all())

def create_users(number):
	for i in range(0, number):
		fname = gen_fname()
		lname = gen_lname()
		username = fname.lower() + lname.lower()
		user = User.objects.create_user(username=username, password=gen_password(), first_name=fname, last_name=lname)
		user.save()


def gen_datetime(datetime=None):
	# gets random datetime this year till now, if a datetime is passed in it will get a datetime after that date
	if datetime != None:
		return fake.date_time_between(start_date=datetime, end_date="+50d", tzinfo=None)
	return fake.date_time_this_year(before_now=True, after_now=False)


def seed_room_types():
	lists = [['Standard',3,100,'Standard room type'],['Deluxe',4,150,'Deluxe room type'],['Suite', 6, 300, 'Suite room type'],['Presidental Suite',3,1000,'Presidental Suite room type']]
	for i in lists:
		room_type = RoomType(name=i[0], capacity=i[1], price=i[2], desc=i[3])
		room_type.save()

def seed_rooms(number):
	types = RoomType.objects.all()
	for i in range(0, number):
		room = Room(room_type=random.choice(types))
		room.save()

def seed_booking(number):
	for i in range(0,number):
		room = pick_room()
		start_date = gen_datetime()
		booking = Booking(
			user = pick_user(),
			room = room,
			start_date = start_date,
			end_date = gen_datetime(start_date),
			occupants = (room.room_type.capacity - 1)
			)
		booking.save()
