# Generated by Django 3.0 on 2019-12-27 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20191213_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(blank=True, default=True, upload_to='images/'),
        ),
    ]
