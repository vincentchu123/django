# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')
admin.site.register(Blog, BlogAdmin)
#作者
  
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()                     
    def __unicode__(self):
    	return self.first_name       
  # 出版商
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    ddress = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    def __unicod__(self):
        return self.name 
