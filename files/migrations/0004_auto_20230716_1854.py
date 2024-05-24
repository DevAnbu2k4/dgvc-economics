# Generated by Django 3.2.14 on 2023-07-16 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0003_subject_unit_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='pdf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('text', models.FileField(upload_to='media')),
            ],
        ),
        migrations.RemoveField(
            model_name='subject',
            name='unit_name',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='files',
        ),
        migrations.AddField(
            model_name='subject',
            name='files',
            field=models.ManyToManyField(to='files.pdf'),
        ),
    ]