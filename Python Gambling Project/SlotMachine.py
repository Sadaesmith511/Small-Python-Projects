import random

# Constants for the game's settings
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

# Symbol distribution and values
symbols_count = {"A": 2, "B": 4, "C": 6, "D": 8}
symbol_value = {"A": 5, "B": 4, "C": 3, "D": 2}

def check_win(columns, lines, bet, values):
    """
    Calculate the winnings based on the slot results, bet lines, and bet amount.

    columns: The result of the slot spin - a list of columns with symbols.
    lines: Number of lines the player has bet on.
    bet: The amount bet on each line.
    values: The value/multiplier for each symbol.

    Returns the total winnings and the winning lines.
    """
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_spin(rows, cols, symbols):
    """
    Generate a random spin for the slot machine.

    rows, cols: Dimensions of the slot machine.
    symbols: A dictionary with symbols and their frequency.

    Returns a list of columns representing the slot spin.
    """
    all_symbols = [symbol for symbol, count in symbols.items() for _ in range(count)]
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def printing_slot_machine(columns):
    """
    Print the slot machine spin in a readable format.

    columns: The result of the slot spin to be printed.
    """
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            print(column[row], end=" | " if i != len(columns) - 1 else "")
        print()

def deposit():
    """
    Handle the deposit process for the player.

    Returns the amount deposited by the player.
    """
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit() and int(amount) > 0:
            return int(amount)
        print("Please enter a valid amount greater than zero.")

def get_number_of_lines():
    """
    Ask the player for the number of lines they want to bet on.

    Returns the number of lines chosen by the player.
    """
    while True:
        lines = input(f"How many lines would you like to bet on? (1-{MAX_LINES})? ")
        if lines.isdigit() and 1 <= int(lines) <= MAX_LINES:
            return int(lines)
        print("Please enter a valid number of lines.")

def get_bet():
    """
    Ask the player for the amount they want to bet on each line.

    Returns the bet amount.
    """
    while True:
        amount = input(f"What would you like to bet on each line? ${MIN_BET}-${MAX_BET} ")
        if amount.isdigit() and MIN_BET <= int(amount) <= MAX_BET:
            return int(amount)
        print(f"Please enter a valid bet amount between ${MIN_BET} and ${MAX_BET}.")

def spin(balance):
    """
    Perform one spin of the slot machine.

    balance: The player's current balance.

    Returns the net change to the player's balance after the spin.
    """
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You don't have enough money to place this bet. Your balance is ${balance}.")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet: ${total_bet}.")
    
    slots = get_slot_spin(ROWS, COLS, symbols_count)
    printing_slot_machine(slots)
    winnings, winning_lines = check_win(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print("You won on lines:", *winning_lines)
    
    return winnings - total_bet


def main():
    """
    Main function to handle the game flow.
    """
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        spin_input = input("Press enter to play (q to quit)")
        if spin_input == "q":
            break
        balance += spin(balance)
    print(f"You left with {balance}")


main()


