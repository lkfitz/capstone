# Generated by Django 2.0.8 on 2018-10-16 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capdb', '0053_auto_20181012_2045'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='casemetadata',
            name='capdb_casem_tsvecto_a0d06d_gin',
        ),
        migrations.RemoveField(
            model_name='casemetadata',
            name='tsvector',
        ),
    ]
