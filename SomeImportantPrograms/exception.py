while True:
    try:
        number=int(input("enter your favourite number?:\n"))
        print(18/number)
        break

    except ValueError:
        print("Make sure and enter a number only")

    except ZeroDivisionError:
        print("dont pick zero")

    except: #if you dont know the type of exception
        break
    finally:
        print("Loop completed")