import os,django
os.environ["DJANGO_SETTINGS_MODULE"] = "project.settings"


django.setup()

from faker import Faker 
import random
from product.models import Product, Brand



def seed_brand(n):
    fake = Faker()
    images = ['2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jepg','9.jpg','10.jpg']
    for _ in range(n):
        name = fake.name()
        image = f"brand/{images[random.randint(0,8)]}"
        Brand.objects.create(name=name,image=image)

    print(f"seed {n} Brand ....")



def seed_product(n):
    fake = Faker()
    images = ['01.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpeg','9.jpg','10.jpg','11.png','12.png','13.jpeg','14.jpeg']
    flag_type = ['Sale','Feature','New']

    for _ in range(n):
        name=fake.name()
        sku = random.randint(1,100000)
        image = f"product/{images[random.randint(0,13)]}"
        brand = Brand.objects.get(id=random.randint(4,23))
        price = round(random.uniform(20.99,99.99),2)
        flag = flag_type[random.randint(0,2)]
        subtitle = fake.text(max_nb_chars=500)
        describtion =fake.text(max_nb_chars=2000)
        quantity = random.randint(2,30)

        Product.objects.create(
            name=name,
            image = image,
            sku=sku,
            price=price,
            flag =flag,
            brand=brand,
            subtitle=subtitle,
            describtion=describtion,
            quantity=quantity
        )
    print (f'seed {n} product .....')


#seed_brand(20)
seed_product(3000)

