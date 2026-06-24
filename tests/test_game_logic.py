from logic_utils import check_guess, new_game_state

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_lexicographic_bug_guess_6_secret_50():
    # Regression test for the high/low glitch.
    #
    # The old code stringified the secret on even attempts and compared
    # lexicographically, so "6" > "50" (because '6' > '5') wrongly returned
    # "Too High". Numerically 6 < 50, so the guess is too low.
    outcome, _ = check_guess(6, 50)
    assert outcome == "Too Low"


def test_hint_direction_points_toward_secret():
    # The hint must tell the player which way to move their NEXT guess.
    # Guess below the secret -> go higher; guess above -> go lower.
    _, low_message = check_guess(2, 36)
    assert low_message == "📈 Go HIGHER!"

    _, high_message = check_guess(68, 36)
    assert high_message == "📉 Go LOWER!"


def test_new_game_resets_status_to_playing():
    # Regression test for the "New Game doesn't restart" bug.
    #
    # The old "New Game" block reset attempts and secret but forgot to reset
    # status. So after a finished game (status == "won" or "lost"), starting a
    # new game left status stuck on the finished value, and the guard in app.py
    # immediately blocked play with "You already won / Game over."
    #
    # A fresh game must always be back in the "playing" state.
    assert new_game_state(1, 100)["status"] == "playing"


def test_new_game_fully_resets_progress():
    # New Game should be a genuine full reset, not a partial one.
    state = new_game_state(1, 100)
    assert state["attempts"] == 1
    assert state["score"] == 0
    assert state["history"] == []


def test_new_game_secret_respects_difficulty_range():
    # The secret must come from the difficulty's range, not a hardcoded 1-100.
    for _ in range(50):
        secret = new_game_state(1, 20)["secret"]
        assert 1 <= secret <= 20
