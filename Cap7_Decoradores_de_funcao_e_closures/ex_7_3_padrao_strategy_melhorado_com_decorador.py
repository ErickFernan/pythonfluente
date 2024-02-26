promos = []

def promotion(promo_func):
    promos.append(promo_func)
    return promo_func

@promotion
def fidelity(order):
    """5% de desconto para client4es com mil ou mains pontos nmo programa de fidelidade"""
    return order.total()* .05 if order.customer.fidelity >= 1000 else 0

@promotion
def bulk_item(order):
    """10% de desconto para cada LineItem com 20 ou mias unidades"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

@promotion
def large_order(order):
    """7% de desconto para pedidos com 10 ou mkais itens diferentes"""
    distincit_items = {item.product for item in order.cart}
    if len(distincit_items) >= 10:
        return order.total() * .07
    return 0

def best_promo(order):
    """Seleciona o melhor desconto disponível"""

    return max(promo(order) for promo in promos)
