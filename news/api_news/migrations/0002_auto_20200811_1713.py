# Generated by Django 2.2.5 on 2020-08-11 14:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api_news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='creation_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 8, 11, 14, 13, 40, 717541, tzinfo=utc)),
        ),
    ]