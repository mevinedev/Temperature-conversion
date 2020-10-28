celsius = int(input(" enter value to convert: "))
def conv(c):
    fahreinheit = (9/5 * celsius +32)
    return fahreinheit

fahreinheit = conv(celsius)
print("the value in fahreinheit is: ",fahreinheit)