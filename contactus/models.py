from django.db import models


class Contact(models.Model):
    """
    Contact model
    """
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    message = models.TextField(max_length=500)
    sent_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-sent_time']

    def __str__(self):
        return f"{self.name}'s Contact message"
