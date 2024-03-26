# Generated by Django 3.2.16 on 2022-12-22 16:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("phones", "0026_inboundcontact_add_last_call_and_text_dates"),
    ]

    operations = [
        migrations.CreateModel(
            name="TwilioMessagingService",
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
                (
                    "service_id",
                    models.CharField(
                        help_text="Service ID, starts with MG",
                        max_length=40,
                        unique=True,
                    ),
                ),
                (
                    "friendly_name",
                    models.CharField(
                        help_text="Friendly name of service", max_length=64
                    ),
                ),
                (
                    "use_case",
                    models.CharField(
                        help_text="The Service usecase, such as notifications",
                        max_length=40,
                    ),
                ),
                (
                    "campaign_use_case",
                    models.CharField(
                        help_text="The US A2P use case code, such as PROXY",
                        max_length=40,
                    ),
                ),
                (
                    "campaign_status",
                    models.CharField(
                        help_text="The US A2P campaign status, such as IN_PROGRESS, PENDING, VERIFIED, or FAILED",
                        max_length=15,
                    ),
                ),
                (
                    "channel",
                    models.CharField(
                        default="unknown",
                        help_text="Which Relay channel uses this service?",
                        max_length=40,
                    ),
                ),
                (
                    "spam",
                    models.BooleanField(
                        default=False,
                        help_text="Service has been identifed as sending spam",
                    ),
                ),
                (
                    "full",
                    models.BooleanField(
                        default=False,
                        help_text="Service is at limit of associated phones",
                    ),
                ),
                (
                    "current",
                    models.BooleanField(
                        default=False,
                        help_text="New numbers should be assigned to this service",
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        help_text="Creation time in Twilio",
                    ),
                ),
                (
                    "date_updated",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        help_text="Update time in Twilio",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="relaynumber",
            name="service",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="phones.twiliomessagingservice",
            ),
        ),
    ]
