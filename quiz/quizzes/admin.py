from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(quiz, site=admin.site)
class QuizAdmin(admin.ModelAdmin):
    fields = ('name','descripion')


@admin.register(question, site=admin.site)
class QuestionAdmin(admin.ModelAdmin):
    fields = ('name','quiz','order')
    

@admin.register(answer, site=admin.site)
class AnswerAdmin(admin.ModelAdmin):
    fields = ('name','question','correct')
    