from django.db import models
from django.urls import reverse

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    
