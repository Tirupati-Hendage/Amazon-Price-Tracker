# Generated by Django 3.1.1 on 2021-04-06 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('url', models.URLField()),
                ('current_price', models.FloatField(blank=True)),
                ('old_price', models.FloatField(default=0)),
                ('price_difference', models.FloatField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('price_difference', '-created'),
            },
        ),
    ]
