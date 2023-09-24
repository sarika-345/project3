# Generated by Django 4.2.3 on 2023-07-19 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='film/img')),
                ('title', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=30)),
                ('date', models.IntegerField()),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
