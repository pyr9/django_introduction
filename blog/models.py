from django.db import models

# Create your models here.
from django.db import models
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)