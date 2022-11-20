from django.db import migrations, models
from django.conf import settings
from gameDockApp.models import Producto
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL)
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField(help_text='Descripción del producto')),
                ('precio', models.FloatField(help_text='Precio del producto')),
                ('stock', models.IntegerField(help_text='Stock del prodcuto')),
                ('tipo', models.IntegerField(choices=Producto.TipoProducto.choices, 
                    default=Producto.TipoProducto.JUEGO, null=False)),
                ('imagen', models.ImageField(upload_to="productos", verbose_name="Imagen"))
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto_Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameDockApp.Pedido')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameDockApp.Producto')),
                ('cantidad', models.IntegerField(help_text="Cantidad del producto comprado")),
            ],
        ),
    ]