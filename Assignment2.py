import os

# Populate quiz.txt with 10 DSA questions
def populate_quiz_file():
    """Creates a quiz file with 10 DSA questions."""
    questions = [
        "What is the time complexity of inserting an element into a Binary Search Tree (average case)?;O(log n)",
        "What is the auxiliary space complexity of the Merge Sort algorithm?;O(n)",
        "Which data structure is used for the implementation of recursion?;Stack",
        "In a graph, what is the time complexity of Breadth-First Search (BFS) when using an adjacency list?;O(V + E)",
        "What is the best-case time complexity of Quick Sort?;O(n log n)",
        "Which heap operation has a time complexity of O(log n)?;Insertion",
        "Which algorithm uses a priority queue to find the shortest path in a weighted graph?;Dijkstra's Algorithm",
        "What is the time complexity of finding the median of two sorted arrays of size n using a divide-and-conquer approach?;O(log n)",
        "What is the amortized time complexity of an insertion in a dynamic array?;O(1)",
        "Which traversal technique in Binary Trees visits nodes in the order: Left, Root, Right?;Inorder"
    ]
    with open("quiz.txt", "w") as file:
        for question in questions:
            file.write(f"{question}\n")
    print("Quiz file populated with 10 DSA questions!")

def register():
    """Registers a new user."""
    print("\n--- Registration ---")
    username = input("Enter a username: ").strip()
    password = input("Enter a password: ").strip()

    if os.path.exists("users.txt"):
        with open("users.txt", "r") as file:
            users = file.readlines()
            for user in users:
                if user.split(",")[0] == username:
                    print("Username already exists. Try logging in.")
                    return False

    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")
    print("Registration successful!")
    return True

def login():
    """Logs in an existing user."""
    print("\n--- Login ---")
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    if not os.path.exists("users.txt"):
        print("No registered users. Please register first.")
        return None

    with open("users.txt", "r") as file:
        users = file.readlines()
        for user in users:
            registered_username, registered_password = user.strip().split(",")
            if registered_username == username and registered_password == password:
                print("Login successful!")
                return username

    print("Invalid username or password. Try again.")
    return None

def take_quiz(username):
    """Handles the quiz functionality."""
    print("\n--- Quiz Time ---")

    if not os.path.exists("quiz.txt"):
        print("No quiz available. Please add questions to 'quiz.txt' and try again.")
        return

    with open("quiz.txt", "r") as file:
        questions = file.readlines()

    score = 0
    total = len(questions)

    for question in questions:
        parts = question.strip().split(";")
        if len(parts) != 2:
            print("Invalid question format in quiz file.")
            continue

        q, ans = parts
        print(q)
        user_answer = input("Your answer: ").strip()

        if user_answer.lower() == ans.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {ans}")

    print(f"\n{username}, you scored {score}/{total}.")

    with open("results.txt", "a") as file:
        file.write(f"{username},{score},{total}\n")

def view_results():
    """Displays the results of all users."""
    print("\n--- Results ---")

    if not os.path.exists("results.txt"):
        print("No results available.")
        return

    with open("results.txt", "r") as file:
        results = file.readlines()

    for result in results:
        username, score, total = result.strip().split(",")
        print(f"{username} scored {score}/{total}")

def main():
    """Main program loop."""
    # Populate quiz file if it doesn't exist
    if not os.path.exists("quiz.txt"):
        populate_quiz_file()

    while True:
        print("\n--- Quiz Application ---")
        print("1. Register")
        print("2. Login")
        print("3. View Results")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register()
        elif choice == "2":
            username = login()
            if username:
                take_quiz(username)
        elif choice == "3":
            view_results()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if _name_ == "_main_":
    main()
