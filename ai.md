# AI

LLMs, or Large Language Models, are advanced AI systems designed to understand and generate human-like  
text based on vast amounts of data. They are trained on diverse text sources, enabling them to perform  
a variety of tasks such as:

- **Natural Language Understanding**: Comprehending and interpreting text to derive meaning.
- **Text Generation**: Creating coherent and contextually appropriate text based on a given prompt.
- **Conversation**: Engaging in human-like dialogue, answering questions, and carrying out conversations.
- **Summarization**: Condensing long texts into brief summaries while retaining key information.
- **Translation**: Converting text from one language to another with high accuracy.

LLMs have applications in chatbots, content creation, language translation, and much more,  
revolutionizing the way we interact with technology.


## Models


| Name             | Date of Publishing | Country of Origin | Model Category          |
|------------------|--------------------|-------------------|-------------------------|
| **ChatGPT**      | November 2022      | USA               | General-purpose LLM     |
| **GPT-4**        | March 2023         | USA               | Advanced multi-modal LLM|
| **DeepSeek R1**  | January 2025       | China             | General-purpose LLM     |
| **Mistral 7B**   | September 2023     | France            | Open-weight LLM         |
| **Claude 3.5**   | June 2024          | USA               | Safety-focused LLM      |
| **Grok-1**       | November 2023      | USA               | Open-source LLM         |
| **PaLM 2**       | May 2023           | USA               | Multilingual LLM        |
| **Falcon 180B**  | September 2023     | UAE               | Open-weight LLM         |
| **Gemini 1.5**   | February 2024      | USA               | Multimodal LLM          |
| **Llama 2**      | July 2023          | USA               | Open-source LLM         |
| **Command R**    | 2024               | Canada            | Retrieval-augmented LLM |
| **Phi-2**        | December 2023      | USA               | Small-scale LLM         |
| **GPT-Neo**      | March 2021         | USA               | Open-source LLM         |
| **BERT**         | October 2018       | USA               | Bidirectional Encoder    |
| **LaMDA**        | May 2021           | USA               | Conversational LLM      |


## Web interfaces 

- `https://chatgpt.com` - recent leader in AI  
- `https://venice.ai` - focus on privacy
- `https://playground.allenai.org/` - open source, academic LLM
- `https://openrouter.ai` - connecting multiple LLM services, including free ones
- `https://www.perplexity.ai` - deep research and instant answers
- `https://abacus.ai` - one superasistant
- `https://console.groq.com` - generous, free access to top LLMs
- `https://chat.deepseek.com` - excellent Chinese model
- `https://chat.qwenlm.ai/` - Chinese model from Alibaba
- `https://github.com/cheahjs/free-llm-api-resources` - free API resources


## Simple chat 

```python
from ollama import chat

# Define the input message
message = {
    "model": "phi4",
    "messages": [{"role": "user", "content": "Is pluto a planet?"}]
}

# Use the Ollama chat function
response = chat(model=message["model"], messages=message["messages"])

# Print the response
print(response["message"]["content"])
```



## Ollama vision

```python
import ollama

response = ollama.chat(
    model='llama3.2-vision',
    messages=[{
        'role': 'user',
        'content': 'What is in this image?',
        'images': ['image2.jpg']
    }]
)

print(response)
```

## List models

list local models

```python
from ollama import list
from ollama import ListResponse

response: ListResponse = list()

for model in response.models:
    print('Name:', model.model)
    print('  Size (MB):', f'{(model.size.real / 1024 / 1024):.2f}')
    if model.details:
        print('  Format:', model.details.format)
        print('  Family:', model.details.family)
        print('  Parameter Size:', model.details.parameter_size)
        print('  Quantization Level:', model.details.quantization_level)
    print('\n')
```

## Ollama via OpenAI API

Connect to the Ollama local models via OpenAI API, which became industry standard.  

```python
import openai

client = openai.OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="nokeyneeded",
)

response = client.chat.completions.create(
    model="deepseek-r1",
    temperature=0.7,
    n=1,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a haiku about a hungry cat"},
    ],
)

print("Response:")
print(response.choices[0].message.content)
```

## Streaming example

```python
from ollama import chat

prompt = "When was Alien movie released?"
for chunk in chat(model="deepseek-r1", messages=[{"role": "user", "content": prompt}], stream=True):
    print(chunk['message']['content'], end='', flush=True)
```


## Sentiment analysis with HuggingFace

```python
from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
import numpy as np
from scipy.special import softmax

# Preprocess text (username and link placeholders)


def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)


MODEL = f"cardiffnlp/twitter-roberta-base-sentiment-latest"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
config = AutoConfig.from_pretrained(MODEL)
# PT
model = AutoModelForSequenceClassification.from_pretrained(MODEL)
# model.save_pretrained(MODEL)
# text = "Covid cases are increasing fast!"
text = "That was a trash movie."
text = preprocess(text)

encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)
scores = output[0][0].detach().numpy()
print(scores)
scores = softmax(scores)
print(scores)
# # TF
# model = TFAutoModelForSequenceClassification.from_pretrained(MODEL)
# model.save_pretrained(MODEL)
# text = "Covid cases are increasing fast!"
# encoded_input = tokenizer(text, return_tensors='tf')
# output = model(encoded_input)
# scores = output[0][0].numpy()
# scores = softmax(scores)
# Print labels and scores
ranking = np.argsort(scores)
ranking = ranking[::-1]

for i in range(scores.shape[0]):
    l = config.id2label[ranking[i]]
    s = scores[ranking[i]]
    print(f"{i+1}) {l} {np.round(float(s), 4)}")
```

## OpenRouter

```python
from openai import OpenAI
import os

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.environ["OPENROUTER_API_KEY"],
)

completion = client.chat.completions.create(
  model="deepseek/deepseek-r1:free",
  messages=[
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
)

print(completion.choices[0].message.content)
```

## Sentiment analysis

```python
from openai import OpenAI

import yaml
from pathlib import Path
import os
import time


client = OpenAI(
    base_url="https://api.deepseek.com",
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
)

# movie_reviews = {
#     1: "The storyline was absolutely captivating, and the performances were brilliant. I couldn't look away for a second!",
#     2: "The pacing was excruciatingly slow, and the characters lacked depth. I was bored halfway through.",
#     3: "While the visuals were breathtaking, the plot felt predictable and uninspired.",
#     4: "This is a cinematic masterpiece that touched my heart. Every scene was perfection!",
#     5: "The dialogue was cringe-worthy, and the humor fell flat. Definitely not worth the hype.",
#     6: "It was an average film—not great, but not terrible either. I enjoyed some parts.",
#     7: "The chemistry between the leads was electric, and the soundtrack was phenomenal!",
#     8: "The movie started strong but completely fell apart in the second half. Such a disappointment.",
#     9: "A visually stunning film that combines action and emotion seamlessly. Highly recommend!",
#     10: "The premise was intriguing, but the execution left a lot to be desired. It just didn't click for me."
# }

slovak_movie_reviews = {
    1: "Príbeh bol úplne pútavý a herecké výkony brilantné. Nemohol som sa odtrhnúť ani na sekundu!",
    2: "Tempo bolo mimoriadne pomalé a postavy nemali žiadnu hĺbku. Nudil som sa už v polovici.",
    3: "Hoci vizuálne efekty boli ohromujúce, dej pôsobil predvídateľne a bez inšpirácie.",
    4: "Toto je filmové dielo, ktoré mi dojalo srdce. Každá scéna bola dokonalosť!",
    5: "Dialógy boli trápne a humor úplne zlyhal. Určite to nestojí za ten humbug.",
    6: "Bol to priemerný film – nie dobrý, ale ani úplná katastrofa. Niektoré časti ma bavili.",
    7: "Chemia medzi hlavnými postavami bola elektrizujúca a soundtrack fenomenálny!",
    8: "Film začal skvele, ale v druhej polovici sa úplne rozpadol. Veľké sklamanie.",
    9: "Vizualne ohromujúci film, ktorý dokonale spája akciu a emócie. Určite odporúčam!",
    10: "Premisa bola zaujímavá, ale realizácia bola slabá. Nedokázalo ma to zaujať."
}

for key, value in slovak_movie_reviews.items():

    # content = 'On a scale 0-1, figure out the sentiment of the the following movie review:'
    content = 'Na škále od 0 do 1, napíš sentiment nasledujúceho filmu:'
    content += value

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": content,
            }
        ],
        temperature=0.7,
        top_p=0.9,
        model='deepseek-chat',
        max_completion_tokens=1000
    )

    # print(chat_completion.choices[0].message.content)
    output = chat_completion.choices[0].message.content
    print(key, value, output)
```

