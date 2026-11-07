from dotenv import load_dotenv
from langchain.chat_models import init_chat_model


def get_llm(temperature: float = 0.0, **kwargs):

    load_dotenv()

    llm_1 = init_chat_model(
        model="gemma-4-31b-it", model_provider="google_genai", temperature=temperature
    )

    llm_2 = init_chat_model(
        model="gemma-4-26b-a4b-it",
        model_provider="google_genai",
        temperature=temperature,
    )

    llm_3 = init_chat_model(
        model="gemini-3.5-flash-lite",
        model_provider="google_genai",
        temperature=temperature,
    )

    llm_4 = init_chat_model(
        model="gemini-3.1-flash-lite",
        model_provider="google_genai",
        temperature=temperature,
    )

    llm_5 = init_chat_model(
        model="gemini-2.5-flash-lite",
        model_provider="google_genai",
        temperature=temperature,
    )

    llm_6 = init_chat_model(
        model="google/gemma-4-31b-it:free",
        model_provider="openrouter",
        temperature=temperature,
    )

    llm_7 = init_chat_model(
        model="google/gemma-4-26b-a4b-it:free",
        model_provider="openrouter",
        temperature=temperature,
    )

    llm_8 = init_chat_model(
        model="openai/gpt-oss-120b", model_provider="groq", temperature=temperature
    )

    llm_9 = init_chat_model(
        model="openai/gpt-oss-20b", model_provider="groq", temperature=temperature
    )

    llm_10 = init_chat_model(
        model="qwen/qwen3.8-27b", model_provider="groq", temperature=temperature
    )

    fallbacks = [llm_2, llm_3, llm_4, llm_5, llm_6, llm_7, llm_8, llm_9, llm_10]

    return llm_1.with_fallbacks(fallbacks)
