# Generated by Django 3.2.7 on 2021-09-14 04:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('projects', '0004_auto_20210908_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profiles'),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.UUIDField(default=uuid.UUID('fc1b6f9a-aa89-4883-98e6-0c98fcba5902'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
