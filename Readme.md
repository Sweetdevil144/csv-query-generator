# Digital Number Extractor

## Overview
This script uses OpenAI's GPT-3.5 model to answer questions about the average cost range and annual visits for various venues or services in California. It reads a list of queries from a CSV file and then writes the model's responses back to another CSV file.

## Requirements
- Python 3.x
- OpenAI Python package
- CSV file containing the list of queries

## Setup
1. Install the OpenAI Python package:  
   ```
   pip install openai
   ```

2. Set your OpenAI API key as an environment variable or within the script.

## Usage
Run the script using:
```
python main.py
```
The script will read the queries from `data.csv` and write the results to `result.csv`.

## New Features
1. The model now provides generalized estimates for queries it cannot answer with specific information.  
2. The model responds only with numerical data or numeric ranges as per updated instructions.

## Limitations
- The model may still return 'unknown' for some specific or localized queries, flag such queries for manual research.
- The numbers provided are estimates and should be used as such.

---

Feel free to add more sections or details as you find appropriate for your project.