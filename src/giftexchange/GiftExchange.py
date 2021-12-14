# This is a sample Python script.
import random

# feedback: PEP8 convention is to use capital camel case for classnames, so can rename to GiftExchance.py
# locks keyboard and crosses arms.

# empty participant list
participant_list = []


def main():
    begin_game()


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
    return assign_givers(names_for_game) if more_names.upper() == 'N' else get_names_for_games()


def get_names_for_games():
    """ Get the list of people participating in the exchange. """
    getting_names = True
    while getting_names:
        if len(participant_list) == 0:
            name = input(
                "Type the name of the first participant: ").strip()  # strip takes care of the whitespaces...
            # feedback: maybe allow the user to enter a comma separated list of names as well? can use "split" on input received
            if not name.isalpha():
                # feedback: move alpha check and dupe check into its own function, call that here, and in next condition
                print(f"'{name}' doesn't look right, try again.")
                get_names_for_games()
            elif name.capitalize() in participant_list:
                print(f"{name} is already on the list!")
                get_names_for_games()
            else:
                participant_list.append(name.capitalize())
        else:
            name = input(
                "Type another name, or -- if you're done -- type 'F': ").strip()  # feedback: same regex comment here, how to apply to both?
            if name.upper() == "F":
                getting_names = False
            else:
                if not name.isalpha():
                    print(f"'{name}' doesn't look right, try again.")
                    get_names_for_games()
                else:
                    participant_list.append(name.capitalize())
    print(f"Here are the participants: {participant_list}.\n")
    main()


def assign_givers(names_for_game):
    """  Given a list of givers, assigns each item to an item on the list of receivers, and removes that receiver from the receiver list """
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

    with open("gift_exchange.txt", 'w') as out_file:
        out_file.write("The game will be played as follows: " + str(results))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
