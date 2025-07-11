# Generated by Django 5.2.4 on 2025-07-07 09:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='eval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=100)),
                ('explain', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='star',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('pi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='star', to='eval.eval')),
            ],
        ),
    ]
