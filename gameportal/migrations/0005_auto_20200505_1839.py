# Generated by Django 3.0.2 on 2020-05-05 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameportal', '0004_delete_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='img_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='url_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
