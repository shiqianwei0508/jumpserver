# Generated by Django 3.1.14 on 2022-04-26 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0095_auto_20220407_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlatformProtocol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Name')),
                ('port', models.IntegerField(verbose_name='Port')),
                ('setting', models.JSONField(default=dict, verbose_name='Setting')),
                ('platform', models.ForeignKey(on_delete=models.deletion.CASCADE, related_name='protocols', to='assets.platform'),),
            ],
        ),
        migrations.CreateModel(
            name='PlatformAutomation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ping_enabled', models.BooleanField(default=False, verbose_name='Ping enabled')),
                ('ping_method', models.CharField(blank=True, max_length=32, null=True, verbose_name='Ping method')),
                ('gather_facts_enabled', models.BooleanField(default=False, verbose_name='Gather facts enabled')),
                ('gather_facts_method', models.TextField(blank=True, max_length=32, null=True, verbose_name='Gather facts method')),
                ('create_account_enabled', models.BooleanField(default=False, verbose_name='Create account enabled')),
                ('create_account_method', models.TextField(blank=True, max_length=32, null=True, verbose_name='Create account method')),
                ('change_password_enabled', models.BooleanField(default=False, verbose_name='Change password enabled')),
                ('change_password_method', models.TextField(blank=True, max_length=32, null=True, verbose_name='Change password method')),
                ('verify_account_enabled', models.BooleanField(default=False, verbose_name='Verify account enabled')),
                ('verify_account_method', models.TextField(blank=True, max_length=32, null=True, verbose_name='Verify account method')),
                ('gather_accounts_enabled', models.BooleanField(default=False, verbose_name='Gather facts enabled')),
                ('gather_accounts_method', models.TextField(blank=True, max_length=32, null=True, verbose_name='Gather facts method')),
            ],
        ),
        migrations.AddField(
            model_name='platform',
            name='automation',
            field=models.OneToOneField(blank=True, null=True, on_delete=models.deletion.CASCADE, related_name='platform', to='assets.platformautomation', verbose_name='Automation'),
        ),
    ]
