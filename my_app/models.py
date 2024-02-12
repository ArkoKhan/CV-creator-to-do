from django.db import models

# Create your models here.
class Scheduler(models.Model):
    task = models.CharField(max_length= 20)
    task_date= models.DateField()
    task_time = models.TimeField()

    def __str__(self):
        return self.task


class personalCV(models.Model):
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')

    ]


    name = models.CharField(max_length= 25)
    dob = models.DateField()
    gender= models.CharField(max_length=9, choices= GENDER)
    image = models.ImageField(upload_to='images/', default='def.jpg')
    address = models.TextField(max_length= 200)
    summary = models.TextField(max_length= 3000, default="HEllo")

    def __str__(self):
        return self.name
    

class Education(models.Model):
    
    institute = models.CharField(max_length=30)
    graduation_date = models.DateField()

    def __str__(self):
        return self.institute

    
class Work(models.Model):
    
    workplace = models.CharField(max_length=30)
    start_date = models.DateField()

    def __str__(self):
        return self.workplace
    


class Skils(models.Model):
    skill_name= models.CharField(max_length=20)
    skill_detail = models.TextField(max_length= 200)

    def __str__(self):
        return self.skill_name
    
