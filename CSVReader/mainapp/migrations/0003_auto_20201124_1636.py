# Generated by Django 3.1.2 on 2020-11-24 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20201124_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvdata',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
