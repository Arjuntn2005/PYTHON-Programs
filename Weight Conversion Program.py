# Weight Conversion Program

weight = float(input("Enter your weight : "))
unit   = input("Kilograms or Pounds?(K/P) : ")

if unit =="K":
    weight = weight* 2.205
    unit  = "pounds"
elif unit =="P":
    weight = weight/2.205
    unit ="kilograms"
else:
    print("Invalid Unit!")
    exit()

print(f"Your weigth is : {round(weight,2)} {unit}")

