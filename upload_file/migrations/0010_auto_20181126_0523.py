# Generated by Django 2.0 on 2018-11-26 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload_file', '0009_auto_20181126_0520'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='txt',
            new_name='txt_id',
        ),
    ]
