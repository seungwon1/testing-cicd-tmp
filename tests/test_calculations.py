import pytest
from app.calculations import add, subtract, multiply, divide, BankAccount, InSufficientFunds

@pytest.fixture
def zero_bank_account():
    print("creating empty bank account")
    return BankAccount()

@pytest.fixture
def bank_account():
    print("creating bank account with 50")
    return BankAccount(50)

@pytest.mark.parametrize("num1, num2, expected", [
    (5, 3, 8),
    (6, 1, 7),
    (2, 1, 3)
])
def test_add(num1, num2, expected):
    assert expected == add(num1, num2)


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(5, 3) == 15


def test_divide():
    assert divide(6, 3) == 2

def test_bank_set_initial_amount(bank_account):
    assert bank_account.balance == 50

def test_bank_default_amount(zero_bank_account):
    assert zero_bank_account.balance == 0

def test_bank_deposit(bank_account):
    bank_account.deposit(20)
    assert bank_account.balance == 70

def test_bank_withdraw(bank_account):
    bank_account.withdraw(50)
    assert bank_account.balance == 0

def test_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 55

@pytest.mark.parametrize("deposited, withdrew, expected", [
    (50, 30, 20),
    (60, 10, 50),
    (120, 20, 100),
])
def test_bank_transaction(zero_bank_account, deposited, withdrew, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected

def test_insufficient_funds(bank_account):
    with pytest.raises(InSufficientFunds):
        bank_account.withdraw(220)


