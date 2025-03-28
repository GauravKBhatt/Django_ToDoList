from django.db import models
from django.utils import timezone
from datetime import datetime


class Item(models.Model):
    # models by default has id generated by them.
    name = models.CharField(max_length=50)
    description = models.TextField(null=True,blank=True)
    updated= models.DateTimeField(auto_now=True)
    created= models.DateTimeField(auto_now=True)
    ending = models.DateTimeField(default=datetime(2025, 12, 31, 23, 59, 59))
    is_expired = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)

    # this is here to make sure that the recently updated or created rooms will be featured first in the homepage. 
    class Meta:
        ordering =['-updated','-created']

    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
        # Check if the current time is greater than or equal to the 'ending' time
        if timezone.now() >= self.ending:
            self.is_expired = True
        else:
            self.is_expired = False
        super().save(*args, **kwargs)
    
    def mark_as_completed(self, value: bool):
        self.is_completed = value
        self.save()