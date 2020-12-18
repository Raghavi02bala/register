import uuid
from django.db import models

class Employee(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    email = models.EmailField(max_length=300)
    
