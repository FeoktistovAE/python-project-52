# Generated by Django 4.1.5 on 2023-03-12 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labels',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Name'),
        ),
    ]