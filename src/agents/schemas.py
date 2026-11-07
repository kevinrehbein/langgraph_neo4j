from typing import Literal

from pydantic import BaseModel, Field


class SupervisorDecision(BaseModel):
    intent: Literal["qa", "sintese", "plano", "fora_dominio"] = Field(
        ..., description="A intenção do usuário: 'qa', 'sintese', 'plano' ou 'fora_dominio'"
    )
    research_directive: str = Field(
        description="Instrução clara e direta dizendo ao pesquisador O QUE ele deve buscar na base de dados."
    )



class ProjectPlan(BaseModel):
    """Usado pelo planejador para gerar o formato final."""

    title: str = Field(..., description="Título do projeto proposto")
    target_audience: str = Field(..., description="Público alvo do projeto")
    justification: str = Field(..., description="Justificativa baseada nas evidências")
    methodology: list[str] = Field(..., description="Passos para execução")
    expected_results: list[str] = Field(..., description="Resultados esperados")
    references: list[str] = Field(
        ..., description="Artigos do WIT citados (nós do grafo)"
    )


class Review(BaseModel):
    """Usado pelo verificador para aprovar ou rejeitar o rascunho."""

    is_valid: bool = Field(
        ..., description="True se a resposta responde ao usuário, contém citações válidas e respeita o schema.",
    )
    feedback: str | None = Field(
        default=None,
        description="Se is_valid for False, explicar exatamente o que o agente deve corrigir.",
    )
