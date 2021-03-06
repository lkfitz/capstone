# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-11 20:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

def link_case_tables(apps, schema_editor):
    if not schema_editor.connection.alias == 'default':
        return
    cursor = schema_editor.connection.cursor()
    cursor.execute("""
      UPDATE capdb_casexml as cx 
      SET metadata_id = cm.id
      FROM capdb_casemetadata as cm
      WHERE cx.case_id = cm.case_id
    """)


class Migration(migrations.Migration):

    dependencies = [
        ('capdb', '0012_auto_20171116_2045'),
    ]

    operations = [

        # turn casexml.case_id into foreign key casexml.metadata_id:

        migrations.AddField(
            model_name='casexml',
            name='metadata',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='case_xml', to='capdb.CaseMetadata'),
        ),
        migrations.RunPython(link_case_tables),

        # make case_id non-unique for now -- will be deleted once migration confirmed
        migrations.AlterField(
            model_name='casexml',
            name='case_id',
            field=models.CharField(db_index=True, max_length=255),
        ),

        # turn volumexml.barcode into foreign key volumexml.metadata_id:

        migrations.AlterField(
            model_name='volumexml',
            name='barcode',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='volume_xml', to='capdb.VolumeMetadata'),
        ),
        migrations.RenameField(
            model_name='volumexml',
            old_name='barcode',
            new_name='metadata',
        ),
    ]
