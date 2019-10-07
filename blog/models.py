from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=255)
    pub_date=models.DateTimeField()
    image=models.ImageField(upload_to='image/')
    body=models.TextField()

    def summary(self):
        return self.body[:50]


    def __str__(self):
        return self.title
