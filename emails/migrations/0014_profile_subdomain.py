# Generated by Django 2.2.13 on 2021-03-16 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("emails", "0013_auto_20210113_1538"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="subdomain",
            field=models.CharField(
                blank=True, db_index=True, max_length=12, null=True, unique=True
            ),
        ),
    ]
