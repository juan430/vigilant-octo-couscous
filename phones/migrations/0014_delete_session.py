# Generated by Django 3.2.13 on 2022-07-08 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("phones", "0013_relaynumber_vcard_lookup_key"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Session",
        ),
    ]
