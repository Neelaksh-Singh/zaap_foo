import random

food_list = [
    'Chuck E. Cheese','Target Pizza Hut',"Antonio's Pizza",'Romeos Pizza','Little Caesars',"Papa John's",'Dominos',"Pavona's Pizza Joint","Rocco's Pizza Shop","Teresa's Pizza","Mr. G's",
    'Subway','Jersey Mikes','Penn Station','Firehouse Subs','The Sub Station','Magic Subs & Gyros',"Mr. Zub's Deli", 'Corral Sanwich Shop','Hanini Subs',"Jimmy John's",
    'Taco Bell','Funky Truckeria','Chipotle',"Tito's Mexican Grill",'Tres Potrillos','El Rancho',"Moe's Southwest Grill",'BOMBA Tacos','Qdoba','Casa Del Rio',
    'China King','Imperial Wok','China Star','Platinum Dragon','Sushi Asia Gormet','China Express','New Ming Restaurant','House of Hunan','Sushi Katsu','Sakura','T J Sushi','Big Eye Japanese Cuisine & Sushi Bar','Hong Kong Buffet','Taste of Bankok','Hyde Out'
]

# Generates a random list of food items
def foodGenerator(tot_food_items_needed):
    ordered_food = random.choices(food_list,k=tot_food_items_needed)
    return ordered_food

    