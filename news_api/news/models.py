from django.db import models


class Journalist(models.Model):
    """Create database model for Journalist"""

    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    biography = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Airticle(models.Model):
    """Create database model for news articles"""

    author = models.ForeignKey(
        Journalist,
        on_delete=models.CASCADE,
        related_name='articles'
    )

    # author = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    body = models.TextField()
    location = models.CharField(max_length=100)
    publication_date = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by ({self.author})"
