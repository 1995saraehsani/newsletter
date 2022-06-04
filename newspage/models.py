from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse

# Create your models here.
class AuthorSportPage(models.Model):
    title=models.CharField(max_length=250)
    author=models.ForeignKey(
        'auth.User',
        on_delete=CASCADE,
        null=True,
        blank=True,
    )
    text=models.TextField()
    def __str__(self):
        return self.text
    def get_absolute_url(self):
        return reverse("sport_detail", args=[str(self.id)])
    
    
class AuthorTechnologyPage(models.Model):
    title=models.CharField(max_length=250)
    author=models.ForeignKey(
        'auth.User',
        on_delete=CASCADE, 
        null=True,
        blank=True,
    )
    text=models.TextField()
    def __str__(self):
        return self.text
    
    def get_absolute_url(self):
        return reverse("technology_detail", args=[str(self.id)])
    
    
class AuthorPoliticPage(models.Model):
    title=models.CharField(max_length=250)
    author=models.ForeignKey(
        'auth.User',
        on_delete=CASCADE,
        null=True,
        blank=True,
    )
    text=models.TextField()
    def __str__(self):
        return self.text
    
    def get_absolute_url(self):
        return reverse("politic_detail", args=[str(self.id)])
    
    