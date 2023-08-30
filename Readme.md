# README.md for Average Costs Fetcher

## Introduction
This script leverages the power of OpenAI's GPT-3.5 API to fetch average costs for a list of queries provided in a CSV file.

## Dependencies
- `csv`: In-built Python library for reading and writing CSV files.
- `openai`: The official Python client for the OpenAI API. Make sure to have it installed:

  ```bash
  pip install openai
  ```

## Setting Up
Before using this script, ensure you have:

1. An active OpenAI API subscription.
2. Your OpenAI API key. You'll set this in the `openai.api_key` section of the script. For example:

   ```python
        openai.api_key = 'YOUR_GPT_3.5_API_KEY'
   ```

## How To Use

1. Prepare your input file, `data.csv`. Each line in this file should contain a single query for which you want to fetch the average cost.

2. Run the script:

   ```bash
   python your_script_name.py
   ```

3. After executing the script, you'll find the results in `result.csv`. This file will contain the numeric values of the average costs for each query.

## Functions Overview

- `remove_blank_lines(text)`: Removes blank lines from the text.

- `generate_conversation(query)`: Generates a conversation format that instructs the model to only respond with numeric values for the given query.

- `main()`: The main function that reads queries from `data.csv`, gets the responses from OpenAI API, and writes the results to `result.csv`.

## Important Notes

- Make sure your API key is kept confidential. Avoid sharing your script with the API key embedded.
- Be cautious about the number of queries in `data.csv` as you'll be billed per token by OpenAI. Large numbers of queries can incur significant costs.
- The current script instructs the model to respond only with numbers. Adjust the instruction if you have different requirements.

## Contribution & Support
Feel free to fork this repository or submit pull requests with enhancements. For any issues or support, open an issue on the repository.