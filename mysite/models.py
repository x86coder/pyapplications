from django.db import models
from django.utils import timezone

class Job(models.Model):
    role_text = models.CharField(max_length=128, null=True, blank=True)
    company_text = models.CharField(max_length=32, null=True, blank=True)
    source_text = models.CharField(max_length=32, null=True, blank=True)
    salary_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_expected = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discarded = models.BooleanField(default=False, blank=True)
    primary_reference_text = models.TextField(null=True, blank=True)
    secondary_reference_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.role_text

class Step(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name_text = models.CharField(max_length=32)
    date = models.DateTimeField(default=timezone.now)
    comments_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name_text

class Wished(models.Model):
    role_text = models.CharField(max_length=128, null=True, blank=True)
    company_text = models.CharField(max_length=32, null=True, blank=True)
    salary= models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discarded = models.BooleanField(default=False, blank=True)
    date_added = models.DateTimeField(default=timezone.now)
    url = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.role_text