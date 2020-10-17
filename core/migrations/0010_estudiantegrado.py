# Generated by Django 3.1.1 on 2020-10-17 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_docentemateria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiantegrado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.estudiante')),
                ('grado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.grado')),
            ],
            options={
                'verbose_name': 'estudiantegrado',
                'verbose_name_plural': 'estudiantegrados',
                'db_table': 'estudiantegrado',
            },
        ),
    ]
