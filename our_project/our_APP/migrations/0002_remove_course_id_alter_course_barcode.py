# Generated by Django 4.1.1 on 2022-10-07 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('our_APP', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='id',
        ),
        migrations.AlterField(
            model_name='course',
            name='barcode',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
