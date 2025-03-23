import logging
from huggingface_hub import InferenceClient

from papers import Papers

HUGGING_FACE_MODEL = "google/gemma-2-2b-it"
MAX_TOKENS = 500

logger = logging.getLogger(__name__)

class Summarizer:
    """
    Summarize a set of Papers using an LLM on HuggingFace
    """
    client: InferenceClient

    def __init__(self, hf_token: str):
        self.client = InferenceClient(
            provider="hf-inference",
            api_key=hf_token
        )

    def summarize(self, papers: Papers, num_sentences: int = 5) -> str:

        messages = [
            {
                "role": "user",
                "content": f"Please summarize the following scientific paper abstracts into "
                           f"a single abstract of {num_sentences} sentences."
                           f"\n\n{papers.content()}"
            }
        ]

        try:
            return self.client.chat_completion(
                model=HUGGING_FACE_MODEL,
                messages=messages,
                max_tokens=MAX_TOKENS
            ).choices[0].message.content


        except Exception:
            logger.warning("Failed to summarize, returning empty summary")
            return ""
