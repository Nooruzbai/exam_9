# Generated by Django 4.0.3 on 2022-04-02 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='token',
            field=models.UUIDField(blank=True, null=True, verbose_name='token'),
        ),
    ]
