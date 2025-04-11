# Generated by Django 5.2 on 2025-04-07 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_category_part_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='part',
            name='location',
        ),
        migrations.AddField(
            model_name='part',
            name='aisle',
            field=models.CharField(default='Unknown', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='part',
            name='bin_number',
            field=models.CharField(default='Unknown', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='part',
            name='room',
            field=models.CharField(default='Unknown', max_length=50),
            preserve_default=False,
        ),
    ]
