import connect_
from  product_ import Product
from query_  import execute_query, read_query
from configuration import dbconf

db_name=dbconf['database']
db_user=dbconf['user']
db_password=dbconf['password']
db_host=dbconf['host']
db_port=dbconf['port']

connection = connect_.create_connection( db_name, db_user, db_password, db_host, db_port)


query_get='SELECT * FROM product'
fetched=read_query(connection, query_get)


prodlist=[]
for n in fetched:
    #print(n)
    prod_=Product()
    prod_.product_id=n[0]
    prod_.product_ean =n[2]
    prod_.product_price =n[3]
    prod_.product_title =n[1]
    print(prod_)
    prodlist.append(prod_)


highest_id=0;
for prod_ in  prodlist:
    if  prod_.product_id>highest_id: highest_id=prod_.product_id;
print(highest_id)

prod_=Product( product_id=2, product_ean="ean",product_title="Very nice", product_price=1200 )


# UPDATING A PRODUCT
update_product_price = "UPDATE product SET price = 333 WHERE product_id = 2"
execute_query(connection,  update_product_price)
update_product_ean = "UPDATE product SET ean = 'eanteapot' WHERE product_id = 2"
execute_query(connection,  update_product_ean)



# INSERTING A PRODUCT
#  product-instance
prod_=Product( product_id=highest_id+1, product_ean="ean",product_title="Very nice", product_price=1200 )
# tuple from product-instance
prod = (prod_.product_id, prod_.product_ean, prod_.product_title, prod_.product_price)
# forming a query
insert_query = (f"INSERT INTO product (product_id, title, ean, price) VALUES {prod}")
# do query
execute_query(connection, insert_query)

















