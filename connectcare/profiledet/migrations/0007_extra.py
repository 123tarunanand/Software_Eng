# Generated by Django 2.0.2 on 2018-03-07 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiledet', '0006_auto_20180307_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qu', models.CharField(blank=True, max_length=255, null=True)),
                ('fi', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]