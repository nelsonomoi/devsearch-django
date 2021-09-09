# Generated by Django 3.2.7 on 2021-09-06 05:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.UUIDField(default=uuid.UUID('46ec4ce5-4617-4496-b757-d191b6c6d0c7'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]