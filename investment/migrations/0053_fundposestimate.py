# Generated by Django 3.1.5 on 2021-02-02 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0052_auto_20210128_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='FundPosEstimate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('normal_stock', models.DecimalField(decimal_places=4, default=0, max_digits=6, verbose_name='普通股票型')),
                ('mix_stock', models.DecimalField(decimal_places=4, default=0, max_digits=6, verbose_name='偏股混合型')),
                ('mix_equal', models.DecimalField(decimal_places=4, default=0, max_digits=6, verbose_name='平衡混合型')),
                ('mix_flexible', models.DecimalField(decimal_places=4, default=0, max_digits=6, verbose_name='灵活配置型')),
                ('date', models.DateField(verbose_name='估算日期')),
                ('secucode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='investment.funds', verbose_name='基金代码')),
            ],
            options={
                'verbose_name': '基金仓位估算',
                'verbose_name_plural': '基金仓位估算',
                'db_table': 'sma_fund_pos',
            },
        ),
    ]