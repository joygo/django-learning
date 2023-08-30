from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    writer = models.CharField(max_length=50, default='anonymous') 
    
    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title