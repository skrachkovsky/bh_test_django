# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 19:24
from __future__ import unicode_literals

from django.db import migrations, models

def fill_values(apps, schaema_editor):
    i = 1
    Table1 = apps.get_model('main', 'Table1')
    db = schaema_editor.connection.alias
    for item in Table1.objects.using(db).all():
        item.field1 = str(i)
        item.save()
        i += 1


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='table1',
            name='field1',
            field=models.CharField(null=True, max_length=20),
            preserve_default=False,
        ),
        migrations.RunPython(fill_values),
        migrations.AlterField(
            model_name='table1',
            name='field1',
            field=models.CharField(null=False, max_length=20, unique=True),
            preserve_default=False,
        )
    ]
