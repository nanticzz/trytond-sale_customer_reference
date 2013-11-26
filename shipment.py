#This file is part of the sale_customer_reference module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.model import fields
from trytond.pyson import Eval, Not, Equal
from trytond.pool import PoolMeta

__all__ = ['ShipmentOut', 'ShipmentOutReturn']
__metaclass__ = PoolMeta


class ShipmentOut:
    __name__ = 'stock.shipment.out'
    customer_reference = fields.Char("Customer Reference", select=True,
        states={
            'readonly': Not(Equal(Eval('state'), 'draft')),
            }, depends=['state'])


class ShipmentOutReturn:
    __name__ = 'stock.shipment.out.return'
    customer_reference = fields.Char("Customer Reference", select=True,
        states={
            'readonly': Not(Equal(Eval('state'), 'draft')),
            }, depends=['state'])
