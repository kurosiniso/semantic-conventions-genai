<!--- Hugo front matter used to generate the website version of this page:
linkTitle: Ollama
--->

# Semantic conventions for Ollama

**Status**: [Development][DocumentStatus]

<!-- toc -->

- [Overview](#overview)
- [Spans](#spans)
  - [Client](#client)
- [Attributes](#attributes)
  - [Request Attributes](#request-attributes)
  - [Response Attributes](#response-attributes)
- [Trace examples](#trace-examples)
  - [Chat completion](#chat-completion)
  - [Streaming completion](#streaming-completion)

<!-- tocstop -->

## Overview

[Ollama](https://ollama.ai) is an open-source platform for running large language models locally.
It provides a simple API for interacting with various models including Llama, Mistral, Phi, Gemma, and more.

This document defines semantic conventions for Ollama operations, including spans, attributes, and metrics
for tracing and monitoring Ollama model interactions.

## Spans

### Client

The client span describes an Ollama API call from the client side. It covers the time to receive the
response for non-streaming calls and the time to consume the response stream for streaming calls.

**Span name**: `<span.kind> ollama`

**Span kind**: Client

**Status**: ![Development](https://img.shields.io/badge/-development-blue)

#### Span attributes

The following attributes are specific to Ollama client spans:

| Attribute | Type | Description | Examples | Stability |
|-----------|------|-------------|----------|-----------|
| `ollama.request.model` | string | The name of the Ollama model being used. | `llama3.2`, `mistral` | Development |
| `ollama.request.base_url` | string | The base URL of the Ollama API endpoint. | `http://localhost:11434` | Development |
| `ollama.request.stream` | boolean | Indicates whether the request was made in streaming mode. | `true`, `false` | Development |
| `ollama.request.temperature` | double | The temperature setting for the request. | `0.7`, `0.0` | Development |
| `ollama.request.top_p` | double | The top_p (nucleus) sampling setting. | `0.9`, `1.0` | Development |
| `ollama.request.top_k` | int | The top_k sampling setting. | `50`, `100` | Development |
| `ollama.request.max_tokens` | int | The maximum number of tokens to generate. | `256`, `1024` | Development |
| `ollama.request.stop` | string[] | List of stop sequences. | `["\\n\\n"]` | Development |
| `ollama.request.repeat_penalty` | double | The repeat penalty setting. | `1.1`, `1.2` | Development |
| `ollama.request.seed` | int | The random seed for reproducible output. | `42`, `12345` | Development |
| `ollama.request.num_predict` | int | The maximum number of tokens to generate (Ollama-specific). | `128`, `512` | Development |
| `ollama.request.num_ctx` | int | The size of the context window. | `2048`, `4096` | Development |
| `ollama.request.num_batch` | int | The number of tokens to process in parallel. | `8`, `16` | Development |
| `ollama.request.num_gpu` | int | The number of GPUs to use. | `1`, `2` | Development |
| `ollama.request.main_gpu` | int | The index of the main GPU to use. | `0`, `1` | Development |
| `ollama.request.low_vram` | boolean | Indicates whether to use low VRAM mode. | `true`, `false` | Development |
| `ollama.request.f16_kv` | boolean | Indicates whether to use 16-bit floating point for KV cache. | `true`, `false` | Development |

#### Inherited attributes

In addition to the Ollama-specific attributes above, the following [generic GenAI attributes](
/docs/registry/attributes/gen-ai.md) should be included where applicable:

- `gen_ai.system.name`
- `gen_ai.system.version`
- `gen_ai.provider.name` (SHOULD be set to `"Ollama"`)
- `gen_ai.request.model`
- `gen_ai.request.temperature`
- `gen_ai.request.max_tokens`
- `gen_ai.request.top_p`
- `gen_ai.request.top_k`
- `gen_ai.response.model`
- `gen_ai.response.finish_reason`

## Attributes

### Request Attributes

Request attributes describe the parameters sent to the Ollama API.

#### `ollama.request.model`

**Type**: string

**Description**: The name of the Ollama model being used.

**Examples**:
- `llama3.2`
- `mistral`
- `phi3`
- `gemma2`

**Stability**: Development

**Note**: The model name as provided to the Ollama API. This can include the model name
with or without the registry prefix (e.g., `llama3.2` or `registry.ollama.ai/library/llama3.2`).
Instrumentations SHOULD use the exact value as provided by the user or configuration.

#### `ollama.request.base_url`

**Type**: string

**Description**: The base URL of the Ollama API endpoint.

**Examples**:
- `http://localhost:11434`
- `https://ollama.example.com`

**Stability**: Development

**Note**: This is useful when using a custom or self-hosted Ollama instance.

#### `ollama.request.num_predict`

**Type**: int

**Description**: The maximum number of tokens to generate.

**Examples**:
- `128`
- `512`

**Stability**: Development

**Note**: This is the Ollama-specific parameter name for max_tokens. Instrumentations
MAY set both `ollama.request.num_predict` and `gen_ai.request.max_tokens` for compatibility.

#### `ollama.request.num_ctx`

**Type**: int

**Description**: The size of the context window for the model.

**Examples**:
- `2048`
- `4096`
- `32768`

**Stability**: Development

**Note**: This represents the maximum number of tokens the model can consider from the
conversation history.

### Response Attributes

Response attributes describe the results returned by the Ollama API.

#### `ollama.response.model`

**Type**: string

**Description**: The name of the model that generated the response.

**Examples**:
- `llama3.2`
- `mistral`

**Stability**: Development

#### `ollama.response.total_duration`

**Type**: int

**Description**: The total time in nanoseconds the model took to generate the response.

**Examples**:
- `1500000000` (1.5 seconds)

**Stability**: Development

#### `ollama.response.load_duration`

**Type**: int

**Description**: The time in nanoseconds the model took to load.

**Examples**:
- `500000000` (0.5 seconds)

**Stability**: Development

#### `ollama.response.prompt_eval_count`

**Type**: int

**Description**: The number of tokens in the prompt that were evaluated.

**Examples**:
- `25`

**Stability**: Development

#### `ollama.response.eval_count`

**Type**: int

**Description**: The number of tokens generated by the model.

**Examples**:
- `100`

**Stability**: Development

## Trace examples

### Chat completion

The following example shows a trace for a chat completion request to Ollama:

```
Span: "POST /api/chat"
  Kind: Client
  Attributes:
    - gen_ai.system.name: "MyApp"
    - gen_ai.provider.name: "Ollama"
    - gen_ai.request.model: "llama3.2"
    - ollama.request.model: "llama3.2"
    - ollama.request.base_url: "http://localhost:11434"
    - ollama.request.stream: false
    - ollama.request.temperature: 0.7
    - ollama.request.top_p: 0.9
    - ollama.request.max_tokens: 256
    - gen_ai.request.temperature: 0.7
    - gen_ai.request.max_tokens: 256
    - http.method: "POST"
    - http.url: "http://localhost:11434/api/chat"
    - http.status_code: 200
    - ollama.response.model: "llama3.2"
    - ollama.response.total_duration: 1500000000
    - ollama.response.eval_count: 100
    - gen_ai.response.model: "llama3.2"
    - gen_ai.response.finish_reason: "stop"
```

### Streaming completion

The following example shows a trace for a streaming completion request to Ollama:

```
Span: "POST /api/chat (stream)"
  Kind: Client
  Attributes:
    - gen_ai.system.name: "MyApp"
    - gen_ai.provider.name: "Ollama"
    - gen_ai.request.model: "mistral"
    - ollama.request.model: "mistral"
    - ollama.request.base_url: "http://localhost:11434"
    - ollama.request.stream: true
    - ollama.request.temperature: 0.3
    - gen_ai.request.temperature: 0.3
    - http.method: "POST"
    - http.url: "http://localhost:11434/api/chat"
    - http.status_code: 200
    - ollama.response.model: "mistral"
    - ollama.response.total_duration: 2500000000
    - ollama.response.eval_count: 200
    - gen_ai.response.finish_reason: "stop"
```

[DocumentStatus]: https://github.com/open-telemetry/semantic-conventions/blob/main/docs/registry/stability.md
[generic GenAI attributes]: /docs/registry/attributes/gen-ai.md
