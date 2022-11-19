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
                ('precio', models.FloatField(help_text='Precio del producto', null=False)),
                ('stock', models.IntegerField(help_text='Stock del prodcuto', null=False)),
                ('tipo', models.IntegerField(choices=Producto.TipoProducto.choices, 
                    default=Producto.TipoProducto.JUEGO, null=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, null=False)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameDockApp.Producto', null=False)),
                ('cantidad', models.IntegerField(help_text="Cantidad del producto comprado", null=False)),
                ('completado', models.BooleanField(null=False)),
            ],
        ),
    ]