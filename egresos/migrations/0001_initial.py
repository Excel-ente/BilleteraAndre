# Generated by Django 4.2 on 2023-05-01 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('configuracion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GastoFijo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True, verbose_name='Activo')),
                ('detalle', models.CharField(max_length=255)),
                ('fecha_primer_pago', models.DateField()),
                ('cuotas', models.IntegerField(default=1)),
                ('valor_cuota', models.DecimalField(decimal_places=2, max_digits=11)),
                ('cuotas_pagas', models.IntegerField(default=0)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='configuracion.tipogasto')),
            ],
        ),
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('detalle', models.CharField(max_length=255)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=11)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='configuracion.tipogasto')),
            ],
        ),
    ]
