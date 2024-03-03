# User.py
from Post import TextPost,SalePost,ImagePost
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.logged_in = False
        self.followers = []
        self.posts = []
        self.notifications = []

    def follow(self, other_user):
        if other_user != self and other_user not in self.followers:
            self.followers.append(other_user)
            print(f"{self.username} started following {other_user.username}")

    def unfollow(self, other_user):
        if other_user in self.followers:
            self.followers.remove(other_user)
            print(f"{self.username} unfollowed {other_user.username}")

    def publish_post(self, post_content):
        if self.logged_in:
            post = TextPost(post_content, self)
            self.posts.append(post)
            print(f"{self.username} published a post.")
            for follower in self.followers:
                follower.notify(post)
            return post
        else:
            print("You need to log in to publish a post.")
    def publish_image_post(self, image_location):
        if self.logged_in:
            post = ImagePost(image_location, self)
            self.posts.append(post)
            print(f"{self.username} published an image post.")
            for follower in self.followers:
                follower.notify(post)
            return post
        else:
            print("You need to log in to publish a post.")
    def publish_sale_post(self, description, price, pickup_location):
        if self.logged_in:
            post = SalePost(description, price, pickup_location, self)
            self.posts.append(post)
            print(f"{self.username} published a post.")
            for follower in self.followers:
                follower.notify(post)
            return post
        else:
            print("You need to log in to publish a post.")

    def notify(self, post):
        if post.author != self:
            self.notifications.append(f"Notification: {post.author.username} posted: {post.content}")

    def display_notifications(self):
        if self.notifications:
            print(f"{self.username}'s notifications:")
            for notification in self.notifications:
                print(notification)
        else:
            print(f"No notifications for {self.username}")

    def __str__(self):
        return f"User name: {self.username}, Number of posts: {len(self.posts)}, Number of followers: {len(self.followers)}"
