# This is a sample Python script.
import random

# feedback: PEP8 convention is to use capital camel case for classnames, so can rename to GiftExchance.py

def main():
    if len(participant_list) == 0:
        print("Let's put together a gift exchange! Add a name to get started.")
        get_names()
    elif len(
            participant_list) > 0:  # feedback: we are allowing only 1 entry but the code breaks if only 1 name is added...
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
''' get the list of people participating in the exchange.'''  # feedback: same as below, put as first line of function


def get_names():
    getting_names = True
    while getting_names == True:  # feedback: this variable may not be necessary, just use while True and when "F" in inputted just break
        if len(participant_list) == 0:
            name = input(
                "Type the name of the first participant: ")  # feedback: maybe use a regex to validate input?  i can put blank spaces in now, maybe check all chars are alphas and trim any white space
            # feedback: maybe allow the user to enter a comma separated list of names as well? can use "split" on input received
            participant_list.append(name)
        else:
            name = input(
                "Type another name, or -- if you're done -- type 'F': ")  # feedback: same regex comment here, how to apply to both?
            if name.upper() == "F":
                getting_names = False
            else:
                participant_list.append(name)
    print(f"Here are the participants: {participant_list}.\n")
    main()


''' Assign the members of the particpant list. '''  # feedback: this docstring should be double not single quotes and be the


# first line of the function, also no space between quotes and words, do u even PEP8 bro, also u do even spell participant
# correctly bro


def matching(givers, receivers):  # feedback: more descriptive function name, matching what?
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
