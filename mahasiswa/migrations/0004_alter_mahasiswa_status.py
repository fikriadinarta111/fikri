# Generated by Django 4.2.3 on 2023-08-01 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mahasiswa', '0003_mahasiswa_status_alter_mahasiswa_jk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahasiswa',
            name='status',
            field=models.CharField(choices=[('Aktif', 'Aktif'), ('Tidak Aktif', 'Tidak Aktif')], default='Aktif', max_length=100),
        ),
    ]
