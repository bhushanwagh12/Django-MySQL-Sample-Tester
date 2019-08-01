from django.db import models

# Create your models here.
class company(models.Model):
    company_no=models.IntegerField(null=None)
    company_name=models.CharField(max_length=20)
    company_address=models.CharField(max_length=20)
    company_city=models.CharField(max_length=30)
    company_email=models.EmailField(max_length=50)
    def __str__(self):
        return self.company_name
