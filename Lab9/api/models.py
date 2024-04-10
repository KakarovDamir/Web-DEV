from tabnanny import verbose
from django.db import models

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    city = models.CharField(max_length=200)
    address = models.TextField()

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address,
        }
    
    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
    


class Vacancy(models.Model):
    id =  models.AutoField(primary_key=True)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


    def to_json(self):
        return {
            'id': self.id,
            'description': self.description,
            'salary': self.salary,
            'company': self.company.to_json()
        }
    

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'