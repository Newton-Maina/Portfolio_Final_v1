# Generated by Django 4.2.3 on 2024-07-18 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('The_Website_v1', '0006_project_image01'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectdetail',
            name='tech1',
            field=models.CharField(default='Tech/You', max_length=200),
        ),
        migrations.AddField(
            model_name='projectdetail',
            name='tech2',
            field=models.CharField(default='Tech/You', max_length=200),
        ),
        migrations.AddField(
            model_name='projectdetail',
            name='tech3',
            field=models.CharField(default='Tech/You', max_length=200),
        ),
        migrations.AddField(
            model_name='projectdetail',
            name='tech4',
            field=models.CharField(default='Tech/You', max_length=200),
        ),
        migrations.AddField(
            model_name='projectdetail',
            name='test_data',
            field=models.TextField(default='More Content Will Be Added Soon'),
        ),
    ]