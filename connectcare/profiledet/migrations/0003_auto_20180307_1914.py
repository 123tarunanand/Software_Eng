# Generated by Django 2.0.2 on 2018-03-07 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiledet', '0002_usermodel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='bg',
            field=models.CharField(choices=[('ab+', 'AB+'), ('ab-', 'AB-'), ('a+', 'A+'), ('a-', 'A-'), ('b+', 'B+'), ('b-', 'B-'), ('o+', 'O+'), ('o-', 'O-')], default='o+', max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='dob',
            field=models.DateField(blank=True, max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='field',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='phno',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='qual',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]