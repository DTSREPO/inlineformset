# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 11:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='position',
            field=models.CharField(choices=[('1', 'ピッチャー'), ('2', 'キャッチャー'), ('3', 'ファースト'), ('4', 'セカンド'), ('5', 'サード'), ('6', 'ショート'), ('7', 'レフト'), ('8', 'センター'), ('9', 'ライト')], default='', max_length=1, verbose_name='守備位置'),
        ),
    ]
