# Generated by Django 2.2.2 on 2019-06-21 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clean_slate', '0003_auto_20190621_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='mock',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]