# Generated by Django 3.1.12 on 2023-06-26 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productApi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='location',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='masterName',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='methodology',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='ownerName',
            field=models.CharField(max_length=500),
        ),
    ]