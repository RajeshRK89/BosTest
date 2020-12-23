from django.contrib import admin
from nested_inline.admin import NestedTabularInline,NestedModelAdmin
from .models import *

class AnswerInline(NestedTabularInline):
    
    model = answer
    max_num =3

class QuestionInline(NestedTabularInline):
    inlines = [AnswerInline,]
    model = question

@admin.register(quiz, site=admin.site)
class QuizAdmin(NestedModelAdmin):
    inlines = [QuestionInline,]

# Register your models here.
# admin.site.register(quiz, QuizAdmin)
# class QuizAdmin(admin.ModelAdmin):
    # fields = ('name','descripion')

class ResponseInline(NestedTabularInline):
    model = response

@admin.register(quizAttemptInfo, site=admin.site)  
class AttemptInline(admin.ModelAdmin):
    inlines= [ResponseInline,]
    exclude=['correct',]


# @admin.register(question, site=admin.site)
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ('name','quiz','order')
    

# @admin.register(answer, site=admin.site)
# class AnswerAdmin(admin.ModelAdmin):
#     fields = ('name','question','correct')
    