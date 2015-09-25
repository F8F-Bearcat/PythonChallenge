''' homework '''
# CS 212, hw1-2: Jokers Wild
#
# -----------------
# User Instructions
#
# Write a function best_wild_hand(hand) that takes as
# input a 7-card hand and returns the best 5 card hand.
# In this problem, it is possible for a hand to include
# jokers. Jokers will be treated as 'wild cards' which
# can take any rank or suit of the same color. The
# black joker, '?B', can be used as any spade or club
# and the red joker, '?R', can be used as any heart
# or diamond.
#
# The itertools library may be helpful. Feel free to
# define multiple functions if it helps you solve the
# problem.
#
# -----------------
# Grading Notes
#
# Muliple correct answers will be accepted in cases
# where the best hand is ambiguous (for example, if
# you have 4 kings and 3 queens, there are three best
# hands: 4 kings along with any of the three queens).

import itertools

def red_joker(hand):
    "Hand has only a red joker"
    red_deck = [r+s for r in '23456789TJQKA' for s in 'HD']
    no_red_dups_set = set(red_deck)-set(hand)
    red_candidates = list(no_red_dups_set)
    ret_hand = []
    old_score = (-1, [0,0,0,0,0])

    for item in red_candidates:
        hand_copy = hand[:]
        hand_copy.append(item)
        best_five = best_hand(hand_copy)
        if hand_rank(best_five) > old_score:
            old_score = hand_rank(best_five)
            ret_hand = best_five
    return ret_hand  #temp...

def black_joker(hand):
    "Hand has only a black joker"
    black_deck = [r+s for r in '23456789TJQKA' for s in 'CS']
    no_black_dups_set = set(black_deck)-set(hand)
    black_candidates = list(no_black_dups_set)
    ret_hand = []
    old_score = (-1, [0,0,0,0,0])

    for item in black_candidates:
        hand_copy = hand[:]
        hand_copy.append(item)
        best_five = best_hand(hand_copy)
        if hand_rank(best_five) > old_score:
            old_score = hand_rank(best_five)
            ret_hand = best_five
    return ret_hand  #temp...

def red_and_black_joker(hand):
    '''Hand has both a red and a black joker
       Input: a five card hand with no jokers'''
    red_deck = [r+s for r in '23456789TJQKA' for s in 'HD']
    black_deck = [r+s for r in '23456789TJQKA' for s in 'CS']
    no_red_dups_set = set(red_deck)-set(hand)
    red_candidates = list(no_red_dups_set)
    no_black_dups_set = set(black_deck)-set(hand)
    black_candidates = list(no_black_dups_set)
    ret_hand = []
    old_score = (-1, [0,0,0,0,0])

    for item in itertools.product(red_candidates, black_candidates):
        hand_copy = hand[:]
        hand_copy.extend(list(item))
        best_five = best_hand(hand_copy)
        if hand_rank(best_five) > old_score:
            old_score = hand_rank(best_five)
            ret_hand = best_five
    return ret_hand  #temp...

def best_hand(hand):
    "From a 7-card hand, return the best 5 card hand."
    possible_hands = []
    scores = []
    for deal in itertools.combinations(hand, 5):
        possible_hands.append(deal)
        scores.append(hand_rank(deal))
    best_score = max(scores)
    this_index = scores.index(best_score)
    return list(possible_hands[this_index])

def best_wild_hand(hand):
    "Try all values for jokers in all 5-card selections."
    branch = ''.join(hand).count('?')
    if branch == 0:
        return best_hand(hand)
    elif branch == 2:
        hand1 = [c for c in hand if c[0] != '?']  # make a 5 card hand w no jokers
        return red_and_black_joker(hand1)
    else:  # only one joker in hand
        if '?R' in hand:
            hand1 = [c for c in hand if c[0] != '?']
            return red_joker(hand1)
        else:
            hand1 = [c for c in hand if c[0] != '?']
            return black_joker(hand1)

def test_best_wild_hand():
    ''' test suite'''
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split()))
             == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_wild_hand passes'

# ------------------
# Provided Functions
#
# You may want to use some of the functions which
# you have already defined in the unit to write
# your best_hand function.

def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)

def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

def straight(ranks):
    """Return True if the ordered
    ranks form a 5-card straight."""
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def kind(n, ranks):
    """Return the first rank that this hand has
    exactly n-of-a-kind of. Return None if there
    is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None

def two_pair(ranks):
    """If there are two pair here, return the two
    ranks of the two pairs, else None."""
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None

print test_best_wild_hand()