# Generated by Django 3.1.4 on 2020-12-11 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0005_auto_20201211_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='calculator.quiz'),
        ),
    ]
