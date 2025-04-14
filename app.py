from src.Batch import Batch
from src.Order import Order


batch = Batch('JEANS-SAMOPAL', "BLUE", 'M', 100)
print(batch)

order = Order(id='001', sku=batch.sku,  quatity=10)
order2 = Order(id='002', sku=batch.sku, quatity=10)
order3 = Order(id='003', sku=batch.sku, quatity=10)
order4 = Order(id='004', sku=batch.sku, quatity=10)
order5 = Order(id='005', sku=batch.sku, quatity=10)
order6 = Order(id='006', sku=batch.sku, quatity=50)
order7 = Order(id='007', sku=batch.sku, quatity=10)

batch.place_order(order)
batch.place_order(order2)
batch.place_order(order3)
batch.place_order(order4)
batch.place_order(order5)
batch.place_order(order6)
batch.place_order(order7)

print(batch.list_orders())
print(batch)
