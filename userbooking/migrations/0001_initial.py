# Generated by Django 4.1.7 on 2023-03-03 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Contact', models.CharField(max_length=20)),
                ('Reason', models.CharField(max_length=200)),
                ('Council', models.CharField(max_length=100)),
                ('Room', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
    ]