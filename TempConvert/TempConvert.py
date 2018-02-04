print 'Fahrenheit to Celsius converter'
while True:
    try:
        tempF = raw_input("Enter temperature in Fahrenheit: ")

        if tempF == "quit":
            print "Shutting Down."
            raise SystemExit

        else:
            tempF = float(tempF)
            tempC = (tempF - 32.0) * (5.0/9)
            print ("%.2f degrees Fahrenheit is %.2f degrees Celsius." % (tempF, tempC))
    except (AttributeError, NameError,ValueError):
        print "Error: Not a valid number."
    
