# Generated by Django 4.2.3 on 2023-07-21 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MataKuliah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_mata_kuliah', models.CharField(max_length=10)),
                ('nama_mata_kuliah', models.CharField(max_length=100)),
                ('jumlah_sks', models.IntegerField()),
                ('program_studi', models.CharField(max_length=50)),
                ('kelas', models.CharField(max_length=10)),
                ('nama_pengajar', models.CharField(max_length=100)),
            ],
        ),
    ]
