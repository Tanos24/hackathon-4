# Generated by Django 2.2.12 on 2021-09-25 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('messages', models.CharField(max_length=1000)),
            ],
        ),
    ]