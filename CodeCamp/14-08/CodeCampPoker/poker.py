'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''

def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    i = 0
    l_2 = []
    while(i<len(hand)):
        if hand[i][0] == 'T':
            k = hand[i][0].replace("T", "10")
            l_2.append(int(k))
        elif hand[i][0] == 'J':
            k = hand[i][0].replace("J", "11")
            l_2.append(int(k))
        elif hand[i][0] == 'Q':
            k = hand[i][0].replace("Q", "12")
            l_2.append(int(k))
        elif hand[i][0] == 'K':
            k = hand[i][0].replace("K", "13")
            l_2.append(int(k))
        elif hand[i][0] == 'A':
            k = hand[i][0].replace("A", "14")
            l_2.append(int(k))
        else:
            k = (hand[i][0])
            l_2.append(int(k))
        i = i+1
    l_3 = sorted(l_2)
    p_tr = 0
    k_tr = 1
    check1 = 1
    while k_tr < len(l_3) and check1 == 1:
        if l_3[k_tr]-l_3[p_tr] == 1:
            pass
        else:
            check1 = 0
        k_tr = k_tr + 1
        p_tr = p_tr + 1
    return check1 == 1

def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    pass
    is_flush = 1
    flush = []
    i = 0
    j = 1
    is_flush = 1
    while(j<len(hand) and is_flush == 1):
        if hand[i][1] != hand[j][1]:
            is_flush = 0
        else:
            i = i + 1
            j = j + 1
        if is_flush == 1:
            flush.append(hand)
    return is_flush == 1


def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''

    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
    is_straigh = is_straight(hand)
    is_flus = is_flush(hand)
    if is_flus and is_straigh:
        return 3
    elif is_flus:
        return 2
    elif is_straigh:
        return 1
    else:
        return 0
def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
