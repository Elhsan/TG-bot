import random

# games.py

# Example: Define different types of casinos
casinos = ["Casino A", "Casino B", "Casino C"]

# Example: Define jobs that earn coins
jobs = ["Job A", "Job B", "Job C"]

# Symbols and their payout multipliers with emojis
symbols = {
    "🍌": 2,      # Banana
    "🍆": 1.5,    # Eggplant
    "❌": 0,      # Cross
    "🍒": 1       # Cherry
}

def play_casino(user_id, casino_index, bet_amount):
    """Simulate playing at a casino with symbols and bet amount."""
    if user_id in user_coins:
        if user_coins[user_id]["balance"] >= bet_amount:
            user_coins[user_id]["balance"] -= bet_amount  # Deduct bet amount from balance

            # Example: Simulate spinning the reels (randomly generate symbols)
            reel1 = random.choice(list(symbols.keys()))
            reel2 = random.choice(list(symbols.keys()))
            reel3 = random.choice(list(symbols.keys()))

            # Example: Calculate winnings based on the combination
            if reel1 == reel2 == reel3:
                winnings = bet_amount * symbols[reel1]  # Example: Amount won based on symbol multiplier
                user_coins[user_id]["balance"] += winnings
                return f"You won {winnings} coins at {casinos[casino_index]} with {reel1} {reel2} {reel3}!"
            else:
                return f"No win this time at {casinos[casino_index]} with {reel1} {reel2} {reel3}. Try again!"
        else:
            return "Insufficient funds for this bet."
    else:
        return "Insufficient funds."

def perform_job(user_id, job_index):
    """Simulate performing a job."""
    if user_id in user_coins:
        # Example: Logic to earn coins from jobs
        earnings = 50  # Example: Amount earned
        user_coins[user_id]["balance"] += earnings
        return f"You earned {earnings} coins from {jobs[job_index]}"
    else:
        return "Insufficient funds."
