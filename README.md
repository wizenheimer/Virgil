# Serverless Inference
This example demonstrates the creation of a question-answering web endpoint and command-line interface (CLI), which is powered by a large-language-model (LLM). The application uses a single document, namely the 2022 USA State of the Union address delivered by President Joe Biden, as its knowledge-base. Nevertheless, the same application structure can be expanded to perform question-answering tasks on a broader range of text corpuses, including all State of the Union speeches and other large textual datasets.

## Defining dependencies    


The example depends on three PyPi packages for scraping and three for building and running question-answering functionality. They are installed in a Debian Slim base image using pip_install. The OpenAI API key is specified through the openai-secret Modal Secret. Additionally, a docsearch global variable is declared for caching a slow operation in the code.

## Scraping the speech from whitehouse.gov

Scraping Biden's speech transcript from whitehouse.gov is effortless using httpx and BeautifulSoup. Although the speech is short and a single document, it sufficiently showcases the LLM chain's question-answering ability.

## Constructing the Q&A chain

The LLM chain can answer questions regarding Biden's speech and refer to the corresponding parts of the speech containing evidence for the answers. It combines a text-embedding index with OpenAI's GPT-3 LLM to select the relevant parts of the speech for building a customized prompt.

## Modal Functions

Our application's functionality can be integrated into Modal through web and cli commands, which are implemented as web endpoints.


## License
Distributed under the MIT License. See [LICENSE](LICENSE) for more information.
        
