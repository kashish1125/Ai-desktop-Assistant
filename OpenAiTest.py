import os
import openai

openai.api_key = os.getenv("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")



response = openai.Completion.create(
  model="text-davinci-003",
  prompt="write a mail to your teacher for increasing your attendance due to medical reasons\n\n",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)