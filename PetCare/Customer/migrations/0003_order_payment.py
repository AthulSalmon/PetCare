# Generated by Django 5.1.5 on 2025-01-25 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
