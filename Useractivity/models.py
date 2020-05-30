from django.db import models
import uuid

class User(models.Model):
    id = models.CharField(primary_key=True,unique=True,max_length=9)
    real_name = models.CharField(max_length=50)
    tz = models.CharField(max_length=50)

    def __str__(self):
        return self.real_name

    def save(self, *args, **kwargs):
        self.id = uuid.uuid4().hex[:9].upper()
        super(User, self).save(*args, **kwargs)

class Activity(models.Model):
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User,related_name='user_activity',on_delete=models.CASCADE)