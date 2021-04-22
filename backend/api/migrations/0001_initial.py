# Generated by Django 3.2 on 2021-04-20 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('req_hours', models.IntegerField(default=40)),
                ('work_hours', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=191, null=True)),
                ('last_name', models.CharField(blank=True, max_length=191, null=True)),
                ('auth_emp1', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='emp1', to='api.employee')),
                ('auth_emp2', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='emp2', to='api.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrive_time', models.DateTimeField()),
                ('exit_time', models.DateTimeField()),
                ('status', models.SmallIntegerField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.employee')),
            ],
        ),
        migrations.CreateModel(
            name='AbsenseRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.employee')),
            ],
        ),
    ]
