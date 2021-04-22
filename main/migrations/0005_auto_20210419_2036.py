# Generated by Django 3.1.7 on 2021-04-19 17:36

from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210418_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hiding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тип сообщения о скрытии вашего предложения')),
                ('code', models.CharField(blank=True, max_length=255, null=True, verbose_name='Код сообщения о скрытии вашего предложения')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Сообщение о скрытии вашего предложения')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий к сообщению о скрытии вашего предложения')),
            ],
        ),
        migrations.CreateModel(
            name='Inclusion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('FREE_EXPIRE', 'Товар,  у которого срок бесплатного хранения подходит к концу. Значение возвращается для товаров с типом условий хранения и обработки FREE'), ('PAID_EXPIRE', 'Товар, за хранение которого скоро придется платить по повышенному тарифу. Значение возвращается для товаров с типом условий хранения и обработки PAID'), ('PAID_EXTRA', 'Товар, который хранится платно по повышенному тарифу. Значение возвращается для товаров с типом условий хранения и обработки PAID')], max_length=11, null=True, verbose_name='Тип условий хранения и обработки товара на складе')),
                ('count', models.BigIntegerField(null=True, verbose_name='Количество товара для указанного типа условий хранения и обработки товара на складе')),
            ],
        ),
        migrations.CreateModel(
            name='OfferReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopSku', models.CharField(max_length=255, null=True, verbose_name='Ваш SKU')),
                ('marketSku', models.PositiveSmallIntegerField(null=True, verbose_name='SKU на Яндексе — идентификатор текущей карточки товара на Маркете')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Название товара')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена на товар, выставленная партнером')),
                ('categoryId', models.BigIntegerField(blank=True, null=True, verbose_name='Идентификатор категории товара на Маркете')),
                ('categoryName', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название категории товара на Маркете')),
                ('offer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='report', to='main.offer')),
                ('warehouses', models.ManyToManyField(to='main.Warehouse', verbose_name='Информация о складах, на которых хранится товар')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('AVAILABLE', 'Товар, доступный для продажи'), ('DEFECT', 'Товар с браком'), ('EXPIRED', 'Товар с истекшим сроком годности'), ('FIT', 'Товар, который доступен для продажи или уже зарезервирован'), ('FREEZE', 'Товар, который зарезервирован для заказов'), ('QUARANTINE', 'Товар, временно недоступный для продажи (например, товар перемещают из одного помещения склада в другое) '), ('UTILIZATION', 'Товар, который будет утилизирован'), ('SUGGEST', 'Товар, который рекомендуется поставить на склад (могут заказать в ближайшие две недели)'), ('TRANSIT', 'Проданный товар')], max_length=11, null=True, verbose_name='Тип остатков товаров на складе')),
                ('count', models.BigIntegerField(null=True, verbose_name='Количество товара для указанного типа остатков на складе')),
                ('offer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='main.offer', verbose_name='Информация об остатках товара на складах.')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='main.warehouse', verbose_name='Информация об остатках товаров на складе.')),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('FREE', 'Товар, который хранится на складе бесплатно'), ('PAID', 'Товар, который хранится платно по обычному тарифу')], max_length=4, null=True, verbose_name='Тип условий хранения и обработки товара на складе')),
                ('count', models.BigIntegerField(null=True, verbose_name='Количество товара для указанного типа условий хранения и обработки товара на складе')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='storage', to='main.offerreport', verbose_name='Информация об условиях хранения и обработки товара на складе.')),
            ],
        ),
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('AGENCY_COMMISSION', 'Прием и перечисление денег от покупателя (агентское вознаграждение)'), ('FULFILLMENT', 'Обработка товара на складе Маркета'), ('STORAGE', 'Хранение товара на складе Маркета в течение суток'), ('SURPLUS', 'Хранение излишков на складе Маркета'), ('WITHDRAW', 'Вывоз товара со склада Маркета'), ('FEE', 'Размещение товара на Маркете')], max_length=17, null=True, verbose_name='Тип остатков товаров на складе')),
                ('percent', models.FloatField(blank=True, null=True, verbose_name='Значение тарифа в процентах')),
                ('amount', models.FloatField(blank=True, null=True, verbose_name='Значение тарифа в рублях')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tariffs', to='main.offerreport', verbose_name='Информация о тарифах, по которым нужно заплатить за услуги Маркета.')),
            ],
        ),
        migrations.DeleteModel(
            name='Sku',
        ),
        migrations.AddField(
            model_name='price',
            name='currencyId',
            field=models.CharField(choices=[('RUR', 'Российский рубль')], max_length=3, null=True, verbose_name='Валюта, в которой указана цена на товар.'),
        ),
        migrations.AlterField(
            model_name='item',
            name='warehouse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='offers', to='main.warehouse', verbose_name='Информация о складе, на котором хранится товар'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='base/base.png', upload_to=main.models.get_path, verbose_name='аватарка'),
        ),
        migrations.AddField(
            model_name='inclusion',
            name='storage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inclusions', to='main.storage', verbose_name='Дополнительная информация о том, для скольких товаров заканчивается срок действия текущего тарифа и для скольких товаров действует повышенный тариф.'),
        ),
        migrations.AddField(
            model_name='hiding',
            name='report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hidings', to='main.offerreport', verbose_name='Информация о скрытии вашего предложения на Маркете. Если ваше предложение не скрыто, параметр не будет возвращаться.'),
        ),
    ]
