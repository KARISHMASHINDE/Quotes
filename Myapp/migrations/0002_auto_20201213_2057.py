# Generated by Django 3.1.4 on 2020-12-13 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myquotes',
            name='Rating',
        ),
        migrations.AddField(
            model_name='myquotes',
            name='likes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
