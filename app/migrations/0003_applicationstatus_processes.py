# Generated by Django 4.2.11 on 2024-03-31 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_applicationstatus_valid_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationstatus',
            name='processes',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
