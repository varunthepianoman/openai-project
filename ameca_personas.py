from openai import OpenAI
client = OpenAI()

prompt = "Ameca_prompts/ameca_sassy.txt"

with open(prompt, "r", encoding="utf-8") as f:
    instructions = f.read()

while True:
    user_input = input("You: ")
    response = client.responses.create(
        model="gpt-4.1",
        instructions=instructions,
        input= [
            {"role": "user", "content": user_input},
        ],
        tools=[{"type": "web_search"}]

    )

    print("Ameca: " + response.output_text)


    