# Generated by Django 3.1.5 on 2021-01-28 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0051_fundassociate_define'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioassetallocate',
            name='alter',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=18, verbose_name='另类'),
        ),
        migrations.AlterField(
            model_name='portfolioassetallocate',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='日期'),
        ),
        migrations.AlterField(
            model_name='portfolioassetallocate',
            name='equity',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=18, verbose_name='权益'),
        ),
        migrations.AlterField(
            model_name='portfolioassetallocate',
            name='fix_income',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=18, verbose_name='固收'),
        ),
        migrations.AlterField(
            model_name='portfolioassetallocate',
            name='money',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=18, verbose_name='货币'),
        ),
    ]