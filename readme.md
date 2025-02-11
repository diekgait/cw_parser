# Crypto Pair Data Extractor

This Python script extracts cryptocurrency pair data from Crypto Wizards html.
 1. Go to zscore
 2. Scroll down until you enough results
 3. Right click save the html.

## Requirements

* Python 3
* Beautiful Soup 4 (`bs4`)

## Installation

1.  **Clone the repository (or download the script):**

## Usage

1.  **Prepare the HTML file:** Place the `Scanner.html` file in the same directory as the Python script (`crypto_data_extractor.py`).

2.  **Run the script:**

    ```bash
    python crypto_data_extractor.py
    ```

3.  **Output:** The extracted data will be saved in a file named `output.csv` in the same directory.

## Script Description

The script parses the `Scanner.html` file using Beautiful Soup. It targets specific HTML elements using CSS selectors to extract the desired data points.  The extracted data is then written to a CSV file, making it easy to import into other tools for analysis or visualization.

## Configuration

*   **`limit` variable:** Controls the maximum number of crypto pairs to process.  Adjust this value in the script to change the number of rows extracted.