from collections.abc import AsyncIterable

from fastapi import FastAPI
# `EventSourceResponse` sets the correct headers automatically:
#   - Content-Type: text/event-stream
#   - Cache-Control: no-cache
#   - X-Accel-Buffering: no  (prevents Nginx from buffering the stream)
# `ServerSentEvent` is a dataclass representing a single SSE frame
from fastapi.sse import EventSourceResponse, ServerSentEvent

app = FastAPI()

tokens = ["Hello", "World", "!"]

# `response_class=EventSourceResponse` tells FastAPI two things:
#   1. Wrap the generator's output in the SSE wire format automatically.
#   2. Advertise the correct Content-Type in the OpenAPI schema.
#
# The return type annotation `AsyncIterable[ServerSentEvent]` tells FastAPI 
# to do the following:
#   1. VALIDATE each yielded item against the declared type.
#   2. SERIALIZE it via Pydantic (Rust-side, for better performance).
#   3. DOCUMENT the response schema in OpenAPI / Swagger UI.
# Omitting it falls back to the slower `jsonable_encoder` path with no validation.
#
# You can populate optional SSE fields on `ServerSentEvent`:
#   - `event`   → custom event name  (event: my_event\n)
#   - `id`      → event ID for retry (id: 42\n)
#   - `retry`   → reconnect delay ms (retry: 3000\n)
#   - `comment` → keep-alive comment (: ping\n)
#
# FastAPI also sends a keep-alive ping comment every 15 seconds automatically,
# preventing proxies from closing idle connections.
@app.get("/stream", response_class=EventSourceResponse)
async def sse_tokens() -> AsyncIterable[ServerSentEvent]: 
    for token in tokens:
        # Each `yield` pushes one SSE frame to the client immediately.
        # The connection stays open between yields — the client does NOT
        # need to reconnect to receive the next event.
        # `data` is always JSON-encoded by FastAPI before sending.
        yield ServerSentEvent(data=token)
    
    # `raw_data` sends the string verbatim in the `data:` field,
    # bypassing JSON encoding entirely — appropriate for sentinel values.
    # Note: `data` and `raw_data` are mutually exclusive on a single ServerSentEvent.
    # "[DONE]" is a conventional sentinel (popularised by OpenAI's API) that tells
    # the client-side JS to close the EventSource, since SSE has no built-in
    # "stream finished" signal at the protocol level.
    yield ServerSentEvent(raw_data="[DONE]")

