# Generated by Django 3.1.7 on 2021-03-09 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='processingstatenote',
            old_name='noteType',
            new_name='type',
        ),
        migrations.AlterField(
            model_name='timing',
            name='offer',
            field=models.ForeignKey(help_text='Срок годности, срок службы, гарантийный срок', null=True,
                                    on_delete=django.db.models.deletion.CASCADE, related_name='timings',
                                    to='main.offer', verbose_name='Тайминги товара'),
        ),
        migrations.AlterField(
            model_name='processingstate',
            name='offer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='processingState_set', to='main.offer',
                                    verbose_name='История статусов публикации товара на Маркете'),
        ),
        migrations.AlterField(
            model_name='mapping',
            name='offer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mapping_set',
                                    to='main.offer', verbose_name='Привязки карточек на Я.Маркете'),
        ),
    ]
