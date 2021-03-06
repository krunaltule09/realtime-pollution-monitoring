# Generated by Django 2.2.2 on 2019-12-26 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gasdb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=4)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='phdb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=4)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='sounddb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=4)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
