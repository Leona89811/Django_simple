# Generated by Django 4.1 on 2023-05-03 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='error_count',
            field=models.IntegerField(blank=True, default=-1, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(blank=True, max_length=32, null=True, unique=True),
        ),
    ]
