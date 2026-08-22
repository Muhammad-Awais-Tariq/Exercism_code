def recite(start_verse, end_verse):
    """Return the requested verses of the The Twelve Days of Christmas.

    Parameters:
        start_verse (int): The first verse to recite.
        end_verse (int): The last verse to recite.

    Returns:
        list[str]: The requested verses, in order.
    """

    ordinals = ["first", "second", "third", "fourth", "fifth", "sixth",
            "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]

    gifts = ["a Partridge in a Pear Tree", "two Turtle Doves", "three French Hens",
            "four Calling Birds", "five Gold Rings", "six Geese-a-Laying",
            "seven Swans-a-Swimming", "eight Maids-a-Milking", "nine Ladies Dancing",
            "ten Lords-a-Leaping", "eleven Pipers Piping", "twelve Drummers Drumming"]

    