# Generated by Django 4.2.5 on 2023-09-23 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0006_client_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientmailing',
            name='users',
        ),
    ]
