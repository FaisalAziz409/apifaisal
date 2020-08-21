from django.db import models

# Create your models here.

from django.contrib.auth import get_user_model

User= get_user_model()

class Post(models.Model):
    title= models.CharField(max_length=255)
    desc= models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    # owner= models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title