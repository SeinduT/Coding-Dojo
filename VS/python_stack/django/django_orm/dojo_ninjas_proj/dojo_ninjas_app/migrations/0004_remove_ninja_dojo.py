# Generated by Django 2.2 on 2020-09-28 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0003_auto_20200927_2312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ninja',
            name='dojo',
        ),
    ]