# Generated by Django 3.2.16 on 2023-04-11 19:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20230411_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor_card',
            name='holder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.customuser'),
            preserve_default=False,
        ),
    ]
