from django.db import models

# Create your models here.

class UploadFile(models.Model):
    #status = models.ForeignKey(TaskStatus, null=False, related_name="t_status")
    task_name = models.CharField(max_length=50)
    t_file = models.FileField(upload_to='documents/%Y/%m/%d')
 
    def __unicode__(self):
        return self.task_name

class Image(models.Model):
    image = models.ImageField(upload_to='static/')
