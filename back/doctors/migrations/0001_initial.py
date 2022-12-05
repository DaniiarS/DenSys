# Generated by Django 4.1.3 on 2022-12-05 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import doctors.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0004_user_is_active'),
        ('patients', '0002_rename_date_patient_bddate_remove_patient_reg_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('middlename', models.CharField(max_length=200)),
                ('bddate', models.CharField(max_length=10)),
                ('id', models.CharField(max_length=12)),
                ('education', models.CharField(max_length=3)),
                ('department', models.CharField(max_length=200)),
                ('specialization', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('photo', models.FileField(upload_to='images/')),
                ('working_hours', models.JSONField(default=list)),
                ('duration', models.CharField(max_length=5)),
                ('price', models.CharField(max_length=10)),
                ('contact_number', models.CharField(max_length=12)),
                ('experience', models.CharField(max_length=3)),
                ('url', models.CharField(blank=True, max_length=200)),
                ('address', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=('accounts.user',),
            managers=[
                ('objects', doctors.models.AccountManager()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=10)),
                ('working_hours', models.JSONField(default=list)),
                ('duration', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceRequestStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when_made', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField()),
                ('srid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.appointment')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=12)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.service')),
            ],
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
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.doctor'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient'),
        ),
    ]
