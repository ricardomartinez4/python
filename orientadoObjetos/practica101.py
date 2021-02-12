"""
Uso de split mediante el formato
uso del zip
"""
# here, stock is string, we want to split it and
# convert the data in to correct format i.e. string, int and float
stock = "GOOG, 100, 20.3"
field_types = [str, int, float]
split_stock = stock.split(',') # split data and get a list
print(split_stock)
#['GOOG', ' 100', ' 20.3']
# change the format
stock_format = [ty(val) for ty, val in zip(field_types, split_stock)]
print(stock_format) # format = [str, int, float]
#['GOOG', 100, 20.3]