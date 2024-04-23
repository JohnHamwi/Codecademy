import random  # Import the random module to generate random numbers

# Variables for the user's name and the question they want to ask
name = ""  # Assume no name is provided
question = "Will I win the lottery?"  # The question provided
answer = ""  # Initialize the answer variable as an empty string

# Ensure there is a question to answer
if question == "":
    print("Please ask a question for the Magic 8-Ball to answer.")
else:
    # Generate a random number between 1 and 12 (inclusive)
    random_number = random.randint(1, 12)

    # Decision structure to assign an answer based on the random number
    if random_number == 1:
        answer = "Yes - definitely"
    elif random_number == 2:
        answer = "It is decidedly so"
    elif random_number == 3:
        answer = "Without a doubt"
    elif random_number == 4:
        answer = "Reply hazy, try again"
    elif random_number == 5:
        answer = "Ask again later"
    elif random_number == 6:
        answer = "Better not tell you now"
    elif random_number == 7:
        answer = "My sources say no"
    elif random_number == 8:
        answer = "Outlook not so good"
    elif random_number == 9:
        answer = "Very doubtful"
    elif random_number == 10:
        answer = "Yes, in due time"
    elif random_number == 11:
        answer = "Definitely not"
    elif random_number == 12:
        answer = "You may rely on it"
    else:
        print("Error")  # Handle unexpected cases

    # Output the question and the answer
    if name == "":
        print("Question: " + question)  # Print just the question if no name is provided
    else:
        print(name + " asks: " + question)  # Include the name if it is provided

    print("Magic 8-Ball's answer: " + answer)  # Display the answer provided by the Magic 8-Ball
