def recite(start_verse, end_verse):
    """Return the requested verses of the nursery rhyme.

    Parameters:
        start_verse (int): The first verse to recite.
        end_verse (int): The last verse to recite.

    Returns:
        list[str]: The requested verses, in order.
    """

    things = ["house that Jack built" , 
              "malt",
              "rat",
              "cat",
              "dog",
              "cow with the crumpled horn",
              "maiden all forlorn",
              "man all tattered and torn",
              "priest all shaven and shorn",
              "rooster that crowed in the morn",
              "farmer sowing his corn",
              "horse and the hound and the horn"
              ]

    actions = ["lay in",
               "ate",
               "killed",
               "worried",
               "tossed",
               "milked",
               "kissed",
               "married",
               "woke",
               "kept",
               "belonged to"
    ]

    verses = []

    for verse_num in range(start_verse, end_verse + 1):
        index = verse_num - 1

        verse = f"This is the {things[index]}"

        while index > 0:
            verse += f" that {actions[index - 1]} the {things[index - 1]}"
            index -= 1

        verse += "."
        verses.append(verse)

    return verses