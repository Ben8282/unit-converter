print("""
Welcome to the Temperature Converter!

1. Celsius → Fahrenheit
2. Fahrenheit → Celsius
3. Celsius → Kelvin
4. Kelvin → Celsius
5. Fahrenheit → Kelvin
6. Kelvin → Fahrenheit

Enter a number (1-6):
""")
while True:
    convertnum = input()
    if convertnum == "1":
        print("so what number to convert")
        while True:
            converta = input()
            try:
                converta = float(converta)
                convertb = converta
                break
            except ValueError:
                print("there was a problem you put a ok number right")
                print("well i dont think its my codes fault so try again")
        converta = converta*1.8
        converta = converta+32
        print(convertb," degrees celsius is ",converta,"degrees fahrenheit")
        break
    elif convertnum == "2":
        print("so what number to convert")
        while True:
            a = input()
            try:
                a = float(a)
                b = a
                break
            except ValueError:
                print("there was a problem you put a ok number right")
                print("well i dont think its my codes fault so try again")
        a = a-32
        a = a/1.8
        print(b," degrees fahrenheit is ",a,"degrees celsius")
        break
    elif convertnum == "3":
        print("so what number to convert")
        while True:
            c = input()
            try:
                c = float(c)
                d = c
                break
            except ValueError:
                print("there was a problem you put a ok number right")
                print("well i dont think its my codes fault so try again")
        c = c+273.15
        print(d," degrees celsius is ",c,"degrees kelvin")
        break
    elif convertnum == "4":
        print("so what number to convert")
        while True:
            e = input()
            try:
                e = float(e)
                f = e
                break
            except ValueError:
                print("there was a problem you put a ok number right")
                print("well i dont think its my codes fault so try again")
        e = e-273.15
        print(f," degrees kelvin is ",e,"degrees celsius")
        break
    elif convertnum == "5":
        print("so what number to convert")
        while True:
            e = input()
            try:
                e = float(e)
                f = e
                break
            except ValueError:
                print("there was a problem you put a ok number right")
                print("well i dont think its my codes fault so try again")
        e = e-32
        e = e/1.8
        e = e+273.15
        print(f," degrees fahrenheit is ",e,"degrees kelvin")
        break
    elif convertnum == "6":
        print("so what number to convert")
        while True:
            g = input()
            try:
                g = float(g)
                h = g
                break
            except ValueError:
                print("there was a problem you put a ok number right")
                print("well i dont think its my codes fault so try again")
        g = g-273.15
        g = g*1.8
        g = g+32
        print(h," degrees kelvin is ",g,"degrees fahrenheit")
        break
    else:
        print("plz enter a number from 1 to 6")
