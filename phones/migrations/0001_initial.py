# Generated by Django 2.2.9 on 2019-12-22 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Session",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("twilio_sid", models.CharField(max_length=34, unique=True)),
                ("initiating_proxy_number", models.CharField(max_length=20)),
            ],
        ),
    ]
