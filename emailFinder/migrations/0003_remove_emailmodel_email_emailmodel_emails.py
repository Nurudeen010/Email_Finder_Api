# Generated by Django 5.0.2 on 2024-02-16 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailFinder', '0002_emailmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailmodel',
            name='email',
        ),
        migrations.AddField(
            model_name='emailmodel',
            name='emails',
            field=models.TextField(blank=True),
        ),
    ]
