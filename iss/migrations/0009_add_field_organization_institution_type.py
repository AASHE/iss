# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-10 16:19


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iss', '0008_add_new_org_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='institution_type',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
