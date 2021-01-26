# Generated by Django 3.1.5 on 2021-01-25 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0048_capitalflow'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioAssetAllocate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equity', models.DecimalField(decimal_places=2, default=0, max_digits=18, verbose_name='quanyi')),
                ('fix_income', models.DecimalField(decimal_places=2, default=0, max_digits=18, verbose_name='gushou')),
                ('alter', models.DecimalField(decimal_places=2, default=0, max_digits=18, verbose_name='gushou')),
                ('money', models.DecimalField(decimal_places=2, default=0, max_digits=18, verbose_name='huobi')),
                ('date', models.DateField(blank=True, null=True, verbose_name='申购开放日')),
                ('port_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='investment.portfolio', to_field='port_code', verbose_name='组合代码')),
            ],
            options={
                'verbose_name': '组合资产配置',
                'verbose_name_plural': '组合资产配置',
                'db_table': 'sma_portfolio_allocate',
                'get_latest_by': 'date',
            },
        ),
    ]