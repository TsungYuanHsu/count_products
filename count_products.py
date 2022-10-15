def count_products(data):
    product_dict = {}
    for p in data:
        p = p.split(' ')
        if p[0] not in product_dict:
            product_dict[p[0]] = int(p[1])
        else:
            product_dict[p[0]] += int(p[1])
    return product_dict

data = ['麥香奶茶 2', '御飯糰 1', '可可 10', '麥香奶茶 1']
print(count_products(data))

# # provide user input function
# data = []
# while True:
#     print('Type q to exit and start counting process')
#     product = input('Please input product name and count(example: blacktea 5): ')
#     if product == 'q':
#         print("start counting...", data)
#         break
#     else:
#         data.append(product)
# print(count_products(data))





