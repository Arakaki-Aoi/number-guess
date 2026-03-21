import main
import pytest

@pytest.mark.parametrize("value, expected", [
    (main.MIN_NUMBER - 1, False),
    (main.MIN_NUMBER, False),
    (main.MAX_NUMBER, True),
    (main.MAX_NUMBER + 1, False),
])
def test_in_range(value, expected):
    assert main.in_range(value) is expected

@pytest.mark.parametrize("answer, guess, expected", [
    (1, 2, "Too high!"),
    (2, 1, "Too low!"),
])
def test_guess_hint(answer, guess, expected):
    assert main.guess_hint(answer, guess) == expected

def test_input_and_validate_valid_input(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "1")
    assert main.input_and_validate() == 1

def test_input_and_validate_retry_until_valid_integer(monkeypatch, capsys):
    input_list = iter(["a", "b", "1"])
    monkeypatch.setattr("builtins.input", lambda _: next(input_list))
    result = main.input_and_validate()
    captured = capsys.readouterr()
    assert result == 1
    assert "Please enter a valid integer." in captured.out

def test_input_and_validate_retry_until_in_range(monkeypatch, capsys):
    input_list = iter(["11", "1"])
    monkeypatch.setattr("builtins.input", lambda _: next(input_list))
    result = main.input_and_validate()
    captured = capsys.readouterr()
    assert result == 1
    assert "Please enter a number between 1 and 10." in captured.out

def test_play_game_correct_first_try(monkeypatch, capsys):
    monkeypatch.setattr("main.random.randint", lambda a, b: 1)
    monkeypatch.setattr("main.input_and_validate", lambda: 1)
    main.play_game()
    captured = capsys.readouterr()
    assert "Correct! Great job!" in captured.out

def test_play_game_correct_second_try(monkeypatch, capsys):
    input_list = iter(["1", "2"])
    monkeypatch.setattr("main.random.randint", lambda a, b: 2)
    monkeypatch.setattr("builtins.input", lambda _: next(input_list))
    main.play_game()
    captured = capsys.readouterr()
    assert "Too low! Try again.\nYou have 2 attempts left." in captured.out
    assert "Correct! Great job!" in captured.out

def test_play_game_correct_third_try(monkeypatch, capsys):
    input_list = iter(["1", "2", "3"])
    monkeypatch.setattr("main.random.randint", lambda a, b: 3)
    monkeypatch.setattr("builtins.input", lambda _: next(input_list))
    main.play_game()
    captured = capsys.readouterr()
    assert "Too low! Try again.\nYou have 2 attempts left." in captured.out
    assert "Too low! Try again.\nYou have 1 attempt left." in captured.out
    assert "Correct! Great job!" in captured.out

def test_play_game_game_over(monkeypatch, capsys):
    input_list = iter(["1", "2", "3"])
    monkeypatch.setattr("main.random.randint", lambda a, b: 4)
    monkeypatch.setattr("builtins.input", lambda _: next(input_list))
    main.play_game()
    captured = capsys.readouterr()
    assert "Game over! The number was" in captured.out