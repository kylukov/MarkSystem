# Generated by Django 3.1.7 on 2021-03-09 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210228_0133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mapping',
            old_name='category_id',
            new_name='categoryId',
        ),
        migrations.RenameField(
            model_name='mapping',
            old_name='mapping_type',
            new_name='mappingType',
        ),
        migrations.RenameField(
            model_name='mapping',
            old_name='market_sku',
            new_name='marketSku',
        ),
        migrations.RenameField(
            model_name='mapping',
            old_name='model_id',
            new_name='modelId',
        ),
        migrations.RenameField(
            model_name='offer',
            old_name='box_count',
            new_name='boxCount',
        ),
        migrations.RenameField(
            model_name='offer',
            old_name='delivery_duration_days',
            new_name='deliveryDurationDays',
        ),
        migrations.RenameField(
            model_name='offer',
            old_name='min_shipment',
            new_name='minShipment',
        ),
        migrations.RenameField(
            model_name='offer',
            old_name='quantum_of_supply',
            new_name='quantumOfSupply',
        ),
        migrations.RenameField(
            model_name='offer',
            old_name='shop_sku',
            new_name='shopSku',
        ),
        migrations.RenameField(
            model_name='offer',
            old_name='transport_unit_size',
            new_name='transportUnitSize',
        ),
        migrations.RenameField(
            model_name='offer',
            old_name='vendor_code',
            new_name='vendorCode',
        ),
        migrations.RenameField(
            model_name='processingstatenote',
            old_name='note_type',
            new_name='noteType',
        ),
        migrations.RenameField(
            model_name='processingstatenote',
            old_name='processing_state',
            new_name='processingState',
        ),
        migrations.RenameField(
            model_name='supplyscheduledays',
            old_name='supply_schedule_day',
            new_name='supplyScheduleDay',
        ),
        migrations.RenameField(
            model_name='timing',
            old_name='time_period',
            new_name='timePeriod',
        ),
        migrations.RenameField(
            model_name='timing',
            old_name='time_unit',
            new_name='timeUnit',
        ),
        migrations.RenameField(
            model_name='timing',
            old_name='timing_type',
            new_name='timingType',
        ),
        migrations.AlterField(
            model_name='customscommoditycode',
            name='offer',
            field=models.ForeignKey(help_text='Список кодов товара в единой Товарной номенклатуре внешнеэкономической деятельности (ТН ВЭД), если товар подлежит особому учету (например, в системе "Меркурий" как продукция животного происхождения или в системе "Честный ЗНАК"). Может содержать только один вложенный код ТН ВЭД.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customsCommodityCodes', to='main.offer', verbose_name='Список кодов товара в единой ТН ВЭД'),
        ),
        migrations.AlterField(
            model_name='manufacturercountry',
            name='offer',
            field=models.ForeignKey(help_text='Содержит от одной до 5 стран', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manufacturerCountries', to='main.offer', verbose_name='Список стран, в которых произведен товар'),
        ),
        migrations.AlterField(
            model_name='processingstate',
            name='offer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='processingState', to='main.offer', verbose_name='История статусов публикации товара на Маркете'),
        ),
        migrations.AlterField(
            model_name='supplyscheduledays',
            name='offer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supplyScheduleDays', to='main.offer', verbose_name='День недели, в который вы поставляете товары на склад'),
        ),
        migrations.AlterField(
            model_name='weightdimension',
            name='offer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='weightDimensions', to='main.offer', verbose_name='Габариты упаковки и вес товара'),
        ),
    ]
