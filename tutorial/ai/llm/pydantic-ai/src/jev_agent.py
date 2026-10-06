"""
Pydantic AI — the same agent on Jev, a decision model.

Jev doesn't write text: it answers typed questions, each with a confidence score.
Read llm_agent.py first, only the differences are commented here.

Jev can't call tools. Pydantic AI asks it questions and makes the calls itself:
  1. Pydantic AI asks: "What to do?", with options described by their docstrings:
       - `recent_reviews` (our tool):
         "Fetch recent review snippets for a product."
       - answer (`ReviewMood`, the output schema, which Pydantic AI declares as a tool too):
         "Give the verdict on the product's sentiment, from the reviews already fetched."
     Jev answers: `recent_reviews` (no reviews fetched yet)
  2. Pydantic AI asks: "Which product?", with options 'Extract' and 'Compose'
     Jev answers: 'Extract'
  3. Pydantic AI calls `recent_reviews(product='Extract')` and adds the reviews to the conversation
  4. Pydantic AI doesn't ask "What to do?" again: a tool is offered once, so answer is left
  5. Pydantic AI asks: each field's question ("What is the overall sentiment...?", ...)
     Jev answers: `ReviewMood(label='positive', positivity=0.95)`

Try it:
    python jev_agent.py
"""

from dataclasses import dataclass
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field
from pydantic_ai import Agent, Capability, RunContext


# Define the output
class Sentiment(BaseModel):
    customer_name: str
    label: Literal['positive', 'negative', 'neutral']
    score: float = Field(ge=-1, le=1)

# Jev's output schema: options and probabilities only, no free text
# ↳ Docstrings are sent to Jev: the class one describes the answer option (see the module docstring),
#   each field's one is its question
class ReviewMood(BaseModel):
    """Give the verdict on the product's sentiment, from the reviews already fetched."""

    # ↳ Turns the field docstrings below into schema descriptions
    model_config = ConfigDict(use_attribute_docstrings=True)

    label: Literal['positive', 'negative', 'neutral']
    """What is the overall sentiment of the reviews?"""

    # ↳ A probability, so in [0, 1] instead of [-1, 1]
    positivity: float = Field(ge=0, le=1)
    """Are the reviews positive?"""


# Define the dependencies
@dataclass
class SupportDependencies:
    customer_name: str


# Define a capability
reviews = Capability[SupportDependencies](id='reviews', description='Fetch recent review snippets for a product.')

@reviews.instructions
def add_customer_name(ctx: RunContext[SupportDependencies]) -> str:
    customer_name = ctx.deps.customer_name
    return f"The customer's name is {customer_name}"

# ↳ `Literal` instead of `str` — Jev picks an option, it can't write one (see the module docstring)
@reviews.tool
def recent_reviews(ctx: RunContext[SupportDependencies], product: Literal['Extract', 'Compose']) -> list[str]:
    """Fetch recent review snippets for a product."""
    if product.lower() == "extract":
        return ['The new release fixed everything I complained about!']
    return []


# Create the agent
# ↳ Only the model changes
agent = Agent("typesafe:jev-latest",
              output_type=ReviewMood,
              deps_type=SupportDependencies,
              retries=3,
              capabilities=[reviews],
        )

# Run
if __name__ == "__main__":
    deps = SupportDependencies(customer_name="John Doe")
    result = agent.run_sync('How are people feeling about the "Extract" app?', deps=deps)

    # ↳ Same `Sentiment` as llm_agent.py, built from what we already know
    mood = result.output
    print(Sentiment(customer_name=deps.customer_name, label=mood.label, score=2 * mood.positivity - 1))
    # ↳ Confidence per field (e.g. {'label': 0.97, 'positivity': 0.93})
    print(result.response.provider_details['confidence'])
