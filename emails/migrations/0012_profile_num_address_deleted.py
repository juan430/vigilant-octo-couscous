# Generated by Django 2.2.13 on 2020-08-05 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("emails", "0011_profile_and_address_timestamps_20200710_1817"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="num_address_deleted",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
