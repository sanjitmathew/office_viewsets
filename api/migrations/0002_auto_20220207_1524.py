# Generated by Django 3.2.5 on 2022-02-07 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teams',
            old_name='name',
            new_name='team_name',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='name',
            new_name='user_name',
        ),
    ]
