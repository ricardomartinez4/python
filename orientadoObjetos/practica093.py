"""
Sobrecarga de operadores:
     __call__
     __doc__
"""
class CalculatePrice:
    """
    Clase que nos va a servir para calcular descuentos aplicados a un precio dado
    """
    # discount in %
    def __init__(self, discount):
        self.discount = discount
    def __call__(self, price):
        discountPrice = price - price*self.discount/100
        return (price, discountPrice)
    
def main():
    # create object of class CalculatePrice with 10% discount
    d = CalculatePrice(10)
    # using object as function i.e. d(300)
    # since two variables are return by call fuction, therefore
    # unpack the return values in two variables
    price, priceAfterDiscount = d(300)
    print("Original Price: %s , Price after discount : %s " % (price, priceAfterDiscount))
    ## or use below method, if you do not want to unpack the return values
    # getPrices = d(300)
    # print("Original Price: %s, Price after discount : %s "
    # % (getPrices[0], getPrices[1]))
    
    
    # AQUI ESTOY CRENADO OBJETOS QUE NO SE USAN, no es como los métodos de clase o abstractos
    
    print("Original Price: %s , Price after discount : %s " % CalculatePrice(10)(300))
    
    # Ahora usamos el __doc__
    print(CalculatePrice.__doc__)
    
    # Ahora el nombre de la clase de la instancia
    print(d.__class__)
    print(d.__class__.__name__)
    print(isinstance(d,CalculatePrice))

    
    # standard boilerplate to set 'main' as starting function
if __name__=='__main__':
    main()