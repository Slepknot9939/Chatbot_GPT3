# Chatbot_GPT3

# ![image](https://user-images.githubusercontent.com/62091944/148089861-a37f5628-d9e6-4f05-ac99-2982ac90d2bb.png)


## What is GPT3?
### Generative Pre-trained Transformer 3 is an autoregressive language model that uses deep learning to produce human-like text. It is the third-generation language prediction model in the GPT-n series created by OpenAI, a San Francisco-based artificial intelligence research laboratory.

### GPT-3's full version has a capacity of 175 billion machine learning parameters. GPT-3, which was introduced in May 2020, and was in beta testing as of July 2020,[3] is part of a trend in natural language processing (NLP) systems of pre-trained language representations


### GPT-3 Training Data
| Dataset		| Tokens	|Weight in Training Mix|
|---|---|---|
|Common Crawl|	410 billion|	60% |
|WebText2|	19 billion|	22%|
|Books|		12 billion|	8%|
|Books2|		55 billion|	8%|
|Wikipedia|	3 billion|	3%|


## How does GPT-3 work?
### To generate output, GPT-3 has a very large vocabulary, which it can combine to generate sentences. These words are sorted into different categories (nouns, verbs, adjectives, etc.), and for each category, there is a “production rule”, which can be used to generate a sentence. The production rules can be modified with different parameters.

A few examples:

**noun + verb = subject + verb<br/>
noun + verb + adjective = subject + verb + adjective<br/>
verb + noun = subject + verb<br/>
noun + verb + noun = subject + verb + noun<br/>
noun + noun = subject + noun<br/>
noun + verb + noun + noun = subject + verb + noun + noun<br/>

In addition, GPT-3 is able to understand negations, as well as the use of tenses, which allows the model to generate sentences in the past, present and future.**

## How was GPT-3 trained?
At a high level, training the GPT-3 neural network consists of two steps.

The first step requires creating the vocabulary, the different categories and the production rules. This is done by feeding GPT-3 with books. For each word, the model must predict the category to which the word belongs, and then, a production rule must be created.

The second step consists of creating a vocabulary and production rules for each category. This is done by feeding the model with sentences. For each sentence, the model must predict the category to which each word belongs, and then, a production rule must be created.

The result of the training is a vocabulary, and production rules for each category.

The model also has a few tricks that allow it to improve its ability to generate texts. For example, it is able to guess the beginning of a word by observing the context of the word. It can also predict the next word by looking at the last word of a sentence. It is also able to predict the length of a sentence.

While those two steps and the related tricks may sound simple in theory, in practice they require massive amounts of computation


## Reasons why the GPT-3 model has been most talked about for
GPT-3 model consists of 175 billion parameters, the previous version, GPT-2 model had only 1.5 billion parameters. Parameters are weights in a neural network model that transforms the inputs to output
It is a generative model which means that it has the ability to generate a long sequence of words that is coherent as an output
This state-of-the-art language model can respond to almost any question passed on to it and that too in a more humane way
Billions of words, text, and code snippets used in model training hence make it capable of auto code in a wide range of programming languages
Its Multilingual text processing help to work on languages other than English as well
The best part is GPT-3 model can perform a specific task, such as being a translator or a chatbot or code builder without any customization or any special tuning, all it needs is a few training examples


## Types of Model in GPT3
__1)Base Series<br/>
	a)Davinci<br/>
	b)Curie<br/>
	c)Babbage<br/>
	d)Ada<br/>__
__2) Instruct Series<br/>__
__3) Codex Series<br/>__
__4) Contect Filter<br/>__


A) Base Series:-Our base GPT-3 models can understand and generate natural language. We offer four base models called davinci, curie, babbage, and ada with different levels of power suitable for different tasks. Davinci is the most capable model, and Ada is the fastest.

While Davinci is generally the most capable, the other models can perform certain tasks extremely well with significant speed or cost advantages. For example, Curie can perform many of the same tasks as Davinci, but faster and for 1/10th the cost.

B) Davinci
Davinci is the most capable engine and can perform any task the other models can perform and often with less instruction. For applications requiring a lot of understanding of the content, like summarization for a specific audience and creative content generation, Davinci is going to produce the best results. These increased capabilities require more compute resources, so Davinci costs more per API call and is not as fast as the other engines.

Another area where Davinci shines is in understanding the intent of text. Davinci is quite good at solving many kinds of logic problems and explaining the motives of characters. Davinci has been able to solve some of the most challenging AI problems involving cause and effect.

Good at: Complex intent, cause and effect, summarization for audience

C)Curie
Curie is extremely powerful, yet very fast. While Davinci is stronger when it comes to analyzing complicated text, Curie is quite capable for many nuanced tasks like sentiment classification and summarization. Curie is also quite good at answering questions and performing Q&A and as a general service chatbot.

Good at: Language translation, complex classification, text sentiment, summarization

D)Babbage
Babbage can perform straightforward tasks like simple classification. It’s also quite capable when it comes to Semantic Search ranking how well documents match up with search queries.

Good at: Moderate classification, semantic search classification

E)Ada
Ada is usually the fastest model and can perform tasks like parsing text, address correction and certain kinds of classification tasks that don’t require too much nuance. Ada’s performance can often be improved by providing more context.

Good at: Parsing text, simple classification, address correction, keywords

## 2)Finding the right model
Experimenting with Davinci is a great way to find out what the API is capable of doing. After you have an idea of what you want to accomplish you can either stay with Davinci if you’re not concerned about cost and speed or move onto Curie or another engine and try to optimize around its capabilities.

You can use this tool that lets you run different engines side-by-side to compare outputs, settings and response times and then download the data into a .xls spreadsheet: https://gpttools.com/comparisontool

__Try focusing on one task at a time<br/>__
__Consider semantic search<br/>__
__Fine tuned models<br/>__

## 3) Instruct series Beta
The Instruct models share our base GPT-3 models’ ability to understand and generate natural language, but they’re better at understanding and following your instructions. You simply tell the model what you want it to do, and it will do its best to fulfill your instructions. This is an important step forward in our goal of building safe models that are aligned with human interests.

Instruct models with different levels of power:

davinci-instruct-beta-v3<br/>
curie-instruct-beta-v2<br/>
babbage-instruct-beta<br/>
ada-instruct-beta<br/>

Using Instruct models

When using the Instruct series, your prompt should include instructions written in clear English — as if you were instructing a human to do the task.

## Weaknesses

The Instruct series is experimental: we don’t yet know which problems it will perform well on, and where it may perform poorly. We expect the Instruct series may be less suited for 2 domains:

## Semantic search - The Instruct series wasn’t trained to perform semantic search, and thus the core API models will likely outperform it at this task.
Long-form text continuation - The core API models are very good at continuing text provided in the prompt (for example, writing a news article given the first 2 paragraphs), and may be better than the Instruct series.

## 4) Codex series

The Codex models are descendants of our base GPT-3 models that can understand and generate code. Their training data contains both natural language and billions of lines of public code from GitHub.
They’re most capable in Python and proficient in over a dozen languages including JavaScript, Go, Perl, PHP, Ruby, Swift, TypeScript, SQL, and even Shell.

We currently offer two Codex models:
__a) davinci-codex---Most capable Codex model. Particularly good at translating natural language to code<br/>__
__b) cushman-codex-- Almost as capable as Davinci Codex, but slightly faster. This speed advantage may make it preferable for real-time application<br/>__

## 5)Content filter
The filter aims to detect generated text that could be sensitive or unsafe coming from the API. It's currently in beta mode and has three ways of classifying text- as safe, sensitive, or unsafe. The filter will make mistakes and we have currently built it to err on the side of caution, thus, resulting in higher false positives.

Label Descriptions
__0 - The text is safe.<br/>__
__1 - This text is sensitive. This means that the text could be talking about a sensitive topic, something political, religious, or talking about a protected class such as race or nationality.<br/>__
__2 - This text is unsafe. This means that the text contains profane language, prejudiced or hateful language, something that could be NSFW, or text that portrays certain groups/people in a harmful manner.<br/>__


![image](https://user-images.githubusercontent.com/62091944/148089799-398d7a40-328a-473f-b935-61152c22e87e.png)

