# Generated by Django 4.2.10 on 2024-03-10 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_options_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='field_2',
            field=models.CharField(default='42'),
        ),
        migrations.AddField(
            model_name='post',
            name='field_3',
            field=models.CharField(null=True),
        ),
    ]
