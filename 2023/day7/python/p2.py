# TODO: This is a WIP still failing cases

import functools

strengths = {"J": 1, "2": 2, "3": 3, "4": 4, "5": 5,
             "6": 6, "7": 7, "8": 8, "9": 9, "T": 10,
             "Q": 12, "K": 13, "A": 14}


def five_of_a_kind(hand):
    dic = {}
    for card in hand:
        if card in dic:
            dic[card] += 1
        else:
            dic[card] = 1
    if len(dic) == 1:
        return True
    if len(dic) == 2 and "J" in dic:
        return True
    return False


def four_of_a_kind(hand):
    dic = {}
    for card in hand:
        if card in dic:
            dic[card] += 1
        else:
            dic[card] = 1
    if len(dic) == 2:
        for card in dic:
            if dic[card] == 4:
                return True
    if len(dic) == 3 and "J" in dic and dic["J"] == 1:
        return True
    return False


def full_house(hand):
    dic = {}
    for card in hand:
        if card in dic:
            dic[card] += 1
        else:
            dic[card] = 1
    if len(dic) == 2:
        for card in dic:
            if dic[card] == 3 or dic[card] == 2:
                return True
    if len(dic) == 3 and "J" in dic and dic["J"] == 1:
        return True
    return False


def three_of_a_kind(hand):
    dic = {}
    for card in hand:
        if card in dic:
            dic[card] += 1
        else:
            dic[card] = 1
    if len(dic) == 3:
        for card in dic:
            if dic[card] == 3:
                return True
    if len(dic) == 4 and "J" in dic and dic["J"] == 1:
        return True
    if len(dic) == 4 and "J" in dic and dic["J"] == 2:
        return True
    return False


def two_pairs(hand):
    dic = {}
    for card in hand:
        if card in dic:
            dic[card] += 1
        else:
            dic[card] = 1
    if len(dic) == 3:
        for card in dic:
            if dic[card] == 2:
                return True
    if len(dic) == 4 and "J" in dic and dic["J"] == 1:
        return True
    return False


def one_pair(hand):
    dic = {}
    for card in hand:
        if card in dic:
            dic[card] += 1
        else:
            dic[card] = 1
    if len(dic) == 4:
        for card in dic:
            if dic[card] == 2:
                return True
    if len(dic) == 5 and "J" in dic and dic["J"] == 1:
        return True
    return False


def stronger_hand(hand1, hand2):
    for i in range(5):
        if hand1[i] > hand2[i]:
            return 1
        elif hand1[i] < hand2[i]:
            return 2


def compare_hands(hand1, hand2):
    hand1 = hand1.split()[0]
    hand2 = hand2.split()[0]
    hand_strengths = [five_of_a_kind, four_of_a_kind, full_house,
                      three_of_a_kind, two_pairs, one_pair]

    for eval_func in hand_strengths:
        hand1_strength = eval_func(hand1)
        hand2_strength = eval_func(hand2)

        if hand1_strength and hand2_strength:
            for i in range(5):
                if strengths[hand1[i]] > strengths[hand2[i]]:
                    return 1
                elif strengths[hand1[i]] < strengths[hand2[i]]:
                    return -1

        if hand1_strength:
            return 1
        if hand2_strength:
            return -1

    for i in range(5):
        if strengths[hand1[i]] > strengths[hand2[i]]:
            return 1
        elif strengths[hand1[i]] < strengths[hand2[i]]:
            return -1

    return 0


with open("../sample.txt", "r") as f:
    contents = f.read().splitlines()

sorted_hands = sorted(contents, key=functools.cmp_to_key(compare_hands))
total = 0
for i, hand in enumerate(sorted_hands):
    total += (i + 1) * int(hand.split()[1])

print(sorted_hands)
print(total)
