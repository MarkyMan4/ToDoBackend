# Generated by Django 3.1 on 2020-08-09 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todo_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date_completed',
            field=models.DateField(null=True),
        ),
    ]