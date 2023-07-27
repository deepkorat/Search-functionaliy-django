from django.db import models
import json

# Create your models here.
class MyModel(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    item = models.TextField(default='{}')

    def __str__(self):
        return self.name
    
    def get_items_dict(self):
        return json.loads(self.item)