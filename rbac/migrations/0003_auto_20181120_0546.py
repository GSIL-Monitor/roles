# Generated by Django 2.0 on 2018-11-20 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0002_auto_20181120_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password_hash',
            field=models.CharField(max_length=100, verbose_name='登录密码'),
        ),
    ]
