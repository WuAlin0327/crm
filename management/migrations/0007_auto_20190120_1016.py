# Generated by Django 2.1.4 on 2019-01-20 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_remove_userinfo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='password',
            field=models.CharField(max_length=256, verbose_name='密码'),
        ),
    ]