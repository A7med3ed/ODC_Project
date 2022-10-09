from asyncio.windows_events import NULL
from contextlib import nullcontext
from email.policy import default
from unicodedata import name
from django.db import models
from django.forms import CharField

Course=(
     ('DS001D','DS001D'),
     ('UX001H ','UX001H '),
     ('y786J','y786J'),
     ('RG839R','RG839R'),
)



Progress=(
     ('Attended','Attended'),
     ('Failed Interview','Failed Interview'),
     ('Not Invited ','Not Invited '),
     ('Passed Interview','Passed Interview'),
     ('Rejected','Rejected'),
     ('Criteria Not Met','Criteria Not Met'),
)

gender=(
       ('male','male'),
       ('female','female'),
  )

class users(models.Model):
    name = models.CharField(max_length=255)

    joinedCourses=models.CharField(choices=Course,
        max_length = 20
  )

    progress=models.CharField(choices=Progress,
        max_length = 20
       
  )
    
    skills=models.CharField(
        max_length = 255 
       )

    Email=models.EmailField()

    mobile=models.IntegerField(primary_key=True)

    gender=models.CharField(choices=gender,
        max_length = 20
       
  )

class course(models.Model):
     name=models.CharField(max_length=255)
     Prerequisite=models.CharField(max_length=255)
     courseSkills=models.CharField(max_length=255)
     barcode=models.CharField(primary_key=True,max_length=255)
