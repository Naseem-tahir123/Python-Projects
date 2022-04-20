weight =  int(input("enter your weight : "))
height = float (input("enter your height : "))
BMI = weight/float(height*height)
if (BMI < 18):
    print("Underweight")
if (BMI >18.5 and BMI<25):
    print("Normal")
if (BMI>25  and BMI<30):
    print("Overweight")
if (BMI>= 30):
    print("Obesity")