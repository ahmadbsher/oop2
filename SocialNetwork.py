# SocialNetwork.py
from User import User 
class SocialNetwork:
    _instance = None

    def __new__(cls, name):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.name = name
            cls._instance.users = []
        return cls._instance

    def sign_up(self, username, password):
        if not (4 <= len(password) <= 8):
            print("Password must be between 4 and 8 characters long.")
            return None

        for user in self.users:
            if user.username == username:
                print("Username already exists.")
                return None

        new_user = User(username, password)
        self.users.append(new_user)
        return new_user

    def log_in(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                user.logged_in = True
                
                return user

        return None

    def log_out(self, username):
        for user in self.users:
            if user.username == username:
                print(username, "disconnected")
                user.logged_in = False
                return

        print("User not found.")

    def display_network(self):
        print("Network:", self.name)
        for user in self.users:
            print("- Username:", user.username)

    def get_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

    def display_user_details(self, username):
        user = self.get_user_by_username(username)
        if user:
            print("User:", user.username)
            print("- Number of followers:", len(user.followers))
            print("- Number of posts:", len(user.posts))
        else:
            print("User not found.")

    def display_notifications(self, username):
        user = self.get_user_by_username(username)
        if user:
            print("Notifications for", username + ":")
            for notification in user.notifications:
                print("-", notification)
        else:
            print("User not found.")

    
