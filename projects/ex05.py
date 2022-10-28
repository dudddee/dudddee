name = 'Eduardo V. Vilaronga'
age = 18
height_cm = 177
height_in = height_cm * 0.393701
weight_kg = 63
weight_pounds = weight_kg * 2.20462
eyes = 'brown'
teeth = 'white'
hair = 'brown'

print(f"let's talk about {name}")
print(f"he's {height_cm:.2f} centimeters tall, which equals {height_in:.2f} inches")
print(f"he's {weight_kg:.2f} kilograms heavy, which equals {weight_pounds:.2f} pounds")
print("actually that's not too heavy")
print(f"he's got {eyes} eyes and {hair} hair")
print(f"his teeth are usually {teeth} depending on the coffee")

total = age + height_cm + weight_kg
print(f"if i add {age}, {height_cm}, and {weight_kg} i get {total}")