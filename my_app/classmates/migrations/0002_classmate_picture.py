# Generated by Django 4.2.7 on 2023-11-09 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classmates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classmate',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='classmate_pics/'),
        ),
    ]
