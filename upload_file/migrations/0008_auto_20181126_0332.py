# Generated by Django 2.0 on 2018-11-26 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_file', '0007_auto_20181126_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='txt',
            name='txt_name',
            field=models.CharField(max_length=200, unique=True, verbose_name='文件名称'),
        ),
        migrations.AlterField(
            model_name='txt',
            name='txt_result',
            field=models.CharField(default='', max_length=200, verbose_name='wc -l /data/logs/tmp_log/guantie_everyday_result/crawl_2018-09-02.txt 执行结果'),
        ),
    ]
