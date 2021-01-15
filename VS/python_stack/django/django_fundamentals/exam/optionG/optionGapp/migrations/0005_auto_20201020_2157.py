# Generated by Django 2.2 on 2020-10-21 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('optionGapp', '0004_auto_20201020_1740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotes',
            name='user_likes',
        ),
        migrations.RemoveField(
            model_name='quotes',
            name='user_quotes',
        ),
        migrations.AddField(
            model_name='quotes',
            name='created_by',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='usersquotes', to='optionGapp.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quotes',
            name='liked_by',
            field=models.ManyToManyField(related_name='likedquotes', to='optionGapp.User'),
        ),
    ]
