from django.shortcuts import render, redirect, reverse


def view_basket(request):
    """ renders the basket view page """
    return render(request, "basket.html")

def add_to_basket(request, id):
    """ Add a quantity of artifact to the basket """
    quantity=int(request.POST.get('quantity'))

    basket = request.session.get('basket', {})
    basket[id] = basket.get(id, quantity)

    request.session['basket'] = basket
    return redirect(reverse('index'))

def adjust_basket(request, id):
    """ adjust the artifact in the basket """
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('cart', {})

    if quantity > 0:
        basket[id] = quantity
    else:
        basket.pop(id)
    
    request.session['basket'] = basket
    return redirect(reverse('view_basket'))