# Generated by Django 4.0.3 on 2022-04-04 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("gqlauth", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userstatus",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="status",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
