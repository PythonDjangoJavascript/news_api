# Generated by Django 3.2.1 on 2021-05-05 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_rename_descirption_airticle_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='airticle',
            old_name='loacation',
            new_name='location',
        ),
    ]
