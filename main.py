import openai
import csv

# Insert your OpenAI API key here
openai.api_key = "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"

# Load the data from the CSV file
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# Generate prompts and ideal completions
prompts = []
completions = []
for row in data[1:]:
    prompt = f"A {row[2]} in {row[3]} with {row[0]} team in {row[1]} duration with {row[4]} desgining, {row[5]},{row[6]},{row[7]},{row[8]},{row[9]},{row[10]} skills"
    completion = f"{row[11]}"
    prompts.append(prompt)
    completions.append(completion)

# Generate the prompt and completion pairs
pairs = []
for i in range(len(prompts)):
    pair = {"prompt": prompts[i], "completion": completions[i]}
    pairs.append(pair)

# Print the prompt and completion pairs
for pair in pairs:
    print(pair)
