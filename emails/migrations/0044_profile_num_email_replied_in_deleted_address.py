# Generated by Django 2.2.27 on 2022-05-05 22:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("emails", "0043_add_num_replied_field_on_addresses"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="num_email_replied_in_deleted_address",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
