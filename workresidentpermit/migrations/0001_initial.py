# Generated by Django 4.2.11 on 2024-04-19 12:51

import _socket
import base_module.model_fields.hostname_modification_field
import base_module.model_fields.userfield
import base_module.model_fields.uuid_auto_field
import base_module.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0011_rename_comment_applicationversion_app_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkResidencePermit',
            fields=[
                ('created', models.DateTimeField(blank=True, default=base_module.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=base_module.utils.get_utcnow)),
                ('user_created', base_module.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', base_module.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', base_module.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('id', base_module.model_fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('file_number', models.CharField(max_length=190)),
                ('preferred_method_comm', models.CharField(choices=[('sms', 'SMS'), ('post', 'POST'), ('email', 'EMAIL')], max_length=190)),
                ('preferred_method_comm_value', models.CharField(max_length=190)),
                ('language', models.CharField(max_length=190)),
                ('state_period_required', models.DateField()),
                ('propose_work_employment', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=4)),
                ('reason_applying_permit', models.CharField(choices=[('dependent', 'Dependent'), ('volunteer', 'Volunteer'), ('student', 'Student'), ('immigrant', 'Immigrant'), ('missionary', 'Missionary')], max_length=190)),
                ('documentary_proof', models.CharField(max_length=190)),
                ('travelled_on_pass', models.CharField(max_length=190)),
                ('is_spouse_applying_residence', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=190)),
                ('ever_prohibited', models.TextField()),
                ('sentenced_before', models.TextField()),
                ('entry_place', models.CharField(max_length=190)),
                ('arrival_date', models.DateField()),
                ('application_version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.applicationversion')),
            ],
            options={
                'verbose_name': 'Work Residence Permits',
            },
        ),
        migrations.CreateModel(
            name='Spouse',
            fields=[
                ('created', models.DateTimeField(blank=True, default=base_module.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=base_module.utils.get_utcnow)),
                ('user_created', base_module.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', base_module.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', base_module.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('id', base_module.model_fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('spouse_last_name', models.CharField(max_length=190)),
                ('spouse_first_name', models.CharField(max_length=190)),
                ('spouse_middle_name', models.CharField(max_length=190)),
                ('spouse_maiden_name', models.CharField(max_length=190)),
                ('spouse_country', models.CharField(max_length=190)),
                ('spouse_place_birth', models.CharField(max_length=190)),
                ('spouse_dob', models.DateField()),
                ('work_resident_permit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workresidentpermit.workresidencepermit')),
            ],
            options={
                'verbose_name': 'Spouse',
            },
        ),
        migrations.CreateModel(
            name='Permit',
            fields=[
                ('created', models.DateTimeField(blank=True, default=base_module.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=base_module.utils.get_utcnow)),
                ('user_created', base_module.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', base_module.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', base_module.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('id', base_module.model_fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('permit_type', models.CharField(max_length=190)),
                ('permit_no', models.CharField(max_length=190)),
                ('date_issued', models.DateField()),
                ('date_expiry', models.DateField()),
                ('place_issue', models.CharField(max_length=190)),
                ('work_resident_permit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workresidentpermit.workresidencepermit')),
            ],
            options={
                'verbose_name': 'Permit',
            },
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('created', models.DateTimeField(blank=True, default=base_module.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=base_module.utils.get_utcnow)),
                ('user_created', base_module.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', base_module.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', base_module.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('id', base_module.model_fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('child_first_name', models.CharField(max_length=150)),
                ('child_last_name', models.CharField(max_length=150)),
                ('child_age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)),
                ('is_applying_residence', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('work_resident_permit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workresidentpermit.workresidencepermit')),
            ],
            options={
                'verbose_name': 'Child',
            },
        ),
    ]
