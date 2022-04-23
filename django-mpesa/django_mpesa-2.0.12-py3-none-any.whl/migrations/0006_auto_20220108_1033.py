# Generated by Django 2.2.20 on 2022-01-08 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('mpesa', '0005_auto_20200822_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymenttransaction',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='paymenttransaction',
            name='object_id',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='paymenttransaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=14),
        ),
    ]
