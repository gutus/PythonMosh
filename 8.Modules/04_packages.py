# PACKAGES
from ecommerce.sales import calc_tax, calc_shipping
from ecommerce import sales

s = sales.calc_shipping()
t = sales.calc_tax()

print(f"Ini adalah contoh import packages untuk Shipping >>> \n{s}")
print(f"Ini adalah contoh import packages untuk Tax >>> \n{t}")
