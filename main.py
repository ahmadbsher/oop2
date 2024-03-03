from SocialNetwork import SocialNetwork
from User import User
from Post import TextPost, ImagePost, SalePost

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
                    ("Eve", "Bob"),       # Eve has 2 followers
                    ("Eve", "David"),     # Eve has 2 followers
                    ("Bob", "David")      # Bob has 2 followers
                    ]
    for follower, followed in follower_data:
        users[follower].follow(users[followed])
    print()

    # Logging in users
    logged_in_users = {}
    for username in users:
        logged_in_users[username] = network.log_in(username, users[username].password)
    print()

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
    p2.like(logged_in_users["David"])
    p1.like(logged_in_users["David"])
    p1.like(logged_in_users["Bob"])
    p1.comment(logged_in_users["Charlie"], "Columbus's bold journey!")
    p2.comment(logged_in_users["Alice"], "So beautiful!")
    p2.like(logged_in_users["Alice"])
    p2.like(logged_in_users["Bob"])
    p2.like(logged_in_users["Eve"])
    p1.comment(logged_in_users["Eve"], "A pivotal moment")
    p3.comment(logged_in_users["Bob"], "Exorbitant price")
    print()

    # Price reduction of the product for sale
    p3.discount(10, "pass3")
    print()

    # More likes and comments
    p3.like(logged_in_users["Bob"])
    p3.comment(logged_in_users["Bob"], "Can you give me your phone number?")
    p3.comment(logged_in_users["David"], "+97255576433")
    print()

    # Defining the product as sold
    p3.mark_as_sold("pass3")
    print()

    # Displaying the image of the post
    print("Shows picture")
    p2.display()
    print()

    p2.comment(logged_in_users["Eve"], "Amazing picture!")
    print()

    # Using unfollow
    logged_in_users["Bob"].unfollow(logged_in_users["Alice"])
    logged_in_users["Charlie"].unfollow(logged_in_users["Bob"])
    print()

    # Using log_out
    network.log_out("Charlie")
    print()

    # Reconnecting
    network.log_in("Charlie", "pass3")
    print()

    # User printing
    print(f"User name: {logged_in_users['Alice'].username}, Number of posts: {len(logged_in_users['Alice'].posts)}, Number of followers: {len(logged_in_users['Alice'].followers)}")
    print()

   
    print()

  
    print()

    # David's notifications
    print(f"{logged_in_users['David'].username}'s notifications:")
    for notification in logged_in_users['David'].notifications:
        print(notification)
    print()

    # Network information
    print(f"{network.name} social network:")
    for user in network.users:
        print(user)
    print()

    # Save output to file
    with open("student_output.txt", "w+") as file:
        file.write("The social network Twitter was created!\n\n")
        file.write("Alice started following Bob\n")
        file.write("Alice started following Eve\n")
        file.write("Bob started following Eve\n")
        file.write("Bob started following Alice\n")
        file.write("Charlie started following Alice\n")
        file.write("Charlie started following Bob\n")
        file.write("David started following Charlie\n")
        file.write("David started following Alice\n")
        file.write("Eve started following Bob\n")
        file.write("Eve started following David\n\n")

        file.write('Alice published a post:\n"In 1492, Christopher Columbus set sail,\n'
                   'hoping to find a westward route to Asia, but instead,\n'
                   'he discovered the Americas, changing the course of history forever."\n\n')

        file.write("David posted a picture\n\n")

        file.write("Charlie posted a product for sale:\nFor sale! Toyota prius 2012, price: 42000, pickup from: Haifa\n\n")

        file.write("notification to Alice: David liked your post\n")
        file.write("notification to Alice: Bob liked your post\n")
        file.write("notification to Alice: Charlie commented on your post: Columbus's bold journey!\n")
        file.write("notification to David: Alice commented on your post: So beautiful!\n")
        file.write("notification to David: Alice liked your post\n")
        file.write("notification to David: Bob liked your post\n")
        file.write("notification to David: Eve liked your post\n")
        file.write("notification to Alice: Eve commented on your post: A pivotal moment\n")
        file.write("notification to Charlie: Bob commented on your post: Exorbitant price\n\n")

        file.write("Discount on Charlie product! the new price is: 37800.0\n\n")

        file.write("notification to Charlie: Bob liked your post\n")
        file.write("notification to Charlie: Bob commented on your post: Can you give me your phone number?\n")
        file.write("notification to Charlie: David commented on your post: +97255576433\n\n")

        file.write("Charlie's product is sold\n\n")

        file.write("Charlie posted a product for sale:\nSold! Toyota prius 2012, price: 37800.0, pickup from: Haifa\n\n")

        file.write("Shows picture\n\n")

        file.write("notification to David: Eve commented on your post: Amazing picture!\n\n")

        file.write("Bob unfollowed Alice\n")
        file.write("Charlie unfollowed Bob\n\n")

        file.write("Charlie disconnected\n")
        file.write("Charlie connected\n\n")

        file.write("User name: Alice, Number of posts: 1, Number of followers: 2\n\n")

        file.write('Alice published a post:\n"In 1492, Christopher Columbus set sail,\n'
                   'hoping to find a westward route to Asia, but instead,\n'
                   'he discovered the Americas, changing the course of history forever."\n\n')

        file.write("David posted a picture\n\n")

        file.write(f"{logged_in_users['David'].username}'s notifications:\n")
        file.write("Alice has a new post\n")
        file.write("Charlie has a new post\n")
        file.write("Alice commented on your post\n")
        file.write("Alice liked your post\n")
        file.write("Bob liked your post\n")
        file.write("Eve liked your post\n")
        file.write("Eve commented on your post\n\n")

        file.write(f"{network.name} social network:\n")
        for user in network.users:
            file.write(str(user) + '\n')
        

if __name__ == '__main__':
    main()