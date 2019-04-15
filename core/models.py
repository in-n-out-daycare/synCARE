from django.db import models, uuid
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Admin(models.Model):
    name = models.CharField(max_length=50, help_text="Last name, First name")
    role = models.CharField(max_length=50, help_text="your role in the facility")


class Caregiver(models.Model):
    name = models.CharField(max_length=50, help_text="Last name, First name")
    role = models.CharField(max_length=50, help_text="your role in the facility")
    classroom = models.ForeignKey('Classroom', on_delete=models.CASCADE)
     

class Classroom(models.Model):
    category = models.CharField(max_length=10, null=False)


class Guardian(models.Model):
    name = models.CharField(max_length=50, help_text="Last name, First name")
    phone_number = models.PhoneNumberField(null=False)
    email = models.EmailField(max_length=254, null=False)
    

class Child(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.CharField(max_length=2, null=False)
    child_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    classroom = models.ForeignKey('Classroom', on_delete=models.CASCADE)
    guardians = models.ManyToManyField(to=Guardian, related_name="children")
    child_pic = models.ImageField(null=True)
    allergy = models.CharField(max_lenth=200)



class Visit(models.Model):
    check_in = models.BooleanField('Check in', default=False)
    check_out = models.BooleanField('Check out', default=False)
    date_created = models.DateTimeField('Date Created', auto_now_add=True, null=True)
    child = models.ForeignKey('Child', on_delete=models.CASCADE)


class Activity(models.Model):
    activity_type = models.TextField(max_length=50, null=False)
    visit = models.ForeignKey('Visit', on_delete=models.CASCADE)
    caregiver = models.ForeignKey('Caregiver', on_delete=models.CASCADE)




