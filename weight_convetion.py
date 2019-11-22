weight = int(input("enter your weight "))
unit_of_measure = input("is this kg or lb? ").lower()


if unit_of_measure == "kg":
 print(f'You are {weight / 0.45359237} LB')
elif unit_of_measure == "lb":
 print(f'You are {weight / 2.2046} KG ')



