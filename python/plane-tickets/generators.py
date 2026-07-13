"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """
    generated = 0
    for val in ["A" , "B" , "C" , "D"]:
        if generated == number:
            return
        yield val
        generated += 1

def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """

    generated = 0
    row = 1

    while generated < number:

        if row == 13:
            row += 1
            continue
        
        for seat in ["A" , "B" , "C" , "D"]:
            if generated == number:
                return 
            yield f"{row}{seat}"

            generated += 1
        row +=1


def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """
    assigned_dict = {}
    no_of_seats = len(passengers)
    seats = generate_seats(no_of_seats)
    for passenger in passengers:
        assigned_dict[passenger] = next(seats)
    return assigned_dict


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers:
        total_zero = 12 - (len(seat) + len(flight_id))
        code = f"{seat}{flight_id}{"0"*total_zero}"
        yield code