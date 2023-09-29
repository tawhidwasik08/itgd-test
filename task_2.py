from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from faker import Faker
import random

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String)
    user_email = Column(String)
    posts = relationship("Post", backref="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"{self.user_id}:{self.user_name}"


class Post(Base):
    __tablename__ = "posts"
    post_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    post_title = Column(String)
    post_text = Column(String)

    def __repr__(self):
        return f"{self.post_id}:{self.post_title}, by: {self.user_id}"


# Define operations using the ORM
# Adding a User
def add_user(session, user_name, user_email):
    new_user = User(user_name=user_name, user_email=user_email)
    session.add(new_user)
    session.commit()
    return None


# Retrieving a User by ID
def get_user_by_id(session, user_id):
    return session.query(User).filter_by(user_id=user_id).first()


# Retrieving all Users
def get_all_users(session):
    return session.query(User).all()


# Updating a User
def update_user(session, user_id, new_name, new_email):
    user = get_user_by_id(session, user_id)
    if user:
        user.user_name = new_name
        user.user_email = new_email
        session.commit()
        return True
    return None


# Deleting a User by ID
def delete_user_by_id(session, user_id):
    user = get_user_by_id(session, user_id)
    if user:
        session.delete(user)
        session.commit()
        return True
    return None


# Adding a Post
def add_post(session, user_id, post_title, post_text):
    new_post = Post(user_id=user_id, post_title=post_title, post_text=post_text)
    session.add(new_post)
    session.commit()
    return None


# Retrieving a Post by ID
def get_post_by_id(session, post_id):
    return session.query(Post).filter_by(post_id=post_id).first()


# Retrieving all posts
def get_all_posts(session):
    return session.query(Post).all()


# Retrieving all Posts for a User
def get_all_posts_for_user(session, user_id):
    return session.query(Post).filter_by(user_id=user_id).all()


# Updating a Post
def update_post(session, post_id, new_title, new_text):
    post = get_post_by_id(session, post_id)
    if post:
        if new_title:
            post.post_title = new_title
        if new_text:
            post.post_text = new_text
        session.commit()
        return True
    return None


# Deleting a Post by ID
def delete_post_by_id(session, post_id):
    post = get_post_by_id(session, post_id)
    if post:
        session.delete(post)
        session.commit()
        return True
    return None


def print_option_screen():
    print()
    print(
        "+------------------- Task 2 Interactions ------------------+\n"
        "| 1. Add User                  2. Get User Info by ID      |\n"
        "| 3. Update User               4. Delete User              |\n"
        "| 5. Add Post                  6. Get Post Info            |\n"
        "| 7. Get All Posts For a User  8. Update Post              |\n"
        "| 9. Delete Post by ID         0. See current db tables    |\n"
        "+----------------------------------------------------------+"
    )
    print()
    return None


def generate_fake_data(session, user_count=5, post_count=10):
    fake = Faker()

    def generate_fake_user():
        return User(user_name=fake.user_name(), user_email=fake.email())

    def generate_fake_post(user_id):
        return Post(
            post_title=fake.sentence(), post_text=fake.paragraph(), user_id=user_id
        )

    for _ in range(user_count):
        user = generate_fake_user()
        add_user(session, user.user_name, user.user_email)

    user_ids = [user.user_id for user in session.query(User).all()]

    for _ in range(post_count):
        user_id = random.choice(user_ids)  # Select a random user's ID
        post = generate_fake_post(user_id)
        add_post(session, post.user_id, post.post_title, post.post_text)

    return None


def main():
    engine = create_engine("sqlite:///simple_db.sqlite")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # generate fake data if database base table user is empty
    if not session.query(User).first():
        generate_fake_data(session)
        print("Generated Fake Data")

    while True:
        print_option_screen()
        choice = input("Please enter your choice (0-10) [q to quit]: ")

        if choice == "q" or choice == "Q":
            print("Exiting..")
            break
        elif choice == "0":
            sub_choice = input(
                "Which data do you want to display?\n1. Users\n2. Posts\nEnter choice (1 or 2): "
            )
            if sub_choice == "1":
                users = get_all_users(session)
                for user in users:
                    print(
                        f"User ID: {user.user_id}, Name: {user.user_name}, Email: {user.user_email}"
                    )
            elif sub_choice == "2":
                posts = get_all_posts(session)
                for post in posts:
                    print(
                        f"Post ID: {post.post_id}, User ID: {post.user_id}, Title: {post.post_title}"
                    )
            else:
                print("Invalid choice.")

            input("Press any key to continue...")

        # add user
        elif choice == "1":
            user_name = input("Enter user name: ")
            user_email = input("Enter user email: ")
            if user_name and user_email:
                add_user(session, user_name, user_email)
                print("User added successfully!")
            else:
                print("Input can not be empty")

        # get user info
        elif choice == "2":
            user_id = int(input("Enter user ID: "))
            user = get_user_by_id(session, user_id)
            if user:
                print(
                    f"User ID: {user.user_id}, Name: {user.user_name}, Email: {user.user_email}"
                )
            else:
                print("User not found.")
            input("Press any key to continue...")

        # update user
        elif choice == "3":
            user_id = int(input("Enter user ID: "))
            new_name = input("Enter new user name: ")
            new_email = input("Enter new user email: ")
            if update_user(session, user_id, new_name, new_email):
                print("User updated successfully!")
            else:
                print("User not found")
            input("Press Enter to continue...")

        # delete user
        elif choice == "4":
            user_id = int(input("Enter user ID to delete: "))
            if delete_user_by_id(session, user_id):
                print("User deleted successfully!")
            else:
                print("No user found")
            input("Press Enter to continue...")

        # add post
        elif choice == "5":
            user_id = int(input("Enter user ID: "))
            user = get_user_by_id(session, user_id)
            if user:
                post_title = input("Enter post title: ")
                post_text = input("Enter post text: ")

                if (
                    post_title.strip() and post_text.strip()
                ):  # Both title and text are non-empty
                    add_post(session, user_id, post_title, post_text)
                    print("Post added successfully!")
                else:
                    print("Post title and text cannot be empty. No post added.")
            else:
                print(f"User with ID {user_id} does not exist.")

            input("Press Enter to continue...")

        # get post info
        elif choice == "6":
            post_id = int(input("Enter post ID: "))
            post = get_post_by_id(session, post_id)
            if post:
                print(
                    f"Post ID: {post.post_id}, User ID: {post.user_id}, Text: {post.post_text}"
                )
            else:
                print("Post not found.")
            input("Press Enter to continue...")

        # get all post for a user
        elif choice == "7":
            user_id = int(input("Enter user ID: "))
            user = get_user_by_id(session, user_id)
            if user:
                posts = get_all_posts_for_user(session, user_id)
                for post in posts:
                    print(
                        f"Post ID: {post.post_id}, User ID: {post.user_id}, Text: {post.post_text}"
                    )
            else:
                print(f"User with ID {user_id} does not exist.")

            input("Press Enter to continue...")

        # update post
        elif choice == "8":
            post_id = int(input("Enter post ID: "))
            new_title = input("Enter new post title: ")
            new_text = input("Enter new post text: ")
            if new_title or new_text:  # At least one of them is non-empty
                if update_post(session, post_id, new_title, new_text):
                    print("Post updated successfully!")
                else:
                    print("No Post Found")
            else:
                print("Both post title and post text are empty. No update performed.")

        # delete post
        elif choice == "9":
            post_id = int(input("Enter post ID to delete: "))
            if delete_post_by_id(session, post_id):
                print("Post deleted successfully!")
            else:
                print("No post found")
            input("Press Enter to continue...")

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
