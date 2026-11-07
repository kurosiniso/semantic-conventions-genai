"""Tests for Ollama semantic conventions.

Runnable directly (``python tests/test_ollama.py``) or under pytest.
"""

from __future__ import annotations

import pytest

from semconv_genai.semconv_model import attribute_specs


class TestOllamaAttributes:
    """Test Ollama-specific attribute definitions."""

    def test_ollama_request_model_exists(self):
        """Verify ollama.request.model attribute is defined."""
        specs = attribute_specs()
        assert "ollama.request.model" in specs, "ollama.request.model not found in attribute specs"
        attr = specs["ollama.request.model"]
        assert attr.type == "string"
        assert "llama3.2" in attr.examples

    def test_ollama_request_base_url_exists(self):
        """Verify ollama.request.base_url attribute is defined."""
        specs = attribute_specs()
        assert "ollama.request.base_url" in specs, "ollama.request.base_url not found in attribute specs"
        attr = specs["ollama.request.base_url"]
        assert attr.type == "string"
        assert "http://localhost:11434" in attr.examples

    def test_ollama_request_stream_exists(self):
        """Verify ollama.request.stream attribute is defined."""
        specs = attribute_specs()
        assert "ollama.request.stream" in specs, "ollama.request.stream not found in attribute specs"
        attr = specs["ollama.request.stream"]
        assert attr.type == "boolean"

    def test_ollama_request_temperature_exists(self):
        """Verify ollama.request.temperature attribute is defined."""
        specs = attribute_specs()
        assert "ollama.request.temperature" in specs, "ollama.request.temperature not found in attribute specs"
        attr = specs["ollama.request.temperature"]
        assert attr.type == "double"
        assert 0.7 in attr.examples

    def test_ollama_request_top_p_exists(self):
        """Verify ollama.request.top_p attribute is defined."""
        specs = attribute_specs()
        assert "ollama.request.top_p" in specs, "ollama.request.top_p not found in attribute specs"
        attr = specs["ollama.request.top_p"]
        assert attr.type == "double"

    def test_ollama_request_top_k_exists(self):
        """Verify ollama.request.top_k attribute is defined."""
        specs = attribute_specs()
        assert "ollama.request.top_k" in specs, "ollama.request.top_k not found in attribute specs"
        attr = specs["ollama.request.top_k"]
        assert attr.type == "int"

    def test_ollama_request_max_tokens_exists(self):
        """Verify ollama.request.max_tokens attribute is defined."""
        specs = attribute_specs()
        assert "ollama.request.max_tokens" in specs, "ollama.request.max_tokens not found in attribute specs"
        attr = specs["ollama.request.max_tokens"]
        assert attr.type == "int"

    def test_ollama_request_num_predict_exists(self):
        """Verify ollama.request.num_predict attribute is defined."""
        specs = attribute_specs()
        assert "ollama.request.num_predict" in specs, "ollama.request.num_predict not found in attribute specs"
        attr = specs["ollama.request.num_predict"]
        assert attr.type == "int"

    def test_ollama_request_num_ctx_exists(self):
        """Verify ollama.request.num_ctx attribute is defined."""
        specs = attribute_specs()
        assert "ollama.request.num_ctx" in specs, "ollama.request.num_ctx not found in attribute specs"
        attr = specs["ollama.request.num_ctx"]
        assert attr.type == "int"
        assert 2048 in attr.examples

    def test_ollama_response_model_exists(self):
        """Verify ollama.response.model attribute is defined."""
        specs = attribute_specs()
        assert "ollama.response.model" in specs, "ollama.response.model not found in attribute specs"
        attr = specs["ollama.response.model"]
        assert attr.type == "string"

    def test_ollama_response_total_duration_exists(self):
        """Verify ollama.response.total_duration attribute is defined."""
        specs = attribute_specs()
        assert "ollama.response.total_duration" in specs, "ollama.response.total_duration not found in attribute specs"
        attr = specs["ollama.response.total_duration"]
        assert attr.type == "int"

    def test_ollama_response_eval_count_exists(self):
        """Verify ollama.response.eval_count attribute is defined."""
        specs = attribute_specs()
        assert "ollama.response.eval_count" in specs, "ollama.response.eval_count not found in attribute specs"
        attr = specs["ollama.response.eval_count"]
        assert attr.type == "int"


class TestOllamaAttributeValues:
    """Test expected values for Ollama attributes."""

    def test_ollama_provider_name(self):
        """Verify that Ollama provider name is consistent."""
        specs = attribute_specs()
        # Check that gen_ai.provider.name can be set to Ollama
        assert "gen_ai.provider.name" in specs

    def test_ollama_model_examples(self):
        """Verify Ollama model examples are valid."""
        specs = attribute_specs()
        model_attr = specs["ollama.request.model"]
        # Check that common Ollama models are in examples
        assert "llama3.2" in model_attr.examples
        assert "mistral" in model_attr.examples
        assert "phi3" in model_attr.examples
        assert "gemma2" in model_attr.examples

    def test_ollama_base_url_examples(self):
        """Verify Ollama base URL examples are valid."""
        specs = attribute_specs()
        url_attr = specs["ollama.request.base_url"]
        assert "http://localhost:11434" in url_attr.examples
        assert "https://ollama.example.com" in url_attr.examples


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
