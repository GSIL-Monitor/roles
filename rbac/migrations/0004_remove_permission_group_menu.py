# Generated by Django 2.0.6 on 2018-11-20 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0003_auto_20181120_0546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permission',
            name='group_menu',
        ),
    ]