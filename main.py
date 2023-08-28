import csv
import openai

# Set your OpenAI API key here.
openai.api_key = 'YOUR_GPT_3.5_API_KEY'


def remove_blank_lines(text):
    return "\n".join(line for line in text.split("\n") if line.strip())


def generate_conversation(query):
    return [
        {
            "role": "system",
            "content": "For each item listed, please provide the average cost. Only respond with exact numbers or "
                       "number ranges. Ignore the question if no numbers are relevant. Do not use words, only numbers."
        },
        {
            "role": "user",
            "content": f"What is the average costs of {query}, please respond only in numeric values."
        }
    ]


def main():
    # Read from data.csv
    with open('data.csv', 'r') as infile:
        csv_reader = csv.reader(infile)
        queries = [row[0] for row in csv_reader]  # Each row contains a full query

    results = []
    for query in queries:
        conversation = generate_conversation(query)
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo-16k", messages=conversation).choices[0].message[
            'content']
        response = remove_blank_lines(response)
        results.append([query, response])

    # Write results to result.csv
    with open('result.csv', 'w', newline='') as outfile:
        csv_writer = csv.writer(outfile)
        for _, response in results:
            csv_writer.writerow([response])


if __name__ == '__main__':
    main()
