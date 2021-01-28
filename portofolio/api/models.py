from django.db import models

# Create your models here.
class Blogpost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} created at {self.created_at}"

class Repository(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=360)
    created_at = models.DateField()
    github_url = models.URLField()

    def __str__(self):
        return f"{self.name} with description {self.description}, created at {self.created_at} and with url {self.github_url}"
    