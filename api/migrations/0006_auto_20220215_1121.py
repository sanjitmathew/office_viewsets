# Generated by Django 3.2.5 on 2022-02-15 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_users_team_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='team_id',
        ),
        migrations.AddField(
            model_name='users',
            name='team_id',
            field=models.ManyToManyField(to='api.Teams'),
        ),
    ]
