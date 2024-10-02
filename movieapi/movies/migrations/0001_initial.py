# Generated by Django 5.0.7 on 2024-10-01 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('imdb_id', models.CharField(max_length=15, unique=True)),
                ('year', models.CharField(max_length=4)),
                ('poster_url', models.URLField(blank=True, max_length=500, null=True)),
                ('overview', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
