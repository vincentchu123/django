# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Question,Choice

# Register your models here.
class ChoiceInline(admin.TabularInline): #内联显示
   	model = Choice #quesrtion是choice的外键
    #extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
    	(None,{'fields': ['question_text']}), #输入栏分块 自定义表单
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),#classes css样式 此处可让pub_data隐藏
	]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')#列表页显示更多的栏目
           
admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)#注册多个模型