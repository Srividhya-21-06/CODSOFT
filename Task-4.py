import random
random_choices = ["rock", "paper", "scissors"]
your_score = 0
system_score = 0
print("🎮 Welcome to Rock-Paper-Scissors Game!")
while True:
    print("\nChoose one: rock, paper, or scissors")
    your_choice = input("Your choice: ").lower()
    if your_choice not in random_choices:
        print("❌ Invalid choice. Try again.")
        continue
    system_choice = random.choice(random_choices)
    print(f"🧍 You chose: {your_choice}")
    print(f"💻 Computer chose: {system_choice}")
    if your_choice == system_choice:
        print("🤝 It's a tie!")
    elif (
        (your_choice == "rock" and system_choice == "scissors") or
        (your_choice == "paper" and system_choice == "rock") or
        (your_choice == "scissors" and system_choice == "paper")
    ):
        print("✅ You win this round!")
        your_score += 1
    else:
        print("❌ You lose this round!")
        system_score += 1
    print(f"📊 Scores → You: {your_score} | Computer: {system_score}")
    redo = input("\nWant to Play again? (yes/no): ").lower()
    if redo != "yes":
        print("👋 Thanks for playing the game!!!!!!")
        break
