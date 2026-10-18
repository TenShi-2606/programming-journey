"""Mini-project — The Three Doors.

A small text adventure using conditions, loops, functions, and input validation.
Run with: python3 05_project/text_adventure.py
"""


def ask_choice(prompt: str, choices: tuple[str, ...]) -> str:
    """Keep asking until the player enters one of the allowed choices."""
    allowed = {choice.lower() for choice in choices}
    while True:
        answer = input(prompt).strip().lower()
        if answer in allowed:
            return answer
        print("Choose one of:", ", ".join(choices))


def play() -> None:
    print("\n=== THE THREE DOORS ===")
    print("You wake up in a quiet room. Three doors stand before you.")
    choice = ask_choice("Choose red, blue, or green: ", ("red", "blue", "green"))

    if choice == "red":
        print("\nThe red door opens into a library.")
        action = ask_choice("Read a book or leave? (read/leave): ", ("read", "leave"))
        if action == "read":
            print("You discover a map and escape. Ending: The Curious Mind.")
        else:
            print("You leave safely, but the mystery remains. Ending: The Cautious One.")
    elif choice == "blue":
        print("\nThe blue door opens into a flooded corridor.")
        action = ask_choice("Swim or return? (swim/return): ", ("swim", "return"))
        if action == "swim":
            print("You find an exit on the other side. Ending: The Brave.")
        else:
            print("You return to the room and try another day. Ending: The Patient.")
    else:
        print("\nThe green door opens into a garden.")
        action = ask_choice("Explore or rest? (explore/rest): ", ("explore", "rest"))
        if action == "explore":
            print("You find a hidden gate. Ending: The Explorer.")
        else:
            print("You rest under a tree and wake up refreshed. Ending: The Peaceful.")

    print("\nThanks for playing!")


if __name__ == "__main__":
    play()
