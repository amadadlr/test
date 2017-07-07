import random

Appetizers= ("Dragon Roll",
"Hawaiian Coconut Shrimp",
"Steak + Coconut Shrimp",
"Tortilla Soup",
"West Coast Ahi Tuna Salad",
"Ahi Tuna Tataki",
"Dragon Roll",
"Dynamite Roll",
"Avocado Super Toast",
"Garlic Fries",
"Hawaiian Coconut Shrimp",
"Hot Wings",
"Italian Style Pan Bread",
"Korean Hot Wings",
"Truffle Fries",
"Noodles + Rice Bowls")

MainCourse= ("Chicken Fettuccine Alfredo",
"Fettuccine Alfredo",
"Cajun Chicken",
"Chimichurri Skirt Steak",
"Oven Roasted Atlantic Salmon",
"Baja Fish Tacos",
"Chicken Pibil Taco",
"Bacon Cheddar Burger",
"California Burger"
)

Dessert= ("Coconut Cream Pie",
"Peanut Butter Skillet Cookie",
"Sticky Toffee Chocolate Pudding",
"Strawberry Cheesecake")

secure_random = random.SystemRandom()
print(secure_random.choice(Appetizers))
print(secure_random.choice(MainCourse))
print(secure_random.choice(Dessert))
