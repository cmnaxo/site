# Generated by Django 4.0.1 on 2022-05-16 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_itemscarro_creado'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='imagen',
            field=models.ImageField(null=True, upload_to='suscritos'),
        ),
    ]