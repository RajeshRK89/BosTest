from django.db import models

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

