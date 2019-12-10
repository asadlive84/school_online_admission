# Generated by Django 3.0 on 2019-12-10 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=100, verbose_name='Section Name')),
            ],
        ),
        migrations.CreateModel(
            name='AcademicSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BloodGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_group_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=50, unique=True, verbose_name='Class Name')),
                ('class_name_numeric', models.PositiveIntegerField(unique=True, verbose_name='Class Name - Numeric')),
            ],
        ),
        migrations.CreateModel(
            name='StudentGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=100, unique=True, verbose_name='Group Name')),
            ],
        ),
        migrations.CreateModel(
            name='Union',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Zilla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WordNo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Word Name')),
                ('name_of_numeric', models.PositiveIntegerField(verbose_name='Word No')),
                ('union', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminTools.Union')),
            ],
        ),
        migrations.CreateModel(
            name='Upazilla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('zilla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminTools.Zilla')),
            ],
        ),
        migrations.AddField(
            model_name='union',
            name='upazilla',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminTools.Upazilla'),
        ),
    ]
