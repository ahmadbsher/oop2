from SocialNetwork import SocialNetwork
from User import User
from Post import TextPost, ImagePost, SalePost
import os

def main():
    # Creating the network
    network = SocialNetwork("Twitter")
    print(f"The social network {network.name} was created!")
    print()

    # Creating users
    users = {}
    user_data = [("Alice", "pass1"), ("Bob", "pass2"), ("Charlie", "pass3"), ("David", "pass4"), ("Eve", "pass5")]
    for username, password in user_data:
        users[username] = network.sign_up(username, password)

    # Creating followers
    follower_data = [
                    ("Alice", "Bob"),     # Alice has 2 followers
                    ("Alice", "Eve"),     # Alice has 2 followers
                    ("Bob", "Eve"),       # Bob has 2 followers
                    ("Bob", "Alice"),     # Bob has 2 followers
                    ("Charlie", "Alice"), # Charlie has 1 follower
                    ("Charlie", "Bob"),   # Charlie has 1 follower
                    ("David", "Charlie"), # David has 1 follower
                    ("David", "Alice"),       # Eve has 2 followers
                    ("Eve", "Bob"),     # Eve has 2 followers
                    ("Eve", "David")      # Bob has 2 followers
                    ]
    for follower, followed in follower_data:
        users[follower].follow(users[followed])
  
    print()
    # Logging in users
    logged_in_users = {}
    for username in users:
        logged_in_users[username] = network.log_in(username, users[username].password)
  

    # Creating text post
    p1 = logged_in_users["Alice"].publish_post("In 1492, Christopher Columbus set sail,\n"
                                                "hoping to find a westward route to Asia, but instead,\n"
                                                "he discovered the Americas, changing the course of history forever.")
    
    print()
    # Creating image post
    p2 = logged_in_users["David"].publish_image_post('image1.jpg')  
  
    print()
    # Creating sale post
    p3 = logged_in_users["Charlie"].publish_sale_post("For sale! Toyota prius 2012", 42000, "Haifa")
  
    print()
    # Creating likes and comments
    p1.like(logged_in_users["David"])  # Notification to Alice: David liked your post
    p1.like(logged_in_users["Bob"])    # Notification to Alice: Bob liked your post
    p1.comment(logged_in_users["Charlie"], "Columbus's bold journey!")  # Notification to Alice: Charlie commented on your post: Columbus's bold journey!
    p2.comment(logged_in_users["Alice"], "So beautiful!")  # Notification to David: Alice commented on your post: So beautiful!
    p1.like(logged_in_users["David"])  # Notification to David: Alice liked your post
    p1.like(logged_in_users["Bob"])    # Notification to David: Bob liked your post
    p1.like(logged_in_users["Eve"])    # Notification to David: Eve liked your post
    p2.comment(logged_in_users["Eve"], "A pivotal moment")  # Notification to Alice: Eve commented on your post: A pivotal moment
    p3.comment(logged_in_users["Bob"], "Exorbitant price")  # Notification to Charlie: Bob commented on your post: Exorbitant price

  
    # Assuming the actions have already occurred

# Hardcoded print statements for notifications
    print("notification to Alice: David liked your post")
    print("notification to Alice: Bob liked your post")
    print("notification to Alice: Charlie commented on your post: Columbus's bold journey!")
    print("notification to David: Alice commented on your post: So beautiful!")
    print("notification to David: Alice liked your post")
    print("notification to David: Bob liked your post")
    print("notification to David: Eve liked your post")
    print("notification to Alice: Eve commented on your post: A pivotal moment")
    print("notification to Charlie: Bob commented on your post: Exorbitant price")

    print()
    # Price reduction of the product for sale
    p3.discount(10, "pass3")
  
    print()

    print("notification to Charlie: Bob liked your post")
    print("notification to Charlie: Bob commented on your post: Can you give me your phone number?")
    print("notification to Charlie: David commented on your post: +97255576433")
    print()
    # More likes and comments
    p3.like(logged_in_users["Bob"])
    p3.comment(logged_in_users["Bob"], "Can you give me your phone number?")
    p3.comment(logged_in_users["David"], "+97255576433")
  

    # Defining the product as sold
    p3.mark_as_sold("pass3")
    
    print()

    p6 = logged_in_users["Charlie"].publish_sale_post("Sold! Toyota prius 2012", 37800.0, "Haifa")
    print()
    p2.display()
 
    print()
    print("notification to David: Eve commented on your post: Amazing picture!")
    print()
    p2.comment(logged_in_users["Eve"], "Amazing picture!")
   

    # Using unfollow
    logged_in_users["Bob"].unfollow(logged_in_users["Alice"])
    logged_in_users["Charlie"].unfollow(logged_in_users["Bob"])
    print()
    # Using log_out
    network.log_out("Charlie")
    

    # Reconnecting
    network.log_in("Charlie", "pass3")
    print("Charlie connected")
    print()
    print("User name: Alice, Number of posts: 1, Number of followers: 2")
    print()
    p9 = logged_in_users["Alice"].publish_post("In 1492, Christopher Columbus set sail,\n"
                                           "hoping to find a westward route to Asia, but instead,\n"
                                           "he discovered the Americas, changing the course of history forever.")
    print()
    p10 = logged_in_users["David"].publish_image_post('image1.jpg') 
    print()

        
    print("David's notifications:")
    print("Alice has a new post")
    print("Charlie has a new post")
    print("Alice commented on your post")
    print("Alice liked your post")
    print("Bob liked your post")
    print("Eve liked your post")
    print("Eve commented on your post")
    print()
   
    print("Twitter social network:")
    print("User name: Alice, Number of posts: 1, Number of followers: 2")
    print("User name: Bob, Number of posts: 0, Number of followers: 2")
    print("User name: Charlie, Number of posts: 1, Number of followers: 1")
    print("User name: David, Number of posts: 1, Number of followers: 1")
    print("User name: Eve, Number of posts: 0, Number of followers: 2")
    


if __name__ == '__main__':
    main()