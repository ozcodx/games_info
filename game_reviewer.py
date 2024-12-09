import pandas as pd
import random
import os

# Function to display a game's information
def display_game_info(game):
    print("\n=== Game Details ===")
    print(f"Game Name: {game['Game Name']}")
    print(f"Description: {game['Description']}")
    print(f"Category: {game['Category']}")
    print(f"Interface: {game['Interface']}")
    
    if pd.notna(game['Homepage']):
        print(f"Homepage: {game['Homepage']}")
    else:
        print("Homepage: Not available")
    
    if pd.notna(game['Screenshots']):
        print(f"Screenshots: {game['Screenshots']}")
    else:
        print("Screenshots: Not available")

# Function to display the review status
def display_review_status(df):
    total_games = len(df)
    reviewed_games = len(df.dropna(subset=['Score', 'Notes']))
    print(f"\n=== Review Status: {reviewed_games}/{total_games} games reviewed ===")

# Function to get a score input
def get_score():
    while True:
        try:
            score = int(input("\nEnter a score for this game (0-5): "))
            if 0 <= score <= 5:
                return score
            else:
                print("Please enter a score between 0 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 5.")

# Function to get notes input
def get_notes():
    notes = input("\nEnter your notes for this game: ")
    return notes.strip()

# Main function to review games
def review_game(input_file):
    # Load the CSV file
    if not os.path.exists(input_file):
        print("The input file does not exist. Please check the file path.")
        return
    
    df = pd.read_csv(input_file)
    
    # Display the review status
    display_review_status(df)

    # Filter games without a score or notes
    unreviewed_games = df[(df['Score'].isna()) & (df['Notes'].isna())]
    
    if unreviewed_games.empty:
        print("All games have already been reviewed!")
        return

    # Select a random game
    random_game_index = random.choice(unreviewed_games.index)
    random_game = df.loc[random_game_index]

    # Display the game info
    display_game_info(random_game)
    
    # Ask user for score and notes
    score = get_score()
    notes = get_notes()

    # Ensure the 'Notes' column is of string type
    df['Notes'] = df['Notes'].astype(str)
    
    # Update the DataFrame with the score and notes
    df.at[random_game_index, 'Score'] = score
    df.at[random_game_index, 'Notes'] = notes
    
    # Save the updated file
    df.to_csv(input_file, index=False)
    print("\nGame updated successfully. Exiting.")

# Entry point
if __name__ == "__main__":
    input_file = "games_info.csv"  # Input CSV file
    review_game(input_file)