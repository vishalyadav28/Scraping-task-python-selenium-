from django.db import models

# Create your models here.

class DataStore(models.Model):
    company_name = models.CharField(max_length=100,null=False,unique=True)
    # report_url = models.URLField(blank=False,null=False)
    report_data = models.URLField(blank=False,null=False)
    plan_id = models.CharField(null=False, unique=True,max_length=100)