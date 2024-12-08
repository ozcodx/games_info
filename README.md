# Debian Games Info
Fetches game details from Debian repositories and adds them to a CSV file.

## Description
This Python script processes a CSV file containing Linux game information, retrieves additional data from the Debian repositories, and outputs a new CSV with extended information. The script uses `apt-cache` to fetch the **Description-en**, **Tag**, and **Homepage** for each game.

## Requirements
- Python 3.7 or higher
- `pandas` library

## Setup

1. Clone or download the repository.
2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate 
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Ensure that the input CSV file (`games_list.csv`) is in the same directory as the script. The CSV should contain the following columns:
   - **Game Name**
   - **Version**
   - **Repository**
   - **Short Description**

## Usage

1. Run the script:

   ```bash
   python get_info.py
   ```

2. The script will process the input CSV and generate a new CSV file (`games_info.csv`) with the additional columns:
   - **Description-en**
   - **Tag**
   - **Homepage**

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.