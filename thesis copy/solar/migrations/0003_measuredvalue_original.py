# Generated by Django 4.0.1 on 2022-02-10 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solar', '0002_alter_measuredvalue_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='measuredvalue',
            name='Original',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
