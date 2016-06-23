from __future__ import unicode_literals

from django.db import models

# Create your models here..
# question
class Question(models.Model):
    question_text = models.CharField(max_length=200) 
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
		return self.question_text
# chioce
class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
   		return self.choice_text
