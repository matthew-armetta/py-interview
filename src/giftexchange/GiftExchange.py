import sys
import random
import logging
import timeit

# feedback: PEP8 convention is to use capital camel case for classnames, so can rename to GiftExchance.py
# locks keyboard and crosses arms.

# empty participant list
participant_list = []
start = timeit.timeit()


def main():
    begin_game()
    logging.info(f"Started game at {start}.")


def begin_game():
    if len(participant_list) == 0:
        print("Let's put together a gift exchange! Add a name to get started.")
        get_names_for_games()
    elif len(participant_list) == 1:
        print("Buying a present for yourself isn't fun. Enter at least another name.")
        get_names_for_games()
    else:
        start_gift_exchange(participant_list)


def start_gift_exchange(names_for_game):
    more_names = input(f"There are {len(names_for_game)} participants. Add more? 'Y' or 'N': ")
    logging.debug(f"names_for_games: {names_for_game}, user selected {more_names}")
    return assign_givers(names_for_game) if more_names.upper() == 'N' else get_names_for_games()


def get_names_for_games():
    """ Get the list of people participating in the exchange. """
    getting_names = True
    while getting_names:
        if len(participant_list) == 0:
            name = input("Type the name of the first participant: ").strip()  # strip takes care of the whitespaces...
            # feedback: maybe allow the user to enter a comma separated list of names as well? can use "split" on
            # input received
            validate_input(name)
        else:
            name = input("Type another name, or -- if you're done -- type 'F': ").strip()
            if name.upper() == "F":
                getting_names = False
            else:
                validate_input(name)
    print(f"Here are the participants: {participant_list}.\n")
    logging.debug(f"Starting game with participants: {participant_list}")
    main()


def validate_input(entered_name):
    """ Checks the entered name to make sure it contains only alpha characters and is not a duplicate name. """
    if entered_name.isalpha() and entered_name.capitalize() not in participant_list:
        participant_list.append(entered_name.capitalize())
        logging.debug(f"Added name: {entered_name.capitalize()}.")
    elif not entered_name.isalpha():
        print(f"'{entered_name}' doesn't look right, try again.")
        logging.debug(f"Non-alpha name {entered_name} was given.")
        get_names_for_games()
    elif entered_name.capitalize() in participant_list:
        print(f"{entered_name} is already on the list!")
        logging.debug(f"Name {entered_name.capitalize()} was already on the list.")
        get_names_for_games()


def assign_givers(names_for_game):
    """  Given a list of givers, assigns each item to an item on the list of receivers, and removes that receiver
    from the receiver list """
    receivers = random.sample(names_for_game, len(names_for_game))
    results = []
    for name in names_for_game:
        giver = name
        receiver = receivers[0]
        if giver == receiver:
            receiver = receivers[1]
            results.append(giver + ' --> ' + receiver)
            receivers.pop(1)
        else:
            receiver = receivers[0]
            results.append(giver + ' --> ' + receiver)
            receivers.pop(0)
    print(results)
    logging.info(f"Results are: {results}")

    with open("gift_exchange.txt", 'w') as out_file:
        out_file.write("The game will be played as follows: " + str(results))
        print('Gift exchange results written to file.')
    end_game()


def end_game():
    print("Thanks for setting up your gift exchange!\n")
    next_step = input("If you want to try again, type 'Y'. Otherwise, press Enter.")
    if next_step.capitalize() == 'Y':
        participant_list.clear()
        print('....\n' * 10)
        main()
    else:
        end = timeit.timeit()
        logging.info(f"Total game time: {end - start}")
        sys.exit("Bye!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
