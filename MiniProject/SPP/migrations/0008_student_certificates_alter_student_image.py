# Generated by Django 5.0.1 on 2024-03-28 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SPP', '0007_proctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='certificates',
            field=models.ImageField(blank=True, null=True, upload_to='certificates/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='student_images/'),
        ),
    ]
