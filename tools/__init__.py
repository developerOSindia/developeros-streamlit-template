"""
DeveloperOS Tools Package & Registration Bootstrap.
Each tool is registered into the ToolRegistry. Tools can be installed or removed
independently without impacting other utilities in the suite.
"""

from tools.registry import registry, ToolDefinition, register_tool

# Import views
from tools.text_analyzer_view import render_text_analyzer_view
from tools.hash_generator_view import render_hash_generator_view
from tools.json_validator_view import render_json_validator_view


def init_tools():
    """Initializes and registers all suite tools."""
    # Register 1: Text Analyzer
    register_tool(ToolDefinition(
        id="tool-text-analyzer",
        name="Text Analyzer & Metrics",
        description="Inspect character counts, word density, reading duration, and Shannon entropy.",
        category="Text & Strings",
        version="1.0.0",
        ui_entrypoint=render_text_analyzer_view,
        core_module="core.text_analyzer",
        input_output_spec={"input": "text/plain (max 1MB)", "output": "dict metrics"},
        privacy_classification="client_side",
        dependency_requirements=["streamlit>=1.38.0"],
        deployment_support=["streamlit_community_cloud", "docker"],
        documentation_link="https://developeros.in/docs/tools/text-analyzer",
        related_tools=["tool-hash-generator", "tool-json-validator"],
    ))

    # Register 2: Hash Generator
    register_tool(ToolDefinition(
        id="tool-hash-generator",
        name="Multi-Algorithm Hasher & HMAC",
        description="Compute SHA-256, SHA-512, MD5 hashes, and HMAC digests client-side.",
        category="Security & Crypto",
        version="1.0.0",
        ui_entrypoint=render_hash_generator_view,
        core_module="core.hash_generator",
        input_output_spec={"input": "text/plain (max 1MB)", "output": "hash digests"},
        privacy_classification="client_side",
        dependency_requirements=["streamlit>=1.38.0"],
        deployment_support=["streamlit_community_cloud", "docker"],
        documentation_link="https://developeros.in/docs/tools/hash-generator",
        related_tools=["tool-text-analyzer", "tool-json-validator"],
    ))

    # Register 3: JSON Validator
    register_tool(ToolDefinition(
        id="tool-json-validator",
        name="JSON Formatter & Schema Validator",
        description="Inspect, validate, prettify, and minify JSON payloads client-side.",
        category="Data & Format",
        version="1.0.0",
        ui_entrypoint=render_json_validator_view,
        core_module="core.json_validator",
        input_output_spec={"input": "application/json (max 2MB)", "output": "formatted JSON"},
        privacy_classification="client_side",
        dependency_requirements=["streamlit>=1.38.0"],
        deployment_support=["streamlit_community_cloud", "docker"],
        documentation_link="https://developeros.in/docs/tools/json-validator",
        related_tools=["tool-text-analyzer", "tool-hash-generator"],
    ))


# Automatically initialize default tools upon import
init_tools()

__all__ = ["registry", "init_tools", "ToolDefinition", "register_tool"]
