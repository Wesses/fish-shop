# Generated by Django 3.0.4 on 2020-03-10 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('price', models.FloatField(null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('available', models.BooleanField(null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main_catalog.Order', verbose_name='Заказ')),
            ],
        ),
    ]
