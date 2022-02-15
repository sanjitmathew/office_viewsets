# Generated by Django 3.2.5 on 2022-02-15 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_users_team_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='team_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.teams'),
        ),
    ]