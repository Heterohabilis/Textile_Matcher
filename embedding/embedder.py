import openai
from typing import List


def get_embeddings_from_descriptions(
        descriptions: List[str],
        openai_api_key: str,
        model: str = "text-embedding-3-large"
) -> List[List[float]]:
    openai.api_key = openai_api_key

    response = openai.embeddings.create(
        input=descriptions,
        model=model
    )

    embeddings = [item.embedding for item in response.data]

    return embeddings
