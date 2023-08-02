# Generated by Django 4.2.3 on 2023-07-31 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dosen_pengajar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dosenpengajarmodel',
            name='jk',
            field=models.CharField(choices=[('L', 'Laki-Laki'), ('P', 'Perempuan')], default='L', max_length=20),
        ),
        migrations.AlterField(
            model_name='dosenpengajarmodel',
            name='status',
            field=models.CharField(choices=[('Aktif', 'Aktif'), ('Tidak Aktif', 'Tidak Aktif')], default='A', max_length=100),
        ),
    ]