# Generated by Django 2.2.9 on 2020-01-04 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('birth_date', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=16)),
            ],
        ),
    ]
