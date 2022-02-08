# Generated by Django 4.0.1 on 2022-02-08 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tweetcommant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='tweetmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_id', models.CharField(max_length=9)),
                ('url', models.CharField(max_length=45)),
                ('tag', models.CharField(max_length=43)),
                ('title', models.CharField(max_length=100)),
                ('des', models.CharField(max_length=200)),
                ('ing', models.CharField(max_length=200)),
                ('img_src', models.CharField(max_length=100)),
            ],
        ),
    ]