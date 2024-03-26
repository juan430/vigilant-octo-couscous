# Generated by Django 3.2.15 on 2022-08-15 17:42

from django.db import migrations, models


def add_db_default_forward_func(apps, schema_editor):
    """
    Add a database default of TRUE for enabled, for PostgreSQL and SQLite3

    Using `./manage.py sqlmigrate` for the SQL, and the technique from:
    https://stackoverflow.com/a/45232678/10612
    """
    if schema_editor.connection.vendor.startswith("postgres"):
        schema_editor.execute(
            'ALTER TABLE "phones_inboundcontact"'
            " ALTER COLUMN \"last_inbound_type\" SET DEFAULT 'text';"
        )
    elif schema_editor.connection.vendor.startswith("sqlite"):
        schema_editor.execute(
            'CREATE TABLE IF NOT EXISTS "new__phones_inboundcontact" '
            ' ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,'
            '  "inbound_number" varchar(15) NOT NULL,'
            '  "last_inbound_date" datetime NOT NULL,'
            "  \"last_inbound_type\" varchar(4) NOT NULL DEFAULT 'text',"
            '  "num_calls" integer unsigned NOT NULL CHECK ("num_calls" >= 0),'
            '  "num_calls_blocked" integer unsigned NOT NULL CHECK ("num_calls_blocked" >= 0),'
            '  "num_texts" integer unsigned NOT NULL CHECK ("num_texts" >= 0),'
            '  "num_texts_blocked" integer unsigned NOT NULL CHECK ("num_texts_blocked" >= 0),'
            '  "blocked" bool NOT NULL,'
            '  "relay_number_id" integer NOT NULL REFERENCES "phones_relaynumber" ("id")'
            "   DEFERRABLE INITIALLY DEFERRED);"
        )
        schema_editor.execute(
            'INSERT INTO "new__phones_inboundcontact"'
            ' ("id", "inbound_number", "last_inbound_date", "last_inbound_type", "num_calls", "num_calls_blocked", "num_texts", "num_texts_blocked", "blocked", "relay_number_id")'
            ' SELECT "id", "inbound_number", "last_inbound_date", "text", "num_calls", "num_calls_blocked", "num_texts", "num_texts_blocked", "blocked", "relay_number_id"'
            ' FROM "phones_inboundcontact";'
        )
        schema_editor.execute('DROP TABLE "phones_inboundcontact";')
        schema_editor.execute(
            'ALTER TABLE "new__phones_inboundcontact" RENAME TO "phones_inboundcontact";'
        )
        schema_editor.execute(
            'CREATE INDEX "phones_inboundcontact_relay_number_id_f95dbf8c" ON "phones_inboundcontact" ("relay_number_id");'
        )
        schema_editor.execute(
            'CREATE INDEX "phones_inbo_relay_n_eaf332_idx" ON "phones_inboundcontact" ("relay_number_id", "inbound_number");'
        )
    else:
        raise Exception(f'Unknown database vendor "{schema_editor.connection.vendor}"')


class Migration(migrations.Migration):

    dependencies = [
        ("phones", "0019_inboundcontact_phones_inbo_relay_n_eaf332_idx"),
    ]

    operations = [
        migrations.AddField(
            model_name="inboundcontact",
            name="last_inbound_type",
            field=models.CharField(
                choices=[("call", "call"), ("text", "text")],
                default="text",
                max_length=4,
            ),
        ),
        migrations.RunPython(
            code=add_db_default_forward_func,
            reverse_code=migrations.RunPython.noop,
            elidable=True,
        ),
    ]
