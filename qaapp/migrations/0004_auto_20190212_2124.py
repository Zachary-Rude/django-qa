# Generated by Django 2.1.4 on 2019-02-12 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qaapp', '0003_questionvote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionvote',
            name='vote',
            field=models.SmallIntegerField(verbose_name='Vote count'),
        ),
    ]