# Generated by Django 3.1 on 2020-08-08 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.CharField(default='', max_length=4000, null=True),
        ),
    ]
