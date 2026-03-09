from vector_store import search_similar
from llm_detector import analyze_url


def detect_url(url):

    similar_examples = search_similar(url)

    context = "\n".join(similar_examples)

    result = analyze_url(url, context)

    return result