import logging
from collections import Counter

import spacy
from spacy import Language

from papers import Papers

logger = logging.getLogger(__name__)

class EntityCounter:
    """
    To get the top named entities from a set of Papers.
    """
    nlp: Language

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def top_entities(self, papers: Papers, num_entities: int = 5):
        doc = self.nlp(papers.content())
        return Counter([ e.text for e in doc.ents ]).most_common(num_entities)
