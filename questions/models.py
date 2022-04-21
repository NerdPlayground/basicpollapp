import uuid
from django.db import models

class Question(models.Model):
    id= models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title= models.CharField(max_length=255)
    body= models.TextField()
    updated= models.DateTimeField(auto_now= True)
    created= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title