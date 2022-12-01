# Generated by Django 4.1.3 on 2022-12-01 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_rename_date_patient_bddate_remove_patient_reg_date'),
        ('doctors', '0005_rename_date_doctor_bddate_remove_doctor_reg_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when_made', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=12)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient')),
            ],
        ),
        migrations.AddConstraint(
            model_name='appointment',
            constraint=models.UniqueConstraint(fields=('patient_iin', 'doctor_iin', 'date', 'time'), name='unique_appointment'),
        ),
    ]
