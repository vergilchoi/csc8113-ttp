# Generated by Django 3.0.4 on 2020-03-15 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0002_auto_20200315_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='session_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
