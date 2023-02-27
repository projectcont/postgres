class Product:
    def __init__(self,product_id=0, product_ean="", product_title="", product_price=0 ):
        self.product_id = product_id
        self.product_ean = product_ean
        self.product_title = product_title
        self.product_price = product_price

    def __str__(self):
        return f'id={self.product_id};  ean={self.product_ean} title={self.product_title} price={self.product_price}'




