# Generated by Django 3.0 on 2019-12-10 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20191210_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
