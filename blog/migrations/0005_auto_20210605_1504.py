# Generated by Django 3.1.7 on 2021-06-05 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210605_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='uploade_pics'),
        ),
    ]
