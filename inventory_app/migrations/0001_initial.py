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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('amount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('total', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('description', models.TextField()),
                ('category', models.ForeignKey(to='inventory_app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Outlet',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='outlets',
            field=models.ManyToManyField(to='inventory_app.Outlet', through='inventory_app.Count'),
        ),
        migrations.AddField(
            model_name='count',
            name='item',
            field=models.ForeignKey(to='inventory_app.Item'),
        ),
        migrations.AddField(
            model_name='count',
            name='outlet',
            field=models.ForeignKey(to='inventory_app.Outlet'),
        ),
    ]
