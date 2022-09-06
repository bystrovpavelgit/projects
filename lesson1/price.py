def format_price(price):
    """ function to format input to string"""
    price = int(price)
    return f"Цена: {price} руб."


out = format_price(56.24)
print(out)
 
