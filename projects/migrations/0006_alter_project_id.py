# Generated by Django 3.2.7 on 2021-09-14 04:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20210914_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.UUIDField(default=uuid.UUID('eaa356e1-9351-405b-b461-5743e842078a'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
