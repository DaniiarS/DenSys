# Generated by Django 4.1.3 on 2022-11-07 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='photo',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]