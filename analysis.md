product :
    - name
    - flag (sale, feature, new)
    - image
    - images
    - price
    - sku
    - brand 
    - reviews *
    - tags 
    - simple disscription
    - full description
    - related


---------------------------------------
orders:
    - id
    - create_date
    - delivery_date
    - subtotal
    - delivery_fee
    - delivery_location
    - user
    - order_status [Recieved, Processed, Shipped, Delivered]
    - total
orders_detail:
    - product
    - quantity
    - price
    - total