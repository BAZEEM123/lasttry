# Generated by Django 5.0.4 on 2024-04-12 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythapp', '0002_team_name_alter_team_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='desc',
            field=models.TextField(default='0'),
            preserve_default=False,
        ),
    ]
