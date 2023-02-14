class User:

    def __init__(self, user_id, username):
        self._user_id = str(user_id).zfill(3)
        self._username = username
        self._followers = 0
        self._following = 0

    def follow(self, user):
        user.add_follower()
        self._following += 1

    def add_follower(self):
        self._followers += 1

    def get_user_id(self):
        return self._user_id

    def get_username(self):
        return self._username

    def get_username_backwards(self):
        return self._username[::-1]

    def get_followers(self):
        return self._followers

    def get_following(self):
        return self._following
