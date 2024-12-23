# Budget Tracker 💰

A simple Python application to track your expenses, manage your budget, and save your data efficiently using JSON.

## Features
- **User-Friendly Input**: Add purchases with descriptions easily.
- **Dynamic Budget Tracking**: Keep track of your total budget and spending.
- **Automatic File Saving**: Save expense data to a JSON file with a timestamped filename.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

## How It Works
1. **Enter Your Budget**: Start by entering your total budget.
2. **Add Purchases**: Input the cost and description of each purchase.
3. **Exit and Save**: Upon exiting, the program saves all data into a JSON file named by date and time (e.g., `budget_2024-12-23_15-30.json`).

## File Structure
- `budget_tracker.py`: The main Python script.
- `saved_files/`: A folder where all JSON files are stored (optional structure if used).

## Requirements
- **Python 3.x**: Make sure you have Python installed on your system.
- No external libraries needed (uses Python's built-in `json` and `datetime` modules).

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Budget-Tracker.git
   cd Budget-Tracker
