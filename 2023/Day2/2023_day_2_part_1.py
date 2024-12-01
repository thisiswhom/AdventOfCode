

input_file = open(r'example_input')

input_lines = input_file.readlines()

def parse_game_input(input_text):
    """
    Parses the game input text into a dictionary, with 'Game' as a key-value pair.
    Supports both string and list inputs.
    Includes print statements to show the process.
    """
    # Convert list input to a single string
    if isinstance(input_text, list):
        print("Input is a list; joining it into a single string...")
        input_text = "\n".join(input_text)

    # Initialize the result list
    games = []
    print("Starting to parse input text...")

    # Split the input into game blocks
    game_blocks = input_text.strip().split("\n")
    print(f"Split input into {len(game_blocks)} game blocks: {game_blocks}")

    for game_block in game_blocks:
        print(f"\nProcessing block: {game_block}")
        # Separate the game title (e.g., "Game 1") from the rounds
        game_title, rounds_text = game_block.split(":", 1)
        game_title = game_title.strip()
        print(f"Extracted game title: {game_title}")

        # Extract the game number
        game_number = int(game_title.split()[1])  # "Game 1" -> 1
        print(f"Game number parsed as: {game_number}")

        # Split the rounds by semicolons
        rounds = rounds_text.split(";")
        print(f"Split rounds into {len(rounds)} parts: {rounds}")

        # Parse each round into a dictionary
        parsed_rounds = {}
        for round_index, round_text in enumerate(rounds, start=1):
            round_text = round_text.strip()
            print(f"  Processing Round {round_index}: {round_text}")
            if not round_text:
                print(f"  Round {round_index} is empty. Skipping.")
                continue

            # Split the items in the round and parse into a dictionary
            items = round_text.split(",")
            print(f"  Split round into items: {items}")
            round_dict = {}
            for item in items:
                count, color = item.strip().split()
                round_dict[color] = int(count)
                print(f"    Parsed item '{item}': {color} -> {count}")

            # Use "Round X" as the key for this round
            parsed_rounds[f"Round {round_index}"] = round_dict
            print(f"  Completed parsing Round {round_index}: {round_dict}")

        # Add the game details to the list
        game_entry = {
            "Game": game_number,
            "Rounds": parsed_rounds
        }
        games.append(game_entry)
        print(f"Added game to list: {game_entry}")

    print("\nFinished parsing all input.")
    return games



parse_game_input(input_lines)