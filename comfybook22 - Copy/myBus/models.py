from django.db import models

# Create your models here.
class Tripform(models.Model):
    route =models.TextField(max_length=50)
    duration=models.TextField(max_length=50)
    distance=models.TextField(max_length=50)
    price=models.TextField(max_length=50)
    
    
class bus(models.Model):
    find_bus=models.TextField(max_length=50)
    customer_type=models.TextField(max_length=50)
    date_of_travel=models.TextField(max_length=50)
    number_of_seats=models.IntegerField(default=0)
    fare_per_seat=models.IntegerField(default=0)
    total_cost=models.TextField(max_length=50)

class billing(models.Model):
    payment_method=models.TextField(max_length=50)
    payment_amount=models.IntegerField(default=0)


class travel(models.Model):
    routes =models.TextField(max_length=80)
    durations=models.TextField(max_length=40)
    distances=models.TextField(max_length=50)
    prices=models.TextField(max_length=60)

class sleep(models.Model):
    roomnumber =models.TextField(max_length=80)
    floor=models.TextField(max_length=40)
    duration=models.TextField(max_length=50)

