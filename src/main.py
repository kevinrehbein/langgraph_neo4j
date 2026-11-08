# Copyright (c) 2026 Kevin Rehbein
# Licensed under the MIT License.

import argparse
import logging
from datetime import datetime

from agents.graph import graph_builder
from agents.state import initial_state
from agents.utils import format_final_response
from config import (
    GRAPH_RECURSION_LIMIT,
    MAX_QUESTION_CHARS,
    OUTPUT_DIR,
    validate_config,
)

logger = logging.getLogger("wit")


def ask(question: str) -> str:
    question = question.strip()
    if not question:
        raise ValueError("A pergunta não pode ser vazia.")
    if len(question) > MAX_QUESTION_CHARS:
        raise ValueError(f"Pergunta muito longa (máx. {MAX_QUESTION_CHARS} caracteres).")

    result = graph_builder().invoke(
        initial_state(question), config={"recursion_limit": GRAPH_RECURSION_LIMIT}
    )
    text = format_final_response(result.get("final_response"))
    if result.get("warning"):
        text += f"\n\n> ⚠️ {result['warning']}"
    return text


def _save(text: str) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUTPUT_DIR / f"resposta_{datetime.now():%Y%m%d_%H%M%S}.md"
    path.write_text(text, encoding="utf-8")
    print(f"\n[salvo em {path}]")


def _answer(question: str, save: bool) -> None:
    try:
        text = ask(question)
    except ValueError as exc:
        print(f"Entrada inválida: {exc}")
        return
    except Exception:
        logger.exception("Falha ao processar a pergunta")
        print("Ocorreu um erro ao processar sua pergunta. Veja os logs para detalhes.")
        return
    print(f"\n{text}\n")
    if save:
        _save(text)


def main() -> None:
    parser = argparse.ArgumentParser(description="Assistente de agentes WIT")
    parser.add_argument("question", nargs="*", help="Pergunta (omita para modo interativo)")
    parser.add_argument("--save", action="store_true", help="Salva a resposta em data/outputs")
    parser.add_argument("-v", "--verbose", action="store_true", help="Logs detalhados")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s [%(name)s] %(message)s",
    )
    validate_config()

    if args.question:
        _answer(" ".join(args.question), args.save)
        return

    print("Meninas Digitais Assistant — digite 'sair' para encerrar.")
    while True:
        try:
            question = input("\nVocê: ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if question.lower() in {"sair", "exit", "quit", "q"}:
            break
        if question:
            _answer(question, args.save)


if __name__ == "__main__":
    main()