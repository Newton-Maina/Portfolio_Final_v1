# Generated by Django 4.2.3 on 2024-08-12 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('The_Website_v1', '0010_alter_post_created_on_alter_post_updated_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectdetail',
            name='detail_paragraph4',
            field=models.TextField(default='More Content Will Be Added Soon'),
        ),
    ]
