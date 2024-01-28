# Solana Transaction Signer Scraper

Let's say you have some txHash that you need to look over and get the signer for each. How would you do that? 

## Description:

This Python script utilizes Selenium and BeautifulSoup to scrape signer information from Solana transactions on SolScan. It takes a batch of transaction IDs from a CSV file, filters out specific transactions, and then extracts the signer information by navigating to the SolScan website for each transaction ID. The results are stored in a Pandas DataFrame and exported to a CSV file.


## Libraries:

- **bs4 (BeautifulSoup):** For parsing HTML content.
- **webdriver from selenium:** For automating the web browser (in this case, Chrome).
- **pandas as pd:** For handling data in tabular form.
- **time:** For introducing delays in the script.
- **csv:** For working with CSV files.

## Set working directories:

- **path_in:** Input directory where the initial CSV file is located.
- **path_out:** Output directory where the final CSV file will be saved.

## Outline:

In this project we read transaction IDs from a CSV file (export_txs_batch1.csv), filtering only those with a specific condition (row[4] == '1'). The selected transaction IDs are stored in the list tx_id.

Remove the first element from `tx_id list (tx_id.pop(0))` as it is a header.

Then we define the base URL for SolScan (solscan = "https://solscan.io/tx/"). Initialize an empty list (signer) to store signer information.

Loop through each transaction ID in tx_id:
- Construct the URL for the specific transaction.
- Use Selenium to open the URL in a Chrome browser.
- Wait for 5 seconds to allow the page to load.
- Extract the page source.
- Parse the HTML using BeautifulSoup.
- Find all `<a>` tags with an href attribute, limiting to the first three.
- If the href contains "/account/", extract the signer information and append it to the signer list.

Once the loop is done we create a Pandas DataFrame (df) from the signer list and export the DataFrame to a CSV file (`signers.csv`) in the specified output directory (`path_out`). 
