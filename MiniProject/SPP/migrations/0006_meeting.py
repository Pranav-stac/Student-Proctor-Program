# Generated by Django 5.0.1 on 2024-02-19 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SPP', '0005_announcement_delete_announcements_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('reason', models.TextField()),
            ],
        ),
    ]
