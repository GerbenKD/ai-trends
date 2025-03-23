import logging

from huggingface_hub import InferenceClient

from papers import Paper

HUGGING_FACE_MODEL = "google/gemma-2-2b-it"
MAX_TOKENS = 500

logger = logging.getLogger(__name__)

class Summarizer:
    client: InferenceClient

    def __init__(self, hf_token: str):
        self.client = InferenceClient(
            provider="hf-inference",
            api_key=hf_token
        )

    def summarize(self, papers: list[Paper], num_sentences: int = 5) -> str:

        content = "\n\n".join([ p.content() for p in papers ])

        messages = [
            {
                "role": "user",
                "content": f"Please summarize the following scientific paper abstracts into "
                           f"a single abstract of {num_sentences} sentences."
                           f"\n\n{content}"
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