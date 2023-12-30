# Generated by Django 5.0 on 2023-12-30 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_transmission', '0004_video_video_process_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_process_status',
            field=models.CharField(choices=[('to_process', "To process'"), ('processing', 'Processing'), ('processed', 'Processed'), ('processed_failed', 'Failed process')], default='to_process', max_length=20, verbose_name='Video status'),
        ),
    ]