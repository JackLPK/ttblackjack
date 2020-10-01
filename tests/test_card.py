from ttblackjack import CLUB, DIAMOND, HEART, SPADE
from ttblackjack.card import Card


def test_str():

    c1 = Card(CLUB, 'A', )
    c2 = Card(CLUB, 'A', False)
    c3 = Card(CLUB, 'A', True)

    assert str(c1) == '(? ??)'
    assert str(c2) == '(? ??)'
    assert str(c3) == '(♣  A)'


def test_points():
    c1 = Card(CLUB, 'A', )
    c2 = Card(DIAMOND, '5', )
    c3 = Card(DIAMOND, 'K', )

    assert c1.points == [1, 11, ]
    assert c2.points == [5, ]
    assert c3.points == [10, ]
