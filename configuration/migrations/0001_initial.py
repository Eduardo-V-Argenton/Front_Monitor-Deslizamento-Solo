# Generated by Django 4.1.7 on 2023-10-22 22:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addh', models.IntegerField(default=0)),
                ('addl', models.IntegerField(default=0)),
                ('transmission_power', models.CharField(default='0', max_length=1)),
                ('enable_lbt', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ControlModule',
            fields=[
                ('module_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='configuration.module')),
                ('read_command_period', models.FloatField(default=3)),
            ],
            bases=('configuration.module',),
        ),
        migrations.CreateModel(
            name='SensorModule',
            fields=[
                ('module_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='configuration.module')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('channel', models.IntegerField(default=64)),
                ('wor_period', models.CharField(default='3', max_length=1)),
                ('air_data_rate', models.CharField(default='2', max_length=1)),
                ('crypth', models.IntegerField(default=0)),
                ('cryptl', models.IntegerField(default=0)),
                ('timeout_sensors_read_packet', models.FloatField(default=60)),
                ('timeout_config_packet', models.FloatField(default=60)),
                ('timeout_handshake', models.FloatField(default=30)),
                ('timeout_SYNACK', models.FloatField(default=3)),
                ('timeout_ACK', models.FloatField(default=3)),
                ('auto_send_sensors_period', models.IntegerField(default=10)),
                ('next_sensors_read', models.DateTimeField(auto_now_add=True)),
                ('city', models.CharField(default='São Paulo', max_length=255)),
                ('country', models.CharField(default='BR', max_length=2)),
                ('air_soil_moisture_value', models.IntegerField(default=600)),
                ('water_soil_moisture_value', models.IntegerField(default=350)),
                ('LC', models.IntegerField(default=25)),
                ('LP', models.IntegerField(default=50)),
                ('LL', models.IntegerField(default=75)),
                ('accel_last_x', models.FloatField(default=0)),
                ('accel_last_y', models.FloatField(default=0)),
                ('accel_last_z', models.FloatField(default=0)),
            ],
            bases=('configuration.module',),
        ),
        migrations.CreateModel(
            name='ModuleObserver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_controller', models.BooleanField(default=False)),
                ('executed', models.BooleanField(default=False)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_module', to='configuration.module')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalSensorModule',
            fields=[
                ('module_ptr', models.ForeignKey(auto_created=True, blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, parent_link=True, related_name='+', to='configuration.module')),
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('addh', models.IntegerField(default=0)),
                ('addl', models.IntegerField(default=0)),
                ('transmission_power', models.CharField(default='0', max_length=1)),
                ('enable_lbt', models.BooleanField(default=False)),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('channel', models.IntegerField(default=64)),
                ('wor_period', models.CharField(default='3', max_length=1)),
                ('air_data_rate', models.CharField(default='2', max_length=1)),
                ('crypth', models.IntegerField(default=0)),
                ('cryptl', models.IntegerField(default=0)),
                ('timeout_sensors_read_packet', models.FloatField(default=60)),
                ('timeout_config_packet', models.FloatField(default=60)),
                ('timeout_handshake', models.FloatField(default=30)),
                ('timeout_SYNACK', models.FloatField(default=3)),
                ('timeout_ACK', models.FloatField(default=3)),
                ('auto_send_sensors_period', models.IntegerField(default=10)),
                ('next_sensors_read', models.DateTimeField(blank=True, editable=False)),
                ('city', models.CharField(default='São Paulo', max_length=255)),
                ('country', models.CharField(default='BR', max_length=2)),
                ('air_soil_moisture_value', models.IntegerField(default=600)),
                ('water_soil_moisture_value', models.IntegerField(default=350)),
                ('LC', models.IntegerField(default=25)),
                ('LP', models.IntegerField(default=50)),
                ('LL', models.IntegerField(default=75)),
                ('accel_last_x', models.FloatField(default=0)),
                ('accel_last_y', models.FloatField(default=0)),
                ('accel_last_z', models.FloatField(default=0)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical sensor module',
                'verbose_name_plural': 'historical sensor modules',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalControlModule',
            fields=[
                ('module_ptr', models.ForeignKey(auto_created=True, blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, parent_link=True, related_name='+', to='configuration.module')),
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('addh', models.IntegerField(default=0)),
                ('addl', models.IntegerField(default=0)),
                ('transmission_power', models.CharField(default='0', max_length=1)),
                ('enable_lbt', models.BooleanField(default=False)),
                ('read_command_period', models.FloatField(default=3)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical control module',
                'verbose_name_plural': 'historical control modules',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
