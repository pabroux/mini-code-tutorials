# FastAPI Server-Sent-Events (SSE) as first-class citizen

This tutorial shows how to create a Server-Sent Events (SSE) response in FastAPI, now supported as a first-class feature since version `0.135.0`.

## What?

SSE is an HTTP protocol for unidirectional streaming from server to client. The connection stays open after the initial request, and the server pushes text events in a simple format:
```
data: {"token": "Hello"}

data: {"token": " world"}
```
SSE is the go-to transport for LLM token streaming — it's what powers the token-by-token output you see in ChatGPT, Claude, and similar interfaces. It's also used for live notifications, log tailing, and progress reporting. Browsers support it natively via the [EventSource API](https://developer.mozilla.org/en-US/docs/Web/API/EventSource).
Since FastAPI `0.135.0`, SSE is a first-class citizen. You no longer need to manually wrap a generator in [StreamingResponse](https://fastapi.tiangolo.com/advanced/custom-response/#streamingresponse) or manage headers yourself — just declare `response_class=EventSourceResponse` and yield from your path operation. FastAPI handles serialization, keep-alive pings, and proxy headers out of the box.

## How to use the tutorial?

- Script

## Requirements

- [uv](https://docs.astral.sh/uv/) or [mise](https://mise.jdx.dev).

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

Everything is well explained in the `main.py` script, in the `src` folder.

To test, run FastAPI in the dev mode as such:
```zsh
fastapi dev src/main.py
```

Now, you can naviguate to `http://localhost:8080/docs` and test the SSE endpoint.

## Resources

- [EventSource API](https://developer.mozilla.org/en-US/docs/Web/API/EventSource) by Mozilla
- [HTML specification: SSE](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events) by WHATWG
- [SSE documentation](https://fastapi.tiangolo.com/tutorial/server-sent-events/) by FastAPI
