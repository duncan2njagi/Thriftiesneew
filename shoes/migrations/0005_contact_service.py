# Generated by Django 2.1 on 2019-07-17 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0004_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('telephone', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('automation', models.CharField(max_length=255)),
                ('responses', models.CharField(max_length=255)),
            ],
        ),
    ]
