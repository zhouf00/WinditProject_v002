# Generated by Django 2.2.6 on 2020-02-06 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile_roles'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ['id'], 'verbose_name': '用户信息', 'verbose_name_plural': '用户信息'},
        ),
    ]
