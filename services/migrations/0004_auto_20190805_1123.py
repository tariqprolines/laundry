# Generated by Django 2.2.3 on 2019-08-05 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20190804_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignservice',
            name='discount',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assignservice',
            name='grandtotal',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assignservice',
            name='total',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
