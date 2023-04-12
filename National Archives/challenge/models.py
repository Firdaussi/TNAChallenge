from django.db import models

# Create your models here.
class TNARecord(models.Model):
    tna_id = models.CharField(
        primary_key=True,
        max_length=128)
    title = models.CharField(
        max_length=256,
        null=True)
    description = models.CharField(
        max_length=256,
        null=True)
    citable = models.CharField(
        max_length=256,
        null=True)

    def __str__(self):
        strRepresentation = None

        if self.title != None:
            strRepresentation = self.title
        elif self.description != None:
            strRepresentation = self.description
        elif self.citable != None:
            strRepresentation = self.citable
        else:
            strRepresentation = self.tna_id
            
        return strRepresentation
