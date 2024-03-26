# Generated by Django 2.2.9 on 2019-12-23 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("phones", "0003_session_initiating_participant_sid"),
    ]

    operations = [
        migrations.AddField(
            model_name="session",
            name="status",
            field=models.CharField(default="", max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="session",
            name="initiating_participant_sid",
            field=models.CharField(max_length=34),
        ),
    ]
