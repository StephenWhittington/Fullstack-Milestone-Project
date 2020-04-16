from django.shortcuts import get_object_or_404
from artifacts.models import Artifact


def basket_contents(request):
    """
    makes sure that the basket contents are available when every page 
    is rendered

    """
    basket = request.session.get('basket', {})

    basket_items = []
    total = 0
    artifact_count = 0
    for id, quantity in basket.items():
        artifact = get_object_or_404(Artifact, pk=id)
        total += quantity * artifact.price
        artifact_count += quantity
        basket_items.append({'id':id, 'quantity': quantity, 'artifact': artifact})
    
    return { 'basket_items': basket_items, 'total': total, 'artifact_count': artifact_count }