import subprocess
import pandas as pd
import time

# Function to get package details from Debian repositories using apt-cache
def get_debian_package_info(package_name):
    time.sleep(0.1)
    try:
        # Get package details using 'apt-cache show'
        print(f"Getting {package_name} Info")
        result = subprocess.run(['aptitude', 'show', package_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        package_info = result.stdout.decode('utf-8')
        return package_info
    except Exception as e:
        print(f"Error fetching package info for {package_name}: {e}")
        return None

# Function to parse the important fields from Debian package info
def parse_debian_package_info(package_info):
    info_dict = {
        'Description': '',
        'Tags': '',
        'Homepage': ''
    }

    lines = package_info.splitlines()
    for line in lines:
        if line.startswith('Description'):
            info_dict['Description'] = line.split(' ', 1)[1]
        elif line.startswith('Tags'):
            info_dict['Tags'] = line.split(' ', 1)[1]
        elif line.startswith('Homepage'):
            info_dict['Homepage'] = line.split(' ', 1)[1]

    return info_dict

def process_tags(tags):
    # Initialize empty lists for categories and interfaces
    category = None
    interfaces = []
    other_tags = []

    # Split the tags string into individual tags
    tag_list = tags.split(', ')

    for tag in tag_list:
        if tag.startswith('game::'):
            category = tag.split('::')[1]  # Extract the category part after 'game::'
        elif tag.startswith('interface::'):
            interfaces.append(tag.split('::')[1])  # Extract the interface part after 'interface::'
        else:
            other_tags.append(tag)  # Add the remaining tags to other_tags
    
    # Join interface and other tags into comma-separated strings
    interface_tags = ', '.join(interfaces)
    other_category_tags = ', '.join(other_tags)

    return category, interface_tags, other_category_tags

# Function to process each game and add extra info
def process_game(row, delay=1):
    game_name = row['Game Name']
    version = row['Version']
    repository = row['Repository']
    description = row['Short Description']
    
    # Pause to avoid overloading the server
    time.sleep(delay)  # Delay for 1 second before processing the next game
    
    # Get Debian package info
    package_info = get_debian_package_info(game_name)
    game_info = {'Game Name': game_name, 'Version': version, 'Repository': repository, 'Short Description': description}
    
    if package_info:
        # Parse the relevant fields from the package info
        debian_info = parse_debian_package_info(package_info)
        game_info.update(debian_info)

        # Process the tags into Category, Interface, and Tags
        if 'Tags' in debian_info:  # Check if the 'Tag' field exists
            category, interface_tags, other_category_tags = process_tags(debian_info['Tags'])
            game_info['Category'] = category
            game_info['Interface'] = interface_tags
            game_info['Tags'] = other_category_tags  # The remaining tags
    
    return game_info

# Main function to read CSV, process each row, and save to a new CSV
def process_csv(input_filename, output_filename):
    # Read input CSV file
    df = pd.read_csv(input_filename)
    
    # Process each game and collect the results
    game_data = []
    for _, row in df.iterrows():
        game_info = process_game(row)
        game_data.append(game_info)
    
    # Convert the data into a new DataFrame and save it to a new CSV file
    output_df = pd.DataFrame(game_data)
    output_df.to_csv(output_filename, index=False)

# Example usage
def main():
    input_filename = 'debian_games.csv'  # Your input CSV file
    output_filename = 'games_info.csv'  # Output file with extra info
    process_csv(input_filename, output_filename)

if __name__ == "__main__":
    main()
