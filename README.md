# Debian Games Info  
Fetches game details from Debian repositories and adds them to a CSV file.

## Description  
This project contains two Python scripts:

1. **`get_info.py`**: Processes a CSV file containing Linux game information, retrieves additional data from the Debian repositories, and outputs a new CSV with extended information. The script uses `apt-cache` to fetch the **Description-en**, **Tag**, and **Homepage** for each game.  

2. **`game_reviewer.py`**: Allows you to review games from the generated CSV (`games_info.csv`) by selecting a random unreviewed game, displaying its details, and letting you add a score (0-5) and notes. The file is updated automatically.

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

4. Ensure that the input CSV file (`games_list.csv`) is in the same directory as the scripts. The CSV should contain the following columns:  
   - **Game Name**  
   - **Version**  
   - **Repository**  
   - **Short Description**  

## Usage  

### Fetch Debian Game Info  

Run the script to generate `games_info.csv` with extended information:  

```bash
python get_info.py  
```

The output file will include these columns:  
- **Description**  
- **Tags**  
- **Homepage**  

### Review Games  

Run the script to review games, add scores and notes:  

```bash
python game_reviewer.py  
```

It will:  
- Select a random unreviewed game (no score or notes).  
- Display the game details:  
   - **Game Name**  
   - **Description**  
   - **Category**  
   - **Interface**  
   - Links to Homepage and Screenshots (if available).  
- Prompt you to input a **score** (0-5) and **notes**.  
- Update the `games_info.csv` file with your input.  

## License  
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.  
