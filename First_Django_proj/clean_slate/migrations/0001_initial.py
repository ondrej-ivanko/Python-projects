# Generated by Django 2.2.2 on 2019-06-21 08:27

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('individual', 'individual'), ('collective', 'collective')], help_text='collective or individual', max_length=15)),
            ],
            managers=[
                ('sports', django.db.models.manager.Manager()),
            ],
        ),
    ]
