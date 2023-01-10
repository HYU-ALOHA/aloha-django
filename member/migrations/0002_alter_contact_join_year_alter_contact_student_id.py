# Generated by Django 4.1.5 on 2023-01-10 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("member", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="join_year",
            field=models.IntegerField(db_index=True, verbose_name="기수"),
        ),
        migrations.AlterField(
            model_name="contact",
            name="student_id",
            field=models.CharField(db_index=True, max_length=20),
        ),
    ]