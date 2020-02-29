
def exception_handling():

    car = {'make': 'BMW', 'model': 'Road', 'year': 2001}

    try:
        print(car['color'])

    except:
        print("Error accessing the color")
#        raise Exception("No Key")
    else:
        print("No Error, because you have a valid key")
    finally:
        print()
        print("Please try another key in the car dictionary")


exception_handling()
