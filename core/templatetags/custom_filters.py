from django import template

register = template.Library()


@register.filter
def calc_sale_price(price, sale_percentage):
    if sale_percentage is not None:
        return price - (price * (sale_percentage / 100))
    return price
