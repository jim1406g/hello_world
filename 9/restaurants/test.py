# from restaurant import Restaurant
from icecreamstand import IceCreamStand

# restaurant1 = Restaurant("Cantanella", "italian")
# restaurant2 = Restaurant("Meat&Fish", "european")
#
# print(restaurant1.restaurant_name)
# print(restaurant1.cuisine_type)
# restaurant1.describe_restaurant()
# restaurant1.open_restaurant()
#
# print("\n---------------------\n")
#
# print(restaurant2.restaurant_name)
# print(restaurant2.cuisine_type)
# restaurant2.describe_restaurant()
# restaurant2.open_restaurant()
#
# print("\n---------------------\n")
#
# restaurant1.set_number_served(100)
# print(restaurant1.number_served)
# restaurant1.increment_number_served(10)

ice_cream_stand = IceCreamStand('Inmarco')
print(ice_cream_stand.restaurant_name)
ice_cream_stand.describe_restaurant()
ice_cream_stand.describe_flavors()