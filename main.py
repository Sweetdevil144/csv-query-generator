import csv
import openai

# Set your OpenAI API key here.
openai.api_key = 'YOUR_API_KEY'


def remove_blank_lines(text):
    return "\n".join(line for line in text.split("\n") if line.strip())


def generate_conversations(query):
    return [
        [
            {
                "role": "system",
                "content": "You are a digital number extractor. Regardless of the nature of the question, respond ONLY "
                           "with the direct numerical data or numeric ranges related to the query. Any contextual, "
                           "descriptive, or explanatory text should be excluded. Think of yourself as a machine that can "
                           "only display numbers in response to questions."
            },
            {
                "role": "user",
                "content": f"What's the typical cost range when visiting or using an {query}?"
            }
        ],
        [
            {
                "role": "system",
                "content": "You are a digital number extractor. Regardless of the nature of the question, respond ONLY "
                           "with the direct numerical data or numeric ranges related to the query. Any contextual, "
                           "descriptive, or explanatory text should be excluded. Think of yourself as a machine that "
                           "can only display numbers in response to questions. If you do not have specific "
                           "information, provide a generalized estimate based on similar venues or services."
            },
            {
                "role": "user",
                "content": f"Can you give me an estimate of how many people in California visit an {query} each year?"
            }
        ]
    ]


def main():
    # Read from data.csv
    with open('data.csv', 'r') as infile:
        csv_reader = csv.reader(infile)
        queries = [row[0] for row in csv_reader]

    # Write results to result.csv
    with open('result.csv', 'w', newline='') as outfile:
        csv_writer = csv.writer(outfile)
        csv_writer.writerow(["Query", "Average Cost (Range)", "Annual Visits in California"])

        for query in queries:
            conversations = generate_conversations(query)
            row = [query]
            for conversation in conversations:
                response = \
                openai.ChatCompletion.create(model="gpt-3.5-turbo-16k", messages=conversation).choices[0].message[
                    'content']
                response = remove_blank_lines(response)
                row.append(response)
            csv_writer.writerow(row)


if __name__ == '__main__':
    main()
