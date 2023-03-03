from django.db import models

# Create your models here
# from django.db import models

class FormRequest(models.Model):
    contact = models.CharField(max_length=20)
    reason = models.CharField(max_length=200)
    council = models.CharField(max_length=200)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    room = models.CharField(max_length=200)
  
`
