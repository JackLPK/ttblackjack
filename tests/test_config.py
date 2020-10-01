import toml

from ttblackjack import CONFIG_FP


def test_config():
    config1 = toml.load(CONFIG_FP)
    config2 = {
        "decks": 2,
        "sleep": 1.0,
        "rounds": 0,
        "yes": True,
        "viewer": "cli",
        "debug": False,
        "players": [
            {"name": "player 1", "algorithm": "basic 1"},
            {"name": "player 2", "algorithm": "basic 2"},
            {"name": "player 3", "algorithm": "x-ray"},
            {"name": "USER", "algorithm": "user"},
            {"name": "dealer", "algorithm": "dealer"},
        ]
    }
    assert True  # Implement later
