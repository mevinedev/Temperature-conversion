celsius = int(input(" enter value to convert: "))
def convert(c):
    fahreinheit = ((9/5) * (celsius +32))
    return fahreinheit

fahreinheit = convert(celsius)
print("the value in fahreinheit is: ",fahreinheit)

