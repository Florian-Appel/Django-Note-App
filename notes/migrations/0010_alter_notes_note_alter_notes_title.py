# Generated by Django 4.1.5 on 2023-01-15 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0009_remove_category_created_at_remove_notes_category_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notes",
            name="note",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="notes",
            name="title",
            field=models.CharField(max_length=30),
        ),
    ]
