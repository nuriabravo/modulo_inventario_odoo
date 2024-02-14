from odoo import models, fields

class Producto(models.Model):
    _name = 'inventario.producto'
    _description = 'Producto'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
    # Agrega otros campos necesarios para tu modelo de Producto

class Proveedor(models.Model):
    _name = 'inventario.proveedor'
    _description = 'Proveedor'

    name = fields.Char(string='Nombre', required=True)
    direccion = fields.Text(string='Dirección')
    telefono = fields.Char(string='Teléfono')

class PedidoCompra(models.Model):
    _name = 'inventario.compra'
    _description = 'Pedido de Compra'

    proveedor_id = fields.Many2one('inventario.proveedor', string='Proveedor', required=True)
    productos = fields.One2many('inventario.linea_compra', 'pedido_compra_id', string='Productos')

class PedidoCompraLinea(models.Model):
    _name = 'inventario.linea_compra'
    _description = 'Línea de Pedido de Compra'

    producto_id = fields.Many2one('inventario.producto', string='Producto', required=True)
    cantidad = fields.Integer(string='Cantidad')
    precio_unitario = fields.Float(string='Precio Unitario', digits=(10, 2))
    pedido_compra_id = fields.Many2one('inventario.compra', string='Pedido de Compra')

class PedidoVenta(models.Model):
    _name = 'inventario.venta'
    _description = 'Pedido de Venta'

    cliente_id = fields.Many2one('inventario.cliente', string='Cliente', required=True)
    productos = fields.One2many('inventario.linea_venta', 'pedido_venta_id', string='Productos')

class PedidoVentaLinea(models.Model):
    _name = 'inventario.linea_venta'
    _description = 'Línea de Pedido de Venta'

    producto_id = fields.Many2one('inventario.producto', string='Producto', required=True)
    cantidad = fields.Integer(string='Cantidad')
    precio_unitario = fields.Float(string='Precio Unitario', digits=(10, 2))
    pedido_venta_id = fields.Many2one('inventario.venta', string='Pedido de Venta')

class Cliente(models.Model):
    _name = 'inventario.cliente'
    _description = 'Cliente'

    name = fields.Char(string='Nombre', required=True)
    direccion = fields.Text(string='Dirección')
    telefono = fields.Char(string='Teléfono')
    pedidos_venta_ids = fields.One2many('inventario.venta', 'cliente_id', string='Pedidos de Venta')
