# Generated by Django 3.1.4 on 2020-12-23 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0002_auto_20201223_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='name',
            field=models.CharField(max_length=1000, verbose_name='answer'),
        ),
    ]
