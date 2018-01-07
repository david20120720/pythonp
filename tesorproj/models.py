from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Article(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    contents = models.TextField()
    #http:\\ 는 에러발생함 , //로 해야 정상작동함
    url=models.URLField()
    email=models.EmailField()
    cdate=models.DateTimeField(auto_now_add=True)