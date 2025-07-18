# Generated by Django 5.2.4 on 2025-07-17 16:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_alter_habitos_descripcion_alter_habitos_fecha_inicio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seguimientos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(null=True)),
                ('estado', models.CharField(max_length=200)),
                ('nota', models.CharField(max_length=200)),
                ('habito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.habitos')),
            ],
        ),
    ]
