# Generated by Django 4.2.3 on 2024-07-17 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('The_Website_v1', '0004_remove_project_detail_paragraph1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='overview',
        ),
        migrations.AlterField(
            model_name='projectdetail',
            name='overview',
            field=models.TextField(default='More Content Will Be Added Soon'),
        ),
    ]