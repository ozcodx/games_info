import pandas as pd
import os

def clean_file(input_file):
    # Load the CSV file
    if not os.path.exists(input_file):
        print("The input file does not exist. Please check the file path.")
        return
    
    df = pd.read_csv(input_file)

    # Filter games without a score or notes
    unreviewed_games = df[(df['Score'].isna()) & (df['Notes'].isna())]
    
    if unreviewed_games.empty:
        print("All games have already been reviewed!")
        return

        # Keep track of changes to update the main dataframe later
    updates = []

    # Loop through the unreviewed games
    for _, unreviewed_row in unreviewed_games.iterrows():
        base_game_name = unreviewed_row['Game Name']  # Current game name
        
        # Find potential addons (games whose names start with base_game_name + '-')
        for idx, row in df.iterrows():
            if pd.isna(row['Score']) and pd.isna(row['Notes']):
                game_name = row['Game Name']
                if game_name.startswith(f"{base_game_name}-"):
                    # Add to updates
                    updates.append((idx, 0, "addon"))  # (index, score, note)

    # Apply updates to the dataframe
    for idx, score, note in updates:
        df.at[idx, 'Score'] = score
        df.at[idx, 'Notes'] = note

    # Save the updated file
    df.to_csv(input_file, index=False)
    print("\nGame updated successfully. Exiting.")

# Entry point
if __name__ == "__main__":
    input_file = "games_info.csv"  # Input CSV file
    clean_file(input_file)