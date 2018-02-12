print 'Fahrenheit to Celsius converter'
while True:
    try:
        firstquery = raw_input("Convert Celsius Fahrenheit, or Kelvin? [C/F/K]: ")
        firstquery = firstquery.lower()
        if firstquery == "c":
            secondquery = raw_input("Convert Celsius to Fahrenheit or Kelvin? [F/K]: ")
            secondquery = secondquery.lower()
            if secondquery == "f":
                tempC = raw_input("Enter temperature in Celsius: ")

                if tempC == "quit":
                    print "Shutting Down."
                    raise SystemExit
                else:
                    tempC = float(tempC)
                    tempF = (1.8 * tempC + 32)
                    print ("%.2f degrees Celsius is %.2f degrees Fahrenheit." % (tempC, tempF))
            elif secondquery == "k":
                tempC = raw_input("Enter temperature in Celsius: ")

                if tempC == "quit":
                    print "Shutting Down."
                    raise SystemExit
                else:
                    tempC = float(tempC)
                    tempK = (tempC + 273.15)
                    print ("%.2f degrees Celsius is %.2f degrees Kelvin" % (tempC, tempK))
        elif firstquery == "f":
            secondquery = raw_input("Convert Fahrenheit to Celsius or Kelvin? [C/K]: ")
            secondquery = secondquery.lower()

            if secondquery == "c":
                tempF = raw_input("Enter temperature in Fahrenheit: ")
                
                if tempF == "quit":
                    print "Shutting Down."
                    raise SystemExit
                else:
                    tempF = float(tempF)
                    tempC = (tempF - 32.0) * (5.0/9)
                    print ("%.2f degrees Fahrenheit is %.2f degrees Celsius." % (tempF, tempC))
            elif secondquery == "k":
                tempF = raw_input("Enter temperature in Fahrenheit: ")

                if tempF == "quit":
                    print "Shutting Down."
                    raise SystemExit
                else:
                    tempF = float(tempF)
                    tempK = (tempF + 459.67) * (5.0/9)
                    print ("%.2f degrees Fahrenheit is %.2f degrees Kelvin." % (tempF, tempK))
        elif firstquery == "k":
            secondquery = raw_input("Convert Kelvin to Celsius or Fahrenheit? [C/F]: ")
            secondquery = secondquery.lower()

            if secondquery == "c":
                tempK = raw_input("Enter temperature in Kelvin: ")

                if tempK == "quit":
                    print "Shutting Down."
                    raise SystemExit
                else:
                    tempK = float(tempK)
                    tempC =  (tempK - 273.15)
                    print ("%.2f degrees Kelvin is %.2f degrees Celsius." % (tempK, tempC))
            elif secondquery == "f":
                tempK = raw_input("Enter temperature in Kelvin: ")

                if tempK == "quit":
                    print "Shutting Down."
                    raise SystemExit
                else:
                    tempK = float(tempK)
                    tempF =  (tempK * (9.0/5) - 459.67)
                    print ("%.2f degrees Kelvin is %.2f degrees Fahrenheit." % (tempK, tempF))

        else:
            print "Error: Input must be C/F/K."
    except (AttributeError, NameError,ValueError):
        print "Error: Not a valid number."
    
