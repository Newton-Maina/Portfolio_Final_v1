# Generated by Django 4.2.3 on 2024-08-12 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('The_Website_v1', '0011_projectdetail_detail_paragraph4'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectdetail',
            name='laptop_mockup',
            field=models.ImageField(default='More Content Will Be Added Soon', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='projectdetail',
            name='phone_mockup_01',
            field=models.ImageField(default='More Content Will Be Added Soon', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='projectdetail',
            name='phone_mockup_02',
            field=models.ImageField(default='More Content Will Be Added Soon', upload_to='images/'),
        ),
    ]