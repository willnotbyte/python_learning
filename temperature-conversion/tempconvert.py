temp = input("Input the temperature you'd like to convert: (e.g., 45F, 102C, etc.): ")
degree = int(temp[:-1])
i_conversion = temp[-1]

if i_conversion.upper() == "C":
    result = int(round((9 * degree) / 5 + 32))
    o_conversion = "Fahrenheit"
elif i_conversion.upper() == "F":
    result = int(round((degree - 32) * 5 / 9))
    o_conversion = "Celsius"
else:
    print("Input not acceptable.")
    quit()
print("The temperature in", o_conversion, "is", result, "degrees.")