# Generated by Django 3.1.2 on 2020-12-07 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0035_stockdailyquote'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='indexcomponent',
            unique_together=set(),
        ),
    ]