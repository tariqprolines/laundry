# Generated by Django 2.2.3 on 2019-08-06 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_auto_20190806_1043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignservice_detail',
            old_name='service_id',
            new_name='service',
        ),
    ]