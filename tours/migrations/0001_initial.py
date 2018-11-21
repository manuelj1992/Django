# Generated by Django 2.0.1 on 2018-11-21 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('devices', '0004_auto_20181121_0420'),
    ]

    operations = [
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('position', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField()),
                ('client_app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tours', to='devices.ClientApp')),
            ],
        ),
        migrations.AddField(
            model_name='step',
            name='tour_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='tours.Tour'),
        ),
    ]
