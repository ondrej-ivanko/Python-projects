# Generated by Django 2.2.2 on 2019-06-21 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clean_slate', '0002_mock'),
    ]

    operations = [
        migrations.AddField(
            model_name='mock',
            name='tiny',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='mock',
            name='url',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
