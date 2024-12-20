weather = input("What's the weather like today? (sunny/rainy/cold):").lower()
if weather == "sunny":
    current_weather = "Wear a t-shirt and sunglasses."
elif weather == "rainy":
    current_weather = "Don't forget your umbrella and a raincoat."
elif weather == "cold":
    current_weather = "Make sure to wear a warm coat and a scarf."
else:
    current_weather = "Sorry, I don't have recommendations for this weather."
print(current_weather)