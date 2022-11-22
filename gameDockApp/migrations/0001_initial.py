# Generated by Django 4.1.3 on 2022-11-21 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField(help_text='Descripción del producto')),
                ('precio', models.FloatField(help_text='Precio del producto')),
                ('stock', models.IntegerField(help_text='Stock del prodcuto')),
                ('tipo', models.IntegerField(choices=[(1, 'Juego'), (2, 'Consola'), (3, 'Periferico')], default=1)),
                ('imagen', models.ImageField(upload_to='productos', verbose_name='Productos')),
            ],
        ),
        migrations.CreateModel(
            name='Producto_Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(help_text='Cantidad del producto comprado')),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameDockApp.pedido')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameDockApp.producto')),
            ],
        ),
    ]
