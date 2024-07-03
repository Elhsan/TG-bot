import time

# Dictionary to store user profiles
user_profiles = {}

def create_or_update_profile(user_id, first_name):
    """Create or update a user profile."""
    if user_id not in user_profiles:
        user_profiles[user_id] = {
            "name": first_name,
            "first_appearance": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
            "coins": 0,
            "married": False
        }
    else:
        # If the profile exists, we update only the name to handle name changes
        user_profiles[user_id]["name"] = first_name

def get_profile(user_id):
    """Retrieve a user profile."""
    profile = user_profiles.get(user_id, None)
    if profile:
        married_status = "💍 в браке" if profile["married"] else "❌ не в браке"
        return (
            f"👤 Имя: {profile['name']}\n"
            f"📅 Первое появление: {profile['first_appearance']}\n"
            f"💰 Монет: {profile['coins']}\n"
            f"👫 Семейное положение: {married_status}"
        )
    else:
        return "Нет данных профиля."

def add_coins(user_id, amount):
    """Add coins to a user's profile."""
    if user_id in user_profiles:
        user_profiles[user_id]["coins"] += amount
    else:
        return "Профиль не найден."

def set_married_status(user_id, status):
    """Set the married status of a user's profile."""
    if user_id in user_profiles:
        user_profiles[user_id]["married"] = status
    else:
        return "Профиль не найден."
