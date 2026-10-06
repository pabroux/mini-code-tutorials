"""
Pydantic AI — a type-safe agent on a language model.

Try it:
    python llm_agent.py
"""

from dataclasses import dataclass
from typing import Literal

from pydantic import BaseModel, Field
from pydantic_ai import Agent, Capability, RunContext
from pydantic_ai.models.anthropic import AnthropicCompaction


# Define the output
# ↳ The answer is validated against it. Errors are sent back to the model to fix
class Sentiment(BaseModel):
    customer_name: str
    label: Literal['positive', 'negative', 'neutral']
    score: float = Field(ge=-1, le=1)


# Define the dependencies
# ↳ Injected at run time, read through `ctx.deps`
@dataclass
class SupportDependencies:
    customer_name: str


# Define a capability, a reusable bundle of instructions and tools
reviews = Capability[SupportDependencies](id='reviews', description='Fetch recent review snippets for a product.')

# ↳ Instructions — added to the system prompt, computed on each run
@reviews.instructions
def add_customer_name(ctx: RunContext[SupportDependencies]) -> str:
    customer_name = ctx.deps.customer_name
    return f"The customer's name is {customer_name}"

# ↳ Tool — the model can call it
#   Its docstring and signature are sent to the model as the tool's description and schema
@reviews.tool
def recent_reviews(ctx: RunContext[SupportDependencies], product: str) -> list[str]:
    """Fetch recent review snippets for a product."""
    if product.lower() == "extract":
        return ['The new release fixed everything I complained about!']
    return []


# Create the agent
agent = Agent("anthropic:claude-sonnet-5-5",
              output_type=Sentiment,
              deps_type=SupportDependencies,
              # ↳ Max retries after a validation error
              retries=3,
              # ↳ Ours, plus a built-in one: summarizes old messages past 100k tokens
              capabilities=[reviews, AnthropicCompaction(token_threshold=100_000)],
        )

# Run
if __name__ == "__main__":
    deps = SupportDependencies(customer_name="John Doe")
    result = agent.run_sync('How are people feeling about the "Extract" app?', deps=deps)
    print(result.output)
