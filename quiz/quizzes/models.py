from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#quiz model for quizes
class quiz(models.Model):

    name= models.CharField(max_length=255, verbose_name='name')
    descripion = models.CharField(max_length=255, blank=True,null=True)
    created_on = models.DateTimeField(auto_now=True, verbose_name='Created On')
  
    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Quiz'
        verbose_name_plural='Quizess'
        db_table = 'quiz'


class question(models.Model):
    quiz = models.ForeignKey(quiz,on_delete=models.CASCADE)
    name= models.CharField(max_length=1000, verbose_name='name')
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Question'
        verbose_name_plural='Questions'
        db_table = 'question'

class answer(models.Model):
    question = models.ForeignKey(question,on_delete=models.CASCADE)
    name= models.CharField(max_length=1000, verbose_name='answer')
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Answer'
        verbose_name_plural='Answers'
        db_table = 'answer'


#need to create score and wwho has taken in
class quizAttemptInfo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quiz = models.ForeignKey(quiz,on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now=True, verbose_name='Created On')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name='Attempt'
        verbose_name_plural='Attempts'
        db_table = 'attempt'
        
class response(models.Model):
    attemptee= models.ForeignKey(quizAttemptInfo,on_delete=models.CASCADE)
    question =  models.ForeignKey(question,on_delete=models.CASCADE)
    answer =  models.ForeignKey(answer,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.question.name

    class Meta:
        verbose_name='Response'
        verbose_name_plural='Responses'
        db_table = 'response'