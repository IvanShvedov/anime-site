# Generated by Django 3.1.7 on 2021-02-26 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='episodes',
        ),
        migrations.AddField(
            model_name='episode',
            name='anime',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mainapp.anime', verbose_name='Аниме'),
            preserve_default=False,
        ),
    ]