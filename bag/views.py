from django.shortcuts import render, redirect


def view_bag(request):
    """
    A view to return bag contents page
    """
    return render(
        request,
        'bag/bag.html'
    )


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None

    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        # check if item already in the bag
        if item_id in list(bag.keys()):
            # if yes, check if selected size is already in the bag
            if size in bag[item_id]['items_by_size'].keys():
                # if yes, increment quantity
                bag[item_id]['items_by_size'][size] += quantity
            else:
                #  if no, add size entry and quantity
                bag[item_id]['items_by_size'][size] = quantity
        else:
            #  if item not in bag, add item and a nested dict for size
            #  and quantity
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        #  if item has no size, add to bag
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
