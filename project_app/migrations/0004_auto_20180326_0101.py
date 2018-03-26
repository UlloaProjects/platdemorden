# Generated by Django 2.0.3 on 2018-03-26 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0003_auto_20180326_0054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='dma',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='ses',
        ),
        migrations.AlterField(
            model_name='demanda',
            name='demanda_diaria',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
        migrations.AlterField(
            model_name='demanda',
            name='demanda_promedio',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
        migrations.AlterField(
            model_name='ses',
            name='alpha',
            field=models.DecimalField(decimal_places=1, max_digits=20),
        ),
    ]
