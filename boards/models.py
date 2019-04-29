from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class category(models.Model):
    category = models.CharField(max_length=200)
    def __str__(self):
        return '{}'.format(self.category)
    
class movie(models.Model):
    
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=200)
    score = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='movies')
    category = models.ForeignKey(category, related_name='posts')
    image = models.ImageField(upload_to='static/image', default = 'static/image/movie_default.png' , blank=True)
    
    def __str__(self):
        return '{}'.format(self.category)
    
