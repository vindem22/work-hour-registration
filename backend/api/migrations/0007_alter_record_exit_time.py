# Generated by Django 3.2 on 2021-04-21 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_record_exit_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='exit_time',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
