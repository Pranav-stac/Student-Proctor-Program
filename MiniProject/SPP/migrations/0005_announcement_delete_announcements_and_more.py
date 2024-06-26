# Generated by Django 5.0.1 on 2024-02-19 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SPP', '0004_announcements'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='announcements',
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
