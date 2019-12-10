# Generated by Django 3.0 on 2019-12-10 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20191210_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_school',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(default='std_img.png', upload_to='students/'),
        ),
    ]
