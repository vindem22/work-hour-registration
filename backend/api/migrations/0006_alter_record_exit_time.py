# Generated by Django 3.2 on 2021-04-21 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210421_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='exit_time',
            field=models.DateTimeField(null=True),
        ),
    ]
