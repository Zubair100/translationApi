from django.db import models

# Create your models here.


class Animal(models.Model):
    animal_id = models.IntegerField(primary_key=True)
    animal_names = models.CharField(max_length=100)


class ProtectionStatus(models.Model):
    PROTECTION_STATUS = (
        ('LC', 'Least Concern'),
        ('CD', 'Conservation Dependent'),
        ('NT', 'Near Threatened'),
        ('VU', 'Vulnerable'),
        ('EN', 'Endangered'),
        ('CR', 'Critically Endangered'),
        ('EW', 'Extinct in the wild'),
        ('EX', 'Extinct'),
    )
    animal_id = models.ForeignKey(Animal, on_delete=models.CASCADE)
    animal_protection_status = models.CharField(max_length=2,choices=PROTECTION_STATUS)




