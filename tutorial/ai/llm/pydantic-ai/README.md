# Pydantic AI

This tutorial shows how to build a type-safe agent in Python with [Pydantic AI](https://pydantic.dev/docs/ai/), twice: once on a classic LLM, once on [Jev](https://pydantic.dev/docs/ai/models/typesafe/), a decision model, for the same result.

## What?

Pydantic AI is an agent framework from the Pydantic team. It works with any model (Anthropic, OpenAI, Gemini, Ollama, etc.). It brings the FastAPI feeling to LLM apps: you describe what you want with Python types, and the framework handles validation, schemas and the agent loop.

The script covers its core building blocks:
- **Agent**: the entry point. It holds the model, the configuration, and runs the loop between the LLM and your tools.
- **Structured output**: `output_type` is a Pydantic model. The answer is validated, and validation errors are sent back to the LLM so it can retry.
- **Dependencies**: a dataclass injected on each run and available through a typed `RunContext`.
- **Instructions**: dynamic system prompts computed from the dependencies.
- **Tools**: plain Python functions the LLM can call. Their schema comes from the signature and their description from the docstring.

Going further, **capabilities** bundle instructions, tools and settings into reusable units. You can create your own (like `reviews` in the script) and plug in built-in ones through the same `capabilities=[...]` argument. For example, compaction keeps long conversations within the context window:
```python
agent = Agent("anthropic:claude-sonnet-5-5", capabilities=[reviews, AnthropicCompaction(token_threshold=100_000)])
```

### System 1 vs System 2

A language model reasons step by step and writes text ("System 2"). A **decision model** like TypeSafe's Jev gives the fast, one-look judgement ("System 1"): it answers typed questions about a text, each with a probability, and writes no text. For type-safe outputs, that means no text to parse, no answer outside the options, and a confidence per field. Other decision models (CLM, Laya, or local ones through Ollama) speak the same `/v1/systemone` API through `SystemOneModel`.

In Pydantic AI, an agent built for one runs on the other by changing the model. The only work is shaping the types so that a decision model can answer them:

| | [`llm_agent.py`](https://github.com/pabroux/mini-code-tutorials/blob/master/tutorial/ai/llm/pydantic-ai/src/llm_agent.py) | [`jev_agent.py`](https://github.com/pabroux/mini-code-tutorials/blob/master/tutorial/ai/llm/pydantic-ai/src/jev_agent.py) |
|---|---|---|
| Model | `anthropic:claude-sonnet-5-5` | `typesafe:jev-latest` |
| Output | free-form `str`, `float` in [-1, 1] | `Literal`, `float` in [0, 1] (a probability) |
| Tool argument | `product: str`: the LLM writes it | `product: Literal['Extract', 'Compose']`: Jev picks it, it can't write it |

## How to use the tutorial?

- Script

## Requirements

- [uv](https://docs.astral.sh/uv/) or [mise](https://mise.jdx.dev).

> [!IMPORTANT]
> You'll need an [`ANTHROPIC_API_KEY` environment variable](https://platform.claude.com/settings/keys) for `llm_agent.py`, and a `TYPESAFE_API_KEY` from your TypeSafe account for `jev_agent.py`.

## Installation

If you have mise installed, you can install uv with the following:
```zsh
mise install
```

Once uv available, run the following command to install dependencies:
```zsh
uv sync
```

Finally, activate the virtual environment:
```zsh
source .venv/bin/activate
```

## Usage

Everything is well explained in the [`llm_agent.py`](https://github.com/pabroux/mini-code-tutorials/blob/master/tutorial/ai/llm/pydantic-ai/src/llm_agent.py) and [`jev_agent.py`](https://github.com/pabroux/mini-code-tutorials/blob/master/tutorial/ai/llm/pydantic-ai/src/jev_agent.py) scripts, in the `src` folder. Read `llm_agent.py` first.

To test, run the scripts directly:
```zsh
python src/llm_agent.py
python src/jev_agent.py
```

Both give a validated `Sentiment` object, such as:
```
customer_name='John Doe' label='positive' score=0.9
```

Jev also tells you how sure it is of each field:
```
{'label': 0.97, 'positivity': 0.93}
```

## Resources

- [Pydantic AI documentation](https://pydantic.dev/docs/ai/) by Pydantic
- [Pydantic AI v2: capabilities, a leaner core, and the Harness](https://pydantic.dev/articles/pydantic-ai-v2) by Pydantic
- [Capabilities](https://pydantic.dev/docs/ai/capabilities/overview/) by Pydantic
- [Compaction](https://pydantic.dev/docs/ai/harness/compaction/) by Pydantic
- [Decision models](https://pydantic.dev/docs/ai/models/decision/) by Pydantic
- [TypeSafe (Jev)](https://pydantic.dev/docs/ai/models/typesafe/) by Pydantic
