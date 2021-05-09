from django.db import models


class JobOffer(models.Model):
    """Create Job Offer model"""

    company_name = models.CharField(max_length=150)
    company_email = models.CharField(max_length=100)
    job_title = models.CharField(max_length=250)
    job_description = models.TextField()
    salary = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name
