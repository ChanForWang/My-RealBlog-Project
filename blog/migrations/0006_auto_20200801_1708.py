# Generated by Django 3.0.8 on 2020-08-01 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200801_1634'),
    ]

    operations = [
        migrations.RenameField(
            model_name='readnum',
            old_name='read_num',
            new_name='views',
        ),
    ]