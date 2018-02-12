print 'Fahrenheit to Celsius converter'
while True:
    try:
        firstquery = raw_input("Convert to Celsius or Fahrenheit? [C/F]: ")
        firstquery = firstquery.lower()
        if firstquery == "f":
            tempCPrint = raw_input("Enter temperature in Celsius: ")

            if tempCPrint == "quit":
                print "Shutting Down."
                raise SystemExit
            else:
                tempCPrint = float(tempCPrint)
                tempFPrint = (1.8 * tempCPrint + 32)
                print ("%.2f degrees Celsius is %.2f degrees Fahrenheit." % (tempCPrint,tempFPrint))
        elif firstquery == "c":
            tempF = raw_input("Enter temperature in Fahrenheit: ")

            if tempF == "quit":
                print "Shutting Down."
                raise SystemExit
            else:
                tempF = float(tempF)
                tempC = (tempF - 32.0) * (5.0/9)
                print ("%.2f degrees Fahrenheit is %.2f degrees Celsius." % (tempF, tempC))
        else:
            print "Error: Input must be C or F."
    except (AttributeError, NameError,ValueError):
        print "Error: Not a valid number."
    
