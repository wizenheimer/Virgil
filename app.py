from pathlib import Path

import modal

image = modal.Image.debian_slim().pip_install(
    # scraping pkgs
    "beautifulsoup4~=4.11.1",
    "httpx~=0.23.3",
    "lxml~=4.9.2",
    # langchain pkgs
    "faiss-cpu~=1.7.3",
    "langchain~=0.0.138",
    "openai~=0.27.4",
    "tiktoken==0.3.0",
)
stub = modal.Stub(
    name="example-langchain-qanda",
    image=image,
    secrets=[modal.Secret.from_name("openai-secret")],
)
docsearch = None  # embedding index that's relatively expensive to compute, so caching with global var.
