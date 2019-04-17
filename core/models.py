import uuid
from django.db import models 
from django.contrib.auth.models import User


class Classroom(models.Model):
    
    classroom = models.CharField(max_length=254, null=False)
    caregiver = models.ForeignKey(to=User, related_name="classrooms", on_delete=models.CASCADE)

    def __str__(self):
        return self.classroom


class Guardian(models.Model):
    name = models.CharField(max_length=50, help_text="Last name, First name")
    phone_number = models.CharField(max_length=12, null=False)
    email = models.EmailField(max_length=254, null=False)

    def __str__(self):
        return self.name
    

class Child(models.Model):

    class Meta:
        verbose_name_plural = "children"

    full_name = models.CharField(max_length=254)
    age = models.CharField(max_length=2, null=False)
    child_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    classroom = models.ForeignKey(to=Classroom, related_name="children", on_delete=models.CASCADE)
    guardians = models.ManyToManyField(to=Guardian, related_name="children")
    child_pic = models.ImageField(blank=True, null=True)
    allergy = models.TextField(max_length=2000, null=True)

    def __str__(self):
        return self.full_name


class Visit(models.Model):
    check_in = models.DateTimeField('Check in', auto_now_add=True)
    check_out = models.DateTimeField('Check out', default=False)
    child = models.ForeignKey(to=Child,related_name="visits", on_delete=models.CASCADE)

    def __str__(self):
        return self.check_in


class Activity(models.Model):

    class Meta:
        verbose_name_plural = "activities"
    
    FOOD = 'FD'
    NURSE = 'NS'
    BOTTLE = 'BT'
    NAP = 'NP'
    DIAPER1 = 'DP1'
    DIAPER2 = 'DP2'
    
    ACTIVITY_TYPES = (
        (FOOD, 'Food'),
        (NURSE,'Nurse'),
        (BOTTLE, 'Bottle'),
        (NAP, 'Nap'),
        (DIAPER1, 'Diaper1'),
        (DIAPER2, 'Diaper2'),
    )
    activity_type = models.CharField(max_length=2, choices=ACTIVITY_TYPES, null=False)
    visit = models.ForeignKey(to=Visit, related_name="activities", on_delete=models.CASCADE)
    child = models.ForeignKey(to=Child, related_name="activities", on_delete=models.CASCADE)
    start_time = models.DateTimeField('Start time', auto_now_add=True)
    end_time = models.DateTimeField('End time', default=False)

    def __str__(self):
        return self.activity_type
