# Generated by Django 3.2.13 on 2022-07-11 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("phones", "0015_alter_realphone_verification_sent_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="relaynumber",
            name="number",
            field=models.CharField(db_index=True, max_length=15),
        ),
    ]
