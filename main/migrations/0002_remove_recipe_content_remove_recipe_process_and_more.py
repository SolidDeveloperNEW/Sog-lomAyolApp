# Generated by Django 5.0 on 2024-05-01 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='content',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='process',
        ),
        migrations.AddField(
            model_name='recipe',
            name='contents',
            field=models.ManyToManyField(to='main.content'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='processes',
            field=models.ManyToManyField(to='main.process'),
        ),
    ]