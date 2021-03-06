# Generated by Django 3.0.2 on 2020-04-20 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_name', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=1000)),
                ('release_date', models.DateField()),
                ('rating', models.IntegerField()),
                ('img_name', models.CharField(max_length=100)),
            ],
        ),
    ]
