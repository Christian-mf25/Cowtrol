# Generated by Django 4.0.6 on 2022-08-07 15:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('area_name', models.CharField(max_length=255)),
                ('limit_space', models.IntegerField()),
                ('free_space', models.IntegerField()),
                ('occupied_space', models.IntegerField(default=0)),
                ('gmd', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
    ]
