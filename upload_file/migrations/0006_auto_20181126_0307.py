# Generated by Django 2.0 on 2018-11-26 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_file', '0005_auto_20181126_0300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='txt',
            name='date',
        ),
        migrations.AlterField(
            model_name='txt',
            name='txt_result',
            field=models.CharField(default='', max_length=32, verbose_name='wc -l /data/logs/tmp_log/guantie_everyday_result/crawl_2018-09-02.txt 执行结果'),
        ),
    ]
