# Generated by Django 2.1.3 on 2018-12-03 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almoxarifado', '0012_categoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='nome_categoria',
            new_name='nome',
        ),
    ]