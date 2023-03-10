# Generated by Django 4.1.5 on 2023-03-07 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0004_alter_tasks_labels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='labels',
            field=models.ManyToManyField(blank=True, related_name='label', through='tasks.TaskToLabels', to='labels.labels'),
        ),
    ]
