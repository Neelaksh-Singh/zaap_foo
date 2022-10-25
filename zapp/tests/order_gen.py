# To check whether the app produces random order menu
import random
from zapp.Producer.food_item import foodGenerator


food_lists = {
    "pizza": ['Chuck E. Cheese','Target Pizza Hut',"Antonio's Pizza",'Romeos Pizza','Little Caesars',"Papa John's",'Dominos',"Pavona's Pizza Joint","Rocco's Pizza Shop","Teresa's Pizza","Mr. G's"],
    "sanwich": ['Subway','Jersey Mikes','Penn Station','Firehouse Subs','The Sub Station','Magic Subs & Gyros',"Mr. Zub's Deli", 'Corral Sanwich Shop','Hanini Subs',"Jimmy John's"],
    "mexican": ['Taco Bell','Funky Truckeria','Chipotle',"Tito's Mexican Grill",'Tres Potrillos','El Rancho',"Moe's Southwest Grill",'BOMBA Tacos','Qdoba','Casa Del Rio'],
    "burger": ['Wayback','The Rail','Five Guys',"Louie's Bar & Grille","Bob's Hamburg",'Swensons',"Rally's",'Skyway',"Hodge's Cafe","Wendy's",'Burger King',"McDonald's"],
    "healthy": ['First Watch',"Ms. Julie's Kitchen",'Continental Cuisine',"Niko's Sandwich Board",'Poke Fresh','Zoup!',"Aladdin's Eatery","Beau's Grille",'Valley Cafe','CoreLife Eatery'],
    "asian": ['China King','Imperial Wok','China Star','Platinum Dragon','Sushi Asia Gormet','China Express','New Ming Restaurant','House of Hunan','Sushi Katsu','Sakura','T J Sushi','Big Eye Japanese Cuisine & Sushi Bar','Hong Kong Buffet','Taste of Bankok','Hyde Out']}

# category = random.choices(list(food_lists.keys()),k=2)
# print(category)
# rest_list=random.choices(food_lists[category],k=4)
# print(rest_list)
print(foodGenerator(4))
