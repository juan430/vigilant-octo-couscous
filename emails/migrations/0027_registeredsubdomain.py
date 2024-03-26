# Generated by Django 2.2.24 on 2021-10-15 05:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("emails", "0026_make_smallint_fields_full_integer_fields"),
    ]

    operations = [
        migrations.CreateModel(
            name="RegisteredSubdomain",
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
                    "subdomain_hash",
                    models.CharField(db_index=True, max_length=64, unique=True),
                ),
                ("registered_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
