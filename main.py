# from openai import OpenAI
# client = OpenAI()

# response = client.responses.create(
#     model="gpt-4.1",
#     input="Write a one-sentence bedtime story about a unicorn."
# )

# print(response.output_text)

# from openai import OpenAI
# client = OpenAI()

# response = client.responses.create(
#     model="gpt-4.1",
#     input=[
#         {"role": "user", "content": "what teams are playing in this image?"},
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "input_image",
#                     "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/3b/LeBron_James_Layup_%28Cleveland_vs_Brooklyn_2018%29.jpg"
#                 }
#             ]
#         }
#     ]
# )

# print(response.output_text)


# response = client.responses.create(
#     model="gpt-4.1",
#     # tools=[{"type": "web_search_preview"}],
#     input="Say some really long words",
#     stream=True
# )

# for event in response:
#     print(event)
#     print()
#     print()


# response = client.responses.create(
#     model="dall-e-3",
#     input="Generate an image of gray tabby cat hugging an otter with an orange scarf",
#     tools=[{"type": "image_generation"}],
# )

# #  Save the image to a file
# image_data = [
#     output.result
#     for output in response.output
#     if output.type == "image_generation_call"
# ]

# if image_data:
#     image_base64 = image_data[0]
#     with open("cat_and_otter.png", "wb") as f:
#         f.write(base64.b64decode(image_base64))


# from openai import OpenAI
# client = OpenAI()

# result = client.images.generate(
#     model="dall-e-3",
#     prompt="a white siamese cat",
#     size="1024x1024"
# )

# print(result.data[0].url)

from openai import OpenAI
from pydantic import BaseModel

client = OpenAI()

class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]

response = client.responses.parse(
    model="gpt-4o-2024-08-06",
    input=[
        {"role": "system", "content": "Extract the event information."},
        {
            "role": "user",
            "content": "Alice and Bob are going to a science fair on Friday.",
        },
    ],
    text_format=CalendarEvent,
)

event = response.output_parsed

print(event)