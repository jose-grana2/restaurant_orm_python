from producto import Producto, Session, engine, Base
from pedido import Pedido, PedidoProducto
from descuento import aplicar_descuento
from factura import generar_factura
from api import consultar_pedido
from reporte import generar_reporte

# 🔹 Crear todas las tablas después de haber importado los modelos
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base.metadata.create_all(engine)

def main():
    session = Session()
    
    #Crear productos
    producto1 = Producto(nombre="Iphone 16", tipo="Smartphne", precio=900, disponible=True)
    producto2 = Producto(nombre="Google Pixel 7", tipo="Smartphne", precio=650, disponible=True)
    producto3 = Producto(nombre="Samsung Galaxy A13", tipo="Smartphne", precio=150, disponible=False)

    session.add_all([producto1, producto2, producto3])
    session.commit()

    #Crear pedidos
    pedido1 = Pedido(cliente="Jose G")
    session.add(pedido1)
    session.commit()

    #Agregar productos al pedido
    pedidoproducto1 = PedidoProducto(
        pedido_id=pedido1.id, producto_id=producto1.id, cantidad=3
    )
    pedidoproducto2 = PedidoProducto(
        pedido_id=pedido1.id, producto_id=producto2.id, cantidad=2
    )
    pedidoproducto3 = PedidoProducto(
        pedido_id=pedido1.id, producto_id=producto1.id, cantidad=3
    )
    session.add_all([pedidoproducto1, pedidoproducto2, pedidoproducto3])
    pedido1.calcularTotal()
    session.commit()
    
    #Aplicar descuento
    aplicar_descuento(pedido1, 10)
    session.commit()

    #Generar factura
    print(generar_factura(pedido1))

    #Consultar pedido via API
    print(consultar_pedido('Jose G'))

    #Generar reporte PDF
    generar_reporte('reporte_pedidos.pdf')
    print('Reporte generado...')

if __name__ == '__main__':
    main()