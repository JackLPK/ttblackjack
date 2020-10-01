from ttblackjack import CLUB, DIAMOND, HEART, SPADE
from ttblackjack.card import Card
from ttblackjack.hand import Hand


def test_len():
    cards = [Card(CLUB, 'A'), Card(DIAMOND, '4'), Card(SPADE, '7')]
    h1 = Hand(cards)
    h2 = Hand()
    h2.append(Card(CLUB, 'A'))
    h2.append(Card(DIAMOND, '4'))
    h2.append(Card(SPADE, '7'))

    assert len(h1) == len(h2)


def test_empty():
    h1 = Hand()
    assert h1.is_empty


def test_points():
    h1 = Hand()
    h2 = Hand([Card(CLUB, '2'), Card(DIAMOND, '6')])
    h3 = Hand([Card(CLUB, '2'), Card(DIAMOND, 'A')])
    h4 = Hand([Card(CLUB, '2'), Card(DIAMOND, 'A'), Card(DIAMOND, 'A')])
    h5 = Hand([Card(CLUB, '2'), Card(DIAMOND, 'A'), Card(DIAMOND, 'A'), Card(DIAMOND, 'A')])

    assert h1.every_points() == [0, ]
    assert h2.every_points() == [8, ]
    assert h3.every_points() == [3, 13, ]
    assert h4.every_points() == [4, 14, 24, ]
    assert h5.every_points() == [5, 15, 25, 35]

    assert h1.e_max == 0
    assert h2.e_max == 8
    assert h3.e_max == 13
    assert h4.e_max == 14
    assert h5.e_max == 15


def test_busted():
    h0 = Hand()
    h1 = Hand([Card(CLUB, '8'), Card(DIAMOND, '8')])
    h2 = Hand([Card(CLUB, '8'), Card(DIAMOND, '8'), Card(DIAMOND, '8')])

    assert h0.is_busted is False
    assert h1.is_busted is False
    assert h2.is_busted is True


def test_blackjack():
    h1 = Hand([Card(CLUB, 'A'), Card(CLUB, '10')])
    h2 = Hand([Card(CLUB, '9'), Card(CLUB, '6'), Card(CLUB, '6')])

    h3 = Hand([Card(CLUB, '9'), Card(CLUB, '6'), Card(CLUB, '3')])

    assert h1.is_blackjack is True
    assert h2.is_blackjack is True
    assert h3.is_blackjack is False
