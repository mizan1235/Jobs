# Generated by Django 4.2.3 on 2023-12-06 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_job_details_apply_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_details',
            name='username',
            field=models.CharField(default='rahul123', max_length=40),
        ),
    ]
