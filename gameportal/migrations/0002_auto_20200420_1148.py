# Generated by Django 3.0.2 on 2020-04-20 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gameportal', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Games',
            new_name='Game',
        ),
    ]