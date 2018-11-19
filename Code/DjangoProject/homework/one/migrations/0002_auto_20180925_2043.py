# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-25 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postid', models.CharField(max_length=16, unique=True)),
                ('title', models.CharField(max_length=32)),
                ('image', models.CharField(max_length=32)),
                ('like_num', models.CharField(max_length=16)),
                ('request_url', models.CharField(max_length=16)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='u_file',
            field=models.ImageField(upload_to='%Y/%m/%d/'),
        ),
    ]