# Generated by Django 4.0.1 on 2022-05-16 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_created_at_itemscarro_creado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemscarro',
            name='creado',
        ),
    ]
