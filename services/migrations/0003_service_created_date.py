# Generated by Django 2.2.3 on 2019-07-15 06:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20190714_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
