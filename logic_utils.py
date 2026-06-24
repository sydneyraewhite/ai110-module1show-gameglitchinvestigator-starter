def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def new_game_state(low: int, high: int, secret=None):
    """
    Return a fresh game-state dict for starting a new game.

    Every field that the game guard depends on is reset here. In particular,
    `status` is reset to "playing" — the bug was that the old "New Game" block
    reset attempts/secret but forgot status, so a finished game ("won"/"lost")
    stayed finished and immediately blocked play on the next round.

    `secret` may be passed in for deterministic tests; otherwise it is drawn
    from the inclusive [low, high] range for the current difficulty.
    """
    import random

    return {
        "secret": secret if secret is not None else random.randint(low, high),
        "attempts": 1,
        "score": 0,
        "status": "playing",
        "history": [],
    }


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    # Fix 1 (Claude + user): dropped the old `except TypeError` fallback that
    # compared the guess against a stringified secret lexicographically
    # ("6" > "50"), which produced the wrong outcome. Both values are ints now,
    # so this is a plain numeric comparison.
    # Fix 2 (found by user play-testing secret=36): the hint messages were
    # paired with the wrong direction. A guess that's too high now points the
    # player LOWER, and one that's too low points HIGHER.
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
