# Generated by Django 4.1.3 on 2022-12-04 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0006_appointment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='is_active',
        ),
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='AppointmentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when_made', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField()),
                ('aid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.appointment')),
            ],
        ),
    ]
