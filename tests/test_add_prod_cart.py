from playwright.sync_api import Page
from pages.products_page import ProductPage
from pages.cart_page import CartPage

def test_prod_add_cart(page : Page , start_home):
    
    product = ProductPage(page)
    cart = CartPage(page)
    count = 2
    first_item = 4
    second_item = 5
    

    start_home.click_products_button()
    prod_price = int(product.get_item_price(first_item).replace("Rs." , ""))
    prod_price2 = int(product.get_item_price(second_item).replace("Rs." , ""))
    prod_quantity = 1
    prod_quantity2 = 1

    product.hover_and_click_prod(first_item)
    product.click_continue_shopping()
    product.hover_and_click_prod(second_item)
    product.view_cart()
    

    cart_price = int(cart.get_item_price(0).replace("Rs." , ""))
    cart_price2 = int(cart.get_item_price(1).replace("Rs." , ""))
    cart_quantity = int(cart.get_quantity(0))
    cart_quantity2 = int(cart.get_quantity(1))

    total = int(cart.total_price(0).replace("Rs." , ""))
    total1 = int(cart.total_price(1).replace("Rs." , ""))

    cart.check_count_prod(count)
    assert total == cart_price * cart_quantity
    assert total1 == cart_price2 * cart_quantity2
    assert total == prod_price * prod_quantity
    assert total1 == prod_price2 * prod_quantity2
    assert prod_price == cart_price
    assert prod_price2 == cart_price2
    assert cart_quantity == prod_quantity
    assert cart_quantity2 == prod_quantity2



