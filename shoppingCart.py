def shoppingCart(requests):

    cart = {}
    for req in requests:

        action, item, qty, *_ = *req.split(' : '), None, None

        if action == 'checkout':
            cart.clear()
        elif action == 'add':
            cart[item] = 1
        elif action == 'remove':
            del cart[item]
        elif action == 'quantity_upd':
            cart[item] += eval(qty)
    
    output = [f'{k} : {v}' for k, v in cart.items()]
    return output