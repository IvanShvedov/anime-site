# Generated by Django 3.1.7 on 2021-03-01 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20210301_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='number',
            field=models.PositiveIntegerField(null=True, verbose_name='Номер серии'),
        ),
    ]
