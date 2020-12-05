# Generated by Django 3.1 on 2020-12-01 02:21

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('TELLING', '0004_auto_20201108_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='story',
            name='thumbnail',
            field=models.ImageField(upload_to='images'),
        ),
    ]