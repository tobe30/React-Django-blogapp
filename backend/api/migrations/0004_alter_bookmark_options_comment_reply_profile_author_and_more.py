# Generated by Django 4.2 on 2024-03-22 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_post_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookmark',
            options={'verbose_name_plural': 'Bookmark'},
        ),
        migrations.AddField(
            model_name='comment',
            name='reply',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='author',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='notification',
            name='type',
            field=models.CharField(choices=[('Like', 'Like'), ('Comment', 'Comment'), ('Bookmark', 'Bookmark')], max_length=100),
        ),
    ]
