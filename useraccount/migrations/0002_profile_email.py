# Generated by Django 3.1.7 on 2021-05-05 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
