from pay_module import cart


def cart_item_count(request):
    item_count = cart.item_count(request)
    return {'cart_item_count' : item_count }