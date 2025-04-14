from Batch import Batch
from Order import Order


def batch_n_order(article, color, size, b_qty, o_qty):
    batch = Batch(article, color, size, b_qty)
    order = Order('ord-777', batch.sku, o_qty)
    return (batch, order)


def test_can_order_if_available():
    batch, order = batch_n_order('jeans', 'blue', 'm', 10, 5)
    assert batch.can_place_order(order)

    batch, order = batch_n_order('jeans', 'blue', 'm', 5, 5)
    assert batch.can_place_order(order)


def test_decrement_available_after_order():
    batch, order = batch_n_order('jeans', 'blue', 'm', 10, 5)
    batch.place_order(order)
    assert batch.available == 5

    order2 = Order('ord-778', batch.sku, 1)
    batch.place_order(order2)
    assert batch.available == 4


def test_cant_place_double_order():
    batch, order = batch_n_order('jeans', 'blue', 'm', 10, 5)
    batch.place_order(order)
    batch.place_order(order)
    assert batch.available == 5


def test_cant_order_if_not_available():
    batch, order = batch_n_order('jeans', 'blue', 'm', 1, 5)
    assert batch.can_place_order(order) is False


def test_cant_order_other_sku():
    batch = Batch('jeans', 'blue',  'm', 10)
    batch2 = Batch('jeans', 'black', 'm', 10)
    order = Order('ord-777', batch2.sku, 1)
    assert batch.can_place_order(order) is False


def test_available_count_after_remove_order():
    batch, order = batch_n_order('jeans', 'blue', 'm', 10, 5)
    batch.place_order(order)
    batch.remove_order(order)
    assert batch.available == 10


def test_available_count_after_remove_not_placed_order():
    batch, order = batch_n_order('jeans', 'blue', 'm', 10, 5)
    order2 = Order('ord-778', batch.sku, 1)
    batch.place_order(order)
    batch.remove_order(order2)
    assert batch.available == 5
