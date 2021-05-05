from django.db import models


class Article(models.Model):
    """Create database model for news articles"""

    author = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    descirption = models.CharField(max_length=250)
    body = models.TextField()
    loacation = models.CharField(max_length=100)
    publication_date = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.title} by ({self.author})"
