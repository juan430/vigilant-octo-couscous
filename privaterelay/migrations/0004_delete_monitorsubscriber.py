# Generated by Django 2.2.13 on 2021-03-18 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('privaterelay', '0003_remove_invitations'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MonitorSubscriber',
        ),
    ]
