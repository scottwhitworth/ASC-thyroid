from django.db import models

# Create your models here.

class Reference(models.Model):
    """docstring"""
    title = models.CharField(max_length=750)
    link = models.URLField(verify_exists=False, max_length=200)
    
    def __unicode__(self):
        return self.title
        

class Category(models.Model):
    type = models.CharField(max_length=50)
    order = models.IntegerField(unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.type


class Diagnosis(models.Model):
    """docstring"""
    text = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name='diagnosis')
    description = models.TextField(blank=True)
    references = models.ManyToManyField(Reference, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Diagnoses'

    def __unicode__(self):
        return self.text
