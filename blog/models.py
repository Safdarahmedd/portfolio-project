from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to='images/')
    body  = models.TextField()
    date_pub = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
