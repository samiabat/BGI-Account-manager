# Generated by Django 4.0.4 on 2022-07-11 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_manager_app', '0005_alter_sector_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='deleted',
            field=models.CharField(choices=[('1', 1), ('0', 0)], default='0', max_length=2),
        ),
    ]
