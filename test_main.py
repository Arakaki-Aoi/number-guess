from main import in_range, guess_hint,input_and_validate,play_game

# Game settings
MIN_NUMBER = 1
MAX_NUMBER = 10
MAX_ATTEMPTS = 3

def test_in_range():
    assert in_range(0) is False
    assert in_range(1) is True
    assert in_range(10) is True
    assert in_range(11) is False

def test_guess_hint():
    assert guess_hint(1, 2) == "Too high!"
    assert guess_hint(2, 1) == "Too low!"

def test_input_and_validate_valid_input(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _:"1")
    assert input_and_validate() == 1

def test_input_and_validate_retry_until_valid_integer(monkeypatch):
    input_list = iter(["a", "b", "1"])
    monkeypatch.setattr("builtins.input", lambda _:next(input_list))
    assert input_and_validate() == 1

def test_input_and_validate_retry_until_in_range(monkeypatch, capsys):
    input_list = iter(["11", "1"])
    monkeypatch.setattr("builtins.input", lambda _:next(input_list))
    result = input_and_validate()
    captured = capsys.readouterr()
    assert result == 1
    assert "Please enter a number between 1 and 10." in captured.out

def test_play_game_correct_first_try(monkeypatch, capsys):
    monkeypatch.setattr("main.random.randint", lambda a, b :1)
    monkeypatch.setattr("main.input_and_validate", lambda :1)
    play_game()
    captured = capsys.readouterr()
    assert "Correct! Great job!" in captured.out

def test_play_game_correct_second_try(monkeypatch, capsys):
    input_list = iter(["1", "2"])
    monkeypatch.setattr("main.random.randint", lambda a, b :2)
    monkeypatch.setattr("builtins.input", lambda _:next(input_list))
    play_game()
    captured = capsys.readouterr()
    assert "Too low! Try again.\nYou have 2 attempts left." in captured.out
    assert "Correct! Great job!" in captured.out

def test_play_game_correct_third_try(monkeypatch, capsys):
    input_list = iter(["1", "2", "3"])
    monkeypatch.setattr("main.random.randint", lambda a, b :3)
    monkeypatch.setattr("builtins.input", lambda _:next(input_list))
    play_game()
    captured = capsys.readouterr()
    assert "Too low! Try again.\nYou have 1 attempt left." in captured.out
    assert "Correct! Great job!" in captured.out

def test_play_game_correct_game_over(monkeypatch, capsys):
    input_list = iter(["1", "2", "3"])
    monkeypatch.setattr("main.random.randint", lambda a, b :4)
    monkeypatch.setattr("builtins.input", lambda _:next(input_list))
    play_game()
    captured = capsys.readouterr()
    assert "Game over! The number was" in captured.out