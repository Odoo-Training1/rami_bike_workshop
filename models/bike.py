from odoo import models, fields


class Bike(models.Model):
    _name = 'bike.workshop.bike'
    _description = 'Bike Workshop'

    name = fields.Char(string='Bike Name / Code', required=True)
    brand = fields.Char(string='Brand')
    bike_type = fields.Selection([
        ('road', 'Road'),
        ('mountain', 'Mountain'),
        ('city', 'City'),
        ('electric', 'Electric'),
    ], string='Bike Type')
    purchase_date = fields.Date(string='Purchase Date')
    last_maintenance_date = fields.Date(string='Last Maintenance Date')
    daily_rental_price = fields.Float(string='Daily Rental Price')
    wheel_size = fields.Float(string='Wheel Size (inches)')

   
