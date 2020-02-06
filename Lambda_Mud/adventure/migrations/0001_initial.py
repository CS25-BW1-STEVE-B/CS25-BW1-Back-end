# Generated by Django 3.0.3 on 2020-02-05 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=128)),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventure.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=128)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventure.Item')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventure.Player')),
            ],
        ),
    ]
