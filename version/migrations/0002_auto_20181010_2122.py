# Generated by Django 2.1 on 2018-10-10 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('version', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='summary',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
