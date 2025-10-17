print(" sort a dictionary in ascending and descending order")

my_dict = {'banana': 3, 'apple': 5, 'cherry': 1}


asc_dict = dict(sorted(my_dict.items()))
print("Ascending order:", asc_dict)


desc_dict = dict(sorted(my_dict.items(), reverse=True))
print("Descending order:", desc_dict)
