import csv
import openai

# Set your OpenAI API key here.
openai.api_key = 'OPEN-AI-API_KEY'


# Dynamically generate a list of all U.S. states
states = [
    'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado',
    'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho',
    'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana',
    'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
    'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
    'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
    'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',
    'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
    'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia',
    'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'
]


def remove_blank_lines(text):
    return "\n".join(line for line in text.split("\n") if line.strip())


def generate_conversations(query, state):
    return [
        {
            "role": "system",
            "content": "You are a digital number extractor. Regardless of the nature of the question, respond ONLY "
                       "with the direct numerical data or numeric ranges related to the query. Any contextual, "
                       "descriptive, or explanatory text should be excluded. Think of yourself as a machine that can "
                       "only display numbers in response to questions."
        },
        {
            "role": "user",
            "content": f"Can you give me an estimate of how many people in {state} visit a/an {query} each year?"
        }
    ]


def main():
    # Read from data.csv
    with open('./data/data.csv', 'r') as infile:
        csv_reader = csv.reader(infile)
        queries = [row[0] for row in csv_reader]

    # Create the header for the CSV file
    header = ["Query", "Average Cost (Range)"]
    for state in states:
        header.append(f"{state}")

    # Write results to result.csv
    with open('./data/result.csv', 'w', newline='') as outfile:
        csv_writer = csv.writer(outfile)
        csv_writer.writerow(header)

        for query in queries:
            row = [query]

            # Common conversation to find the cost range
            cost_conversation = [
                {
                    "role": "system",
                    "content": "You are a specialized model trained to provide numerical data in response to queries."
                    "Your primary role is to offer precise numerical data or numeric ranges. If specific numbers are "
                    "not available, offer your best estimated numerical range based on the general knowledge you've "
                    "been trained on. Please refrain from providing any explanatory or contextual text."
                },
                {
                    "role": "user",
                    "content": f"What's the typical cost range for {query}? If precise numbers are not available, a "
                    "reasonable estimated numerical range will suffice."
                }
            ]
            cost_response = \
            openai.ChatCompletion.create(model="gpt-3.5-turbo-16k", messages=cost_conversation).choices[0].message[
                'content']
            cost_response = remove_blank_lines(cost_response)
            row.append(cost_response)

            # Generate conversations and append data for each state
            for state in states:
                conversation = generate_conversations(query, state)
                response = \
                openai.ChatCompletion.create(model="gpt-3.5-turbo-16k", messages=conversation).choices[0].message[
                    'content']
                response = remove_blank_lines(response)
                row.append(response)

            csv_writer.writerow(row)


if __name__ == '__main__':
    main()
