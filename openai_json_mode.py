from openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "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"

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": """
    You are a helpful assistant designed to output JSON.
    The text we are about to pass is the text that someone would have created after looking at the image and categorizing the products as shown below.
    ・PET bottles
    ・Fabric products
    ・Blister pack
    ・box
    ・Pouches, bags
    ・Cans, bottles
    ・Shrink packaging
    ・Others not applicable to the above

    You can read the text, look at the image, and give us a response in the Json format below.
    ### output
    {
        objectType:
    }
    """
      },
    {"role": "user", "content": "The image depicts a box."}
  ]
)
print(response.choices[0].message.content)
