# coins.py

# Dictionary to store user coin details
user_coins = {}

def update_coin_balance(user_id, balance):
    """Update user's coin balance."""
    if user_id in user_coins:
        user_coins[user_id]["balance"] = balance
    else:
        user_coins[user_id] = {
            "balance": balance,
            "max_coins": 1000000,  # Example: maximum coins user can hold
            "transfer_fee": 0.1  # Example: transfer fee as a percentage
        }

def get_coin_balance(user_id):
    """Retrieve user's coin balance."""
    return user_coins.get(user_id, {}).get("balance", 0)

def deduct_coins(user_id, amount):
    """Deduct coins from user's balance."""
    if user_id in user_coins:
        if user_coins[user_id]["balance"] >= amount:
            user_coins[user_id]["balance"] -= amount
            return True
        else:
            return False
    else:
        return False
