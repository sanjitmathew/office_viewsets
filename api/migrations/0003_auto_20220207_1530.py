# Generated by Django 3.2.5 on 2022-02-07 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220207_1524'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teams',
            old_name='team_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='user_name',
            new_name='name',
        ),
    ]