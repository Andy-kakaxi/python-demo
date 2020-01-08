# -*- coding:utf-8 -*-
# 流畅的python第一部分代码分析

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()
# print(deck[0])
# print(len(deck))
# print(deck[12::13])
# reversed():返回一个反转的迭代器
# 迭代通常是隐式的，例如一个集合类型没有实现__contains__方法，in运算符就会按顺序做一次迭代搜索

# for card in reversed(deck):
#     print(card)


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)


