# Generated by Django 2.1.3 on 2018-12-02 15:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
