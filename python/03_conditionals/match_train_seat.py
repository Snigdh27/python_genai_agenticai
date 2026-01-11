seat_type = input("Enter seat type (sleeper/AC/general/luxury) :").lower()

match seat_type:
    case "sleeper":
        print("Sleeper seat booked. Price is Rs.150")
    case "ac":
        print("AC seat booked. Price is Rs.300")
    case "general":
        print("General seat booked. Price is Rs.100")
    case "luxury":
        print("Luxury seat booked. Price is Rs.500")
    case _:
        print("Unknown seat type")