# This is a sample Python script.
import random


def main():
    if len(participant_list) == 0:
        print("Let's put together a gift exchange! Add a name to get started.")
        get_names()
    elif len(participant_list) > 0:
        more_names = input(f"There are {len(participant_list)} participants. Add more? 'Y' or 'N': ")
        if more_names.upper() == 'Y':
            get_names()
        elif more_names.upper() == 'N':
            receivers_list = random.sample(participant_list, len(participant_list))
            return matching(participant_list, receivers_list)
        else:
            print("Invalid input...let's try again...")
            main()


# empty participant list
participant_list = []

###  start defining the functions ###
''' get the list of people participating in the exchange.'''


def get_names():
    getting_names = True
    while getting_names == True:
        if len(participant_list) == 0:
            name = input("Type the name of the first participant: ")
            participant_list.append(name)
        else:
            name = input("Type another name, or -- if you're done -- type 'F': ")
            if name.upper() == "F":
                getting_names = False
            else:
                participant_list.append(name)
    print(f"Here are the participants: {participant_list}.\n")
    main()


''' Assign the members of the particpant list. '''


def matching(givers, receivers):
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
    return results


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
