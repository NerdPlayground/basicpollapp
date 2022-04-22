import uuid
from django.db import models

class Choice(models.Model):
    id= models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    question= models.ForeignKey(
        'questions.Question',
        related_name='choices',
        on_delete=models.CASCADE
    )
    body= models.CharField(max_length=255)
    votes= models.IntegerField(default=0)

    def __str__(self):
        return self.body