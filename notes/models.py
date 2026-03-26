from django.db import models
from django.contrib.auth.models import User

# Note model banaya ja raha hai jo sticky notes ko represent karega
class Note(models.Model):
    # note ka title
    title = models.CharField(max_length=200)

    # note ka content / description
    content = models.TextField()

    # note ka background color (default yellow)
    color = models.CharField(max_length=7, default='#FFFF99')

    # note kab create hua
    created_at = models.DateTimeField(auto_now_add=True)

    # note kab last update hua
    updated_at = models.DateTimeField(auto_now=True)

    # kis user ka note hai
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    # admin panel me readable name dikhane ke liye
    def __str__(self):
        return self.title