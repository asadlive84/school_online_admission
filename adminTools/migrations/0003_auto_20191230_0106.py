# Generated by Django 3.0 on 2019-12-29 19:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminTools', '0002_admissionapproval_schoolinformation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admissionapproval',
            name='status_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
