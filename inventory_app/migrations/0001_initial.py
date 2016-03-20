# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('total', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='images', null=True, blank=True)),
                ('description', models.TextField()),
                ('category', models.ForeignKey(to='inventory_app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Outlet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='outlets',
            field=models.ManyToManyField(to='inventory_app.Outlet'),
        ),
    ]
