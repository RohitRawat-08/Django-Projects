# Generated by Django 5.1 on 2024-08-20 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Place', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
    ]
