import uuid
from django.db import models 


class DaycareAdmin(models.Model):
    name = models.CharField(max_length=50, help_text="Last name, First name")
    role = models.CharField(max_length=50, help_text="your role in the facility")
 

class Classroom(models.Model):
    
    INFANT = 1
    TODDLER = 2
    PRE_K = 3
    
    CATEGORY_CHOICES = (
        (INFANT, 'Infant'),
        (TODDLER, 'Toddler'),
        (PRE_K, 'Pre_k'),
    )
    category = models.PositiveIntegerField(choices=CATEGORY_CHOICES, null=False)
    

class Caregiver(models.Model):
    name = models.CharField(max_length=50, help_text="Last name, First name")
    role = models.CharField(max_length=50, help_text="your role in the facility")
    classroom = models.ForeignKey(to=Classroom, related_name="caregivers", on_delete=models.CASCADE)
    

class Guardian(models.Model):
    name = models.CharField(max_length=50, help_text="Last name, First name")
    phone_number = models.CharField(max_length=12, null=False)
    email = models.EmailField(max_length=254, null=False)
    

class Child(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.CharField(max_length=2, null=False)
    child_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    classroom = models.ForeignKey(to=Classroom, related_name="children", on_delete=models.CASCADE)
    guardians = models.ManyToManyField(to=Guardian, related_name="children")
    child_pic = models.ImageField(null=True)
    allergy = models.TextField(max_length=2000, null=True)



class Visit(models.Model):
    check_in = models.DateTimeField('Check in', auto_now_add=True)
    check_out = models.DateTimeField('Check out', default=False)
    child = models.ForeignKey(to=Child,related_name="visits", on_delete=models.CASCADE)


class Activity(models.Model):
    
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
    caregiver = models.ForeignKey(to=Caregiver, related_name="activities", on_delete=models.CASCADE)
    start_time = models.DateTimeField('Start time', auto_now_add=True)
    end_time = models.DateTimeField('End time', default=False)



