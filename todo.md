

- orders

- cart
- checkout
- coupons
- home
- payment
- celery
- redis
- docker
- caching
- testing
- debloy
- aws
- vueje basics






    quantity = request.POST['quantity'] # or request.POST.get('quantity') it is the same think
    product = Product.objects.get(id=request.POST['product_id'])
    cart = Cart.objects.get(user=request.user, cart_status = 'Inprogress')
    cart_detail,created = CartDetail.objects.get_or_create(cart=cart,product=product)
    cart_detail.quantity = quantity
    cart_detail.price = product.price
    cart_detail.total = round(int(quantity) * product.price,2)
    cart_detail.save()
    return redirect(f'/products/{product.slug}')




