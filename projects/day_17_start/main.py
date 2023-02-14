from user import User

users = {0: User(1, "Marek"),
         1: User(2, "Ema")}

users[0].follow(users[1])

for i in users:
    user = users[i]
    print(f"User {user.get_username()} has {user.get_followers()} followers and is following {user.get_following()} people!")


