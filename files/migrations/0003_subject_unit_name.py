# Generated by Django 3.2.14 on 2023-07-16 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_auto_20230716_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='unit_name',
            field=models.CharField(default=100, max_length=100),
            preserve_default=False,
        ),
    ]