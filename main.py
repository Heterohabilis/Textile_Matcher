from util import read_description
from embedding import embedder
import os


def main():
    records = read_description.extract_customer_descriptions()
    k = os.getenv("OPENAI_API_KEY")
    if not k:
        print("Open AI API Key not found.")
        exit(1)
    vec = embedder.get_embeddings_from_descriptions(records, k)
    print(len(vec))

if __name__ == "__main__":
    main()