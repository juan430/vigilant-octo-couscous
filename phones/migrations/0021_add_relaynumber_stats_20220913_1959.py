# Generated by Django 3.2.15 on 2022-09-13 19:59

from django.db import migrations, models


def add_db_default_forward_func(apps, schema_editor):
    """
    Add a database default of TRUE for enabled, for PostgreSQL and SQLite3

    Using `./manage.py sqlmigrate` for the SQL, and the technique from:
    https://stackoverflow.com/a/45232678/10612
    """
    if schema_editor.connection.vendor.startswith("postgres"):
        schema_editor.execute(
            'ALTER TABLE "phones_relaynumber"'
            ' ALTER COLUMN "remaining_minutes" SET DEFAULT 50,'
            ' ALTER COLUMN "remaining_texts" SET DEFAULT 75,'
            ' ALTER COLUMN "calls_forwarded" SET DEFAULT 0,'
            ' ALTER COLUMN "calls_blocked" SET DEFAULT 0,'
            ' ALTER COLUMN "texts_forwarded" SET DEFAULT 0,'
            ' ALTER COLUMN "texts_blocked" SET DEFAULT 0;'
        )
    elif schema_editor.connection.vendor.startswith("sqlite"):
        schema_editor.execute(
            'CREATE TABLE "new__phones_relaynumber"'
            ' ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,'
            ' "remaining_minutes" integer NOT NULL DEFAULT 50,'
            ' "remaining_texts" integer NOT NULL DEFAULT 75,'
            ' "calls_forwarded" integer NOT NULL DEFAULT 0,'
            ' "calls_blocked" integer NOT NULL DEFAULT 0,'
            ' "texts_forwarded" integer NOT NULL DEFAULT 0,'
            ' "texts_blocked" integer NOT NULL DEFAULT 0,'
            ' "enabled" bool NOT NULL DEFAULT 1,'
            ' "number" varchar(15) NOT NULL,'
            ' "location" varchar(255) NOT NULL,'
            ' "user_id" integer NOT NULL REFERENCES "auth_user" ("id")'
            " DEFERRABLE INITIALLY DEFERRED,"
            ' "vcard_lookup_key" varchar(6) NOT NULL UNIQUE);'
        )
        schema_editor.execute(
            'INSERT INTO "new__phones_relaynumber"'
            ' ("id", "number", "location", "user_id", "vcard_lookup_key", "enabled",'
            ' "remaining_texts", "remaining_minutes", "calls_forwarded", "calls_blocked", '
            ' "texts_forwarded", "texts_blocked") '
            ' SELECT "id", "number", "location", "user_id", "vcard_lookup_key", "enabled", '
            " 75, 50, 0, 0, 0, 0 "
            ' FROM "phones_relaynumber";'
        )
        schema_editor.execute('DROP TABLE "phones_relaynumber";')
        schema_editor.execute(
            'ALTER TABLE "new__phones_relaynumber" RENAME TO "phones_relaynumber";'
        )
        schema_editor.execute(
            'CREATE INDEX "phones_relaynumber_number_742e5d6b" ON "phones_relaynumber"'
            ' ("number");'
        )
        schema_editor.execute(
            'CREATE INDEX "phones_relaynumber_user_id_62c65ede" ON "phones_relaynumber"'
            ' ("user_id");'
        )
    else:
        raise Exception(f'Unknown database vendor "{schema_editor.connection.vendor}"')


class Migration(migrations.Migration):
    dependencies = [
        ("phones", "0020_inboundcontact_last_inbound_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="relaynumber",
            name="calls_blocked",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="relaynumber",
            name="calls_forwarded",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="relaynumber",
            name="remaining_minutes",
            field=models.IntegerField(default=50),
        ),
        migrations.AddField(
            model_name="relaynumber",
            name="remaining_texts",
            field=models.IntegerField(default=75),
        ),
        migrations.AddField(
            model_name="relaynumber",
            name="texts_blocked",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="relaynumber",
            name="texts_forwarded",
            field=models.IntegerField(default=0),
        ),
        migrations.RunPython(
            code=add_db_default_forward_func,
            reverse_code=migrations.RunPython.noop,
            elidable=True,
        ),
    ]
