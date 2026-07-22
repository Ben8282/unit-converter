print("""
Welcome to the Unit Converter!

Choose a category:

1. Temperature
2. Length

Enter a number:
""")
while True:
    category = input()
    if category == "1":
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
        break
    elif category == "2":
        print("""
Welcome to the Length Converter!

Choose the unit you want to convert FROM:

1. Millimetres (mm)
2. Centimetres (cm)
3. Metres (m)
4. Kilometres (km)
5. Inches (in)
6. Feet (ft)
7. Yards (yd)
8. Miles (mi)

Enter a number (1-8):
""")    
        while True:
            convertlength1 = input()
            if convertlength1 in ["1","2","3","4","5","6","7","8"]:
                print("please enter number to convert")
                whatconvert = input()
                break
            else:
                print("please make sure you enter a number from 1 to 8")
        if convertlength1 == "1":
            while True:
                try:
                    whatconvert = float(whatconvert)
                    original_value = whatconvert
                    break
                except:
                    print("you didnt enter a valid number")
                    print("what number would you like to convert")
                    whatconvert = input()
            whatconvert = whatconvert/1000
        elif convertlength1 == "2":
            while True:
                try:
                    whatconvert = float(whatconvert)
                    original_value = whatconvert
                    break
                except:
                    print("you didnt enter a valid number")
                    print("what number would you like to convert")
                    whatconvert = input()
            whatconvert = whatconvert/100
        elif convertlength1 == "3":
            while True:
                try:
                    whatconvert = float(whatconvert)
                    original_value = whatconvert
                    break
                except:
                    print("you didnt enter a valid number")
                    print("what number would you like to convert")
                    whatconvert = input()
        elif convertlength1 == "4":
            while True:
                try:
                    whatconvert = float(whatconvert)
                    original_value = whatconvert
                    break
                except:
                    print("you didnt enter a valid number")
                    print("what number would you like to convert")
                    whatconvert = input()
            whatconvert = whatconvert*1000
        elif convertlength1 == "5":
            while True:
                try:
                    whatconvert = float(whatconvert)
                    original_value = whatconvert
                    break
                except:
                    print("you didnt enter a valid number")
                    print("what number would you like to convert")
                    whatconvert = input()
            whatconvert = whatconvert*0.0254
        elif convertlength1 == "6":
            while True:
                try:
                    whatconvert = float(whatconvert)
                    original_value = whatconvert
                    break
                except:
                    print("you didnt enter a valid number")
                    print("what number would you like to convert")
                    whatconvert = input()
            whatconvert = whatconvert*0.3048
        elif convertlength1 == "7":
            while True:
                try:
                    whatconvert = float(whatconvert)
                    original_value = whatconvert
                    break
                except:
                    print("you didnt enter a valid number")
                    print("what number would you like to convert")
                    whatconvert = input()
            whatconvert = whatconvert*0.9144
        elif convertlength1 == "8":
            while True:
                try:
                    whatconvert = float(whatconvert)
                    original_value = whatconvert
                    break
                except:
                    print("you didnt enter a valid number")
                    print("what number would you like to convert")
                    whatconvert = input()
            whatconvert = whatconvert*1609.344
        else: 
            print("there was a error that sadly might have been my codes fault")
        print("""
Choose the unit you want to convert TO:

1. Millimetres (mm)
2. Centimetres (cm)
3. Metres (m)
4. Kilometres (km)
5. Inches (in)
6. Feet (ft)
7. Yards (yd)
8. Miles (mi)

Enter a number (1-8):
""")    
        while True:
            convertto = input()
            try:
                convertto = float(convertto)
            except ValueError:
                print("put in a actual number bro and")
            if convertto in [1,2,3,4,5,6,7,8]:
                break
            else:
                print("make sure your number is between 1 and 8 ")
        convertwhat = whatconvert
        if convertto == 1:
            convertwhat = convertwhat*1000
        elif convertto == 2:
            convertwhat = convertwhat*100
        elif convertto == 3:
            pass
        elif convertto == 4:
            convertwhat = convertwhat/1000
        elif convertto == 5:
            convertwhat = convertwhat/0.0254
        elif convertto == 6:
            convertwhat = convertwhat/0.3048
        elif convertto == 7:
            convertwhat = convertwhat/0.9144
        elif convertto == 8:
            convertwhat = convertwhat/1609.344
        else:
            print("error this was not supposed to happen")
        if convertlength1 == "1":
            original_unit = "Millimetres (mm)"
        elif convertlength1 == "2":
            original_unit = "Centimetres (cm)"
        elif convertlength1 == "3":
            original_unit = "Metres (m)"
        elif convertlength1 == "4":
            original_unit = "Kilometres (km)"
        elif convertlength1 == "5":
            original_unit = "Inches (in)"
        elif convertlength1 == "6":
            original_unit = "Feet (ft)"
        elif convertlength1 == "7":
            original_unit = "Yards (yd)"
        elif convertlength1 == "8":
            original_unit = "Miles (mi)"
        else:
            print("this error was not supposed to happen um 67")
        if convertto == 1.0:
            new_unit = "Millimetres (mm)"
        elif convertto == 2.0:
            new_unit = "Centimetres (cm)"
        elif convertto == 3.0:
            new_unit = "Metres (m)"
        elif convertto == 4.0:
            new_unit = "Kilometres (km)"
        elif convertto == 5.0:
            new_unit = "Inches (in)"
        elif convertto == 6.0:
            new_unit = "Feet (ft)"
        elif convertto == 7.0:
            new_unit = "Yards (yd)"
        elif convertto == 8.0:
            new_unit = "Miles (mi)"
        else:
            print("this error was not supposed to happen") 
        print(original_value, original_unit, "is", convertwhat, new_unit)      
        break
    else:
        print("plz enter either 1 or 2")

