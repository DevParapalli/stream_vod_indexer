# Generated by Django 3.1.2 on 2021-02-15 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameStorage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(max_length=200)),
                ('game_slug', models.CharField(max_length=200)),
                ('game_steam_id', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='StreamStorage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('date_of_stream', models.DateField()),
                ('stream_title', models.CharField(max_length=200)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.gamestorage')),
            ],
        ),
    ]
