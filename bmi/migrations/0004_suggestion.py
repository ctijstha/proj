# Generated by Django 3.1.7 on 2021-04-25 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmi', '0003_auto_20210425_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Underweight', 'Underweight'), ('Normal', 'Normal'), ('Overweight', 'Overweight'), ('Obese', 'Obese')], max_length=25)),
                ('message', models.TextField()),
            ],
        ),
    ]
