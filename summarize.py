from urllib.request import urlopen

from huggingface_hub import InferenceClient
from bs4 import BeautifulSoup

from papers import HuggingFacePapers
from summarizer import Summarizer

papers = HuggingFacePapers.from_year_month('2025', '03', 5)

hf_token = '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'

summarizer = Summarizer(hf_token)

print(summarizer.summarize(papers.papers, 2))



