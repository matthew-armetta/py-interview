# This is a sample Python script.
import random


# feedback: PEP8 convention is to use capital camel case for classnames, so can rename to GiftExchance.py
# locks keyboard and crosses arms.

def main():
    if len(participant_list) == 0:
        print("Let's put together a gift exchange! Add a name to get started.")
        get_names()
    elif len(participant_list) == 1:
        print("Buying a present for yourself isn't fun. Enter at least another name.")
        get_names()
    elif len(
            participant_list) > 1:
        more_names = input(f"There are {len(participant_list)} participants. Add more? 'Y' or 'N': ")
        if more_names.upper() == 'Y':
            get_names()
        elif more_names.upper() == 'N':
            receivers_list = random.sample(participant_list, len(participant_list))
            return assign_givers(participant_list, receivers_list)
        else:
            print("Invalid input...let's try again...")
            main()


# empty participant list
participant_list = []


def get_names():
    """ Get the list of people participating in the exchange. """
    getting_names = True
    while getting_names == True:  # feedback: this variable may not be necessary, just use while True and when "F" in inputted just break
        if len(participant_list) == 0:
            name = input(
                "Type the name of the first participant: ").strip()  # strip takes care of the whitespaces...
            # feedback: maybe allow the user to enter a comma separated list of names as well? can use "split" on input received
            if not name.isalpha():
                print(f"'{name}' doesn't look right, try again.")
                get_names()
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
                    get_names()
                else:
                    participant_list.append(name.capitalize())
    print(f"Here are the participants: {participant_list}.\n")
    main()


def assign_givers(givers, receivers):
    """  Given a list of givers, assigns each item to an item on the list of receivers, and removes that receiver from the receiver list """
    results = []
    for name in givers:
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
    return results  # feedback: unecessary return, the value is not used by the caller, the end goal was just to print the info


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
