def formatar_fontes(itens: list[dict], consulta: str = "") -> str:
    """Formato único de evidência: um bloco [FONTE: título | url] por item.

    `consulta` não é usada aqui; serve para a instrumentação enxergar a busca.
    """
    return "\n\n".join(
        f"[FONTE: {i.get('titulo') or 'Sem título'} | {i.get('url') or ''}]\n"
        f"{i.get('corpo') or ''}".rstrip()
        for i in itens
    )