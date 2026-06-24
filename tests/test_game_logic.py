from logic_utils import check_guess, update_score


# ---------- Hint tests (check_guess) ----------

def test_winning_guess():
    # Secret 50, guess 50 -> a win.
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_guess_too_high_tells_you_to_go_lower():
    # Guess is bigger than the secret -> "Too High", advise LOWER.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_too_low_tells_you_to_go_higher():
    # Guess is smaller than the secret -> "Too Low", advise HIGHER.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


# ---------- Score tests (update_score) ----------

def test_win_awards_more_points_when_faster():
    # Winning on an earlier attempt should be worth more than a later one.
    early = update_score(0, "Win", attempt_number=1)
    late = update_score(0, "Win", attempt_number=4)
    assert early > late


def test_win_points_never_below_floor():
    # No matter how many attempts, a win is worth at least 10 points.
    assert update_score(0, "Win", attempt_number=20) == 10


def test_too_high_always_subtracts_five():
    # Should subtract 5 regardless of whether the attempt number is odd or even.
    assert update_score(100, "Too High", attempt_number=2) == 95  # even
    assert update_score(100, "Too High", attempt_number=3) == 95  # odd


def test_too_low_subtracts_five():
    assert update_score(100, "Too Low", attempt_number=2) == 95


def test_wrong_directions_cost_the_same():
    # A wrong guess costs 5 whether it's too high or too low.
    high = update_score(100, "Too High", attempt_number=2)
    low = update_score(100, "Too Low", attempt_number=2)
    assert high == low


def test_unknown_outcome_leaves_score_unchanged():
    assert update_score(42, "Something Else", attempt_number=1) == 42
