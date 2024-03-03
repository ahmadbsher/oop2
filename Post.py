# Post.py

class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.likes = []
        self.comments = []

    def like(self, user):
        if user != self.author and user not in self.likes:
            self.likes.append(user)
            user.notify(self, "like")

           

    def comment(self, user, text):
        if user != self.author:
            self.comments.append((user, text))
            user.notify(self, "comment",text)

           

    def display_post_info(self):
        print(f"Post by {self.author.username}:")
        print(self.content)
        print("Likes:", len(self.likes))
        print("Comments:")
        for commenter, comment_text in self.comments:
            print(f"{commenter.username}: {comment_text}")
# Post.py

class TextPost(Post):
    def __init__(self, content, author):
        super().__init__(content, author)

    # Additional methods for TextPost if needed...

class ImagePost(Post):
    def __init__(self, image_location, author):
        super().__init__("Image post", author)
        self.image_location = image_location

    def display_post_info(self):
        super().display_post_info()
        

    def display(self):
        print("Shows picture")

class SalePost(Post):
    def __init__(self, description, price, pickup_location, seller):
        super().__init__("Sale post", seller)
        self.description = description
        self.price = price
        self.pickup_location = pickup_location
        self.sold = False
        self.seller = seller 
        self.available = True

    def update_price(self, new_price, password):
        if not self.sold and password == self.seller.password:
            self.price = new_price
            print(f"The price has been updated to {new_price} shekels.")

    def discount(self, discount_percentage, password):
        if not self.sold and password == self.seller.password:
            discounted_price = self.price * (1 - discount_percentage / 100)
            print(f"Discount on {self.seller.username} product! the new price is: {discounted_price}")


    def mark_as_sold(self, password):
        if password == self.seller.password:
            if not self.sold:
                self.sold = True
                self.available = False  # Update available attribute when product is sold
                print(f"{self.seller.username}'s product is sold")
            else:
                print("Product is already sold.")
        else:
            print("Incorrect password.")

    def display_post_info(self):
        super().display_post_info()
        print("Description:", self.description)
        print("Price:", self.price, "shekels")
        print("Pickup location:", self.pickup_location)
        print("Status: Sold" if self.sold else "Status: Available")
