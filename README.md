# DeveloperOS Streamlit Suite Template

[![Live App](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B.svg)](https://devos-template.streamlit.app)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.38%2B-FF4B4B.svg)](https://streamlit.io)
[![Privacy: Client--Side](https://img.shields.io/badge/Privacy-Zero--Storage-10b981.svg)](https://developeros.in/privacy)

A production-ready, modular Streamlit template designed for building independently deployable tool suites within the [DeveloperOS](https://developeros.in) open-source ecosystem.

---

> 🚀 **Live Application**: [https://devos-template.streamlit.app](https://devos-template.streamlit.app)


## 🌟 Key Features

- **Decoupled Architecture**: Pure Python business logic in `core/` completely isolated from Streamlit UI in `tools/`.
- **Plug-and-Play Tool Contract**: Utilities self-register into `tools/registry.py` with 13 metadata fields. Add or remove tools without breaking the suite.
- **DeveloperOS Design System**: Supported native theme settings in `.streamlit/config.toml` matching canonical brand tokens (`#2563eb` primary, `#0f172a` canvas, `#1e293b` surface).
- **Zero-Trust Ephemeral Privacy**: Strict in-memory processing guarantees; no user payloads or inputs are ever saved to disk or sent to third parties.
- **Multi-Tool Automatic Navigation**: Category filtering, live search, and related-tool recommendation cards.
- **Production-Ready CI & Packaging**: Pinned dependencies, pre-configured Ruff linter, Pytest test runner, and GitHub Actions CI.

---

## 📁 Repository Layout

```
developeros-streamlit-template/
├── app.py                      # Main Streamlit application entrypoint
├── manifest.yaml               # Suite metadata & tool inventory
├── requirements.txt            # Locked runtime dependencies
├── pyproject.toml              # Build & linter configuration
├── LICENSE                     # MIT License
├── CONTRIBUTING.md             # Developer guide for adding new utilities
├── .streamlit/
│   └── config.toml             # Native theme & server configuration
├── .github/workflows/
│   └── ci.yml                  # Automated GitHub Actions test pipeline
├── assets/                     # Portable branding assets (SVG logos, theme tokens)
│   ├── logo.svg
│   └── theme.json
├── components/                 # Reusable DeveloperOS UI components
│   ├── header.py               # Standard top navigation & branding
│   ├── footer.py               # Backlinks to developeros.in & MIT notice
│   ├── privacy.py              # Zero-storage assurance badge
│   ├── navigation.py           # Sidebar search & category filter
│   ├── alerts.py               # WCAG AA status banners
│   └── related_tools.py        # Recommendation card grid
├── core/                       # Pure business logic (ZERO Streamlit imports)
│   ├── text_analyzer.py        # Text density, reading time & Shannon entropy
│   ├── hash_generator.py       # SHA-256, SHA-512, MD5, HMAC & safe compare
│   └── json_validator.py       # JSON syntax check, minifier & formatter
├── tools/                      # Tool plugin implementations & views
│   ├── registry.py             # ToolDefinition contract & singleton registry
│   ├── text_analyzer_view.py   # UI presentation for Text Analyzer
│   ├── hash_generator_view.py  # UI presentation for Hash Generator
│   ├── json_validator_view.py  # UI presentation for JSON Formatter
│   └── __init__.py             # Auto-registration bootstrap
├── pages/                      # Optional multi-page Streamlit tabs
│   ├── 1_Catalog.py            # Searchable suite catalog
│   └── 2_About.py              # Architecture & privacy guarantees
└── tests/                      # Automated test suite
    ├── test_core_text_analyzer.py
    ├── test_core_hash_generator.py
    ├── test_core_json_validator.py
    ├── test_registry.py
    └── test_manifest.py
```

---

## 🚀 Quickstart

### 1. Prerequisites
- Python 3.12+
- `pip` or `uv`

### 2. Local Installation
```bash
# Clone or copy the template
cd developeros-streamlit-template

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Run Application Locally
```bash
streamlit run app.py
```
Open your browser to `http://localhost:8501`.

### 4. Run Automated Tests
```bash
python3 -m unittest discover -s tests -p "test_*.py"
```

---

## 🛠️ How to Create a New Suite from this Template

1. **Copy the Template Folder**:
   ```bash
   cp -r infrastructure/developeros-streamlit-template suites/suite-<your-domain>
   ```
2. **Update Metadata in `manifest.yaml`**:
   - Set `suite_id: "suite-<your-domain>"`
   - Set `name: "DeveloperOS <Domain> Suite"`
   - Set `slug: "<your-domain>"`
   - Set `category: "<Category Name>"`
3. **Customize `pyproject.toml` and `README.md`**:
   - Update project title, package name, and repository URL.
4. **Scaffold Your Domain Tools** into `core/` and `tools/`.

---

## 🧩 How to Add a New Tool (Tool Plugin Contract)

Every utility follows a 3-step registration process:

### Step 1: Author Pure Business Logic (`core/<tool_slug>.py`)
*Strict Rule: Do not import Streamlit in `core/`.*
```python
# core/uuid_generator.py
import uuid
from typing import List

def generate_uuids(count: int = 1) -> List[str]:
    """Generates UUIDv4 identifiers."""
    return [str(uuid.uuid4()) for _ in range(min(count, 100))]
```

### Step 2: Implement UI Presentation (`tools/<tool_slug>_view.py`)
```python
# tools/uuid_generator_view.py
import streamlit as st
from core.uuid_generator import generate_uuids
from components.privacy import render_privacy_badge

def render_uuid_generator_view():
    st.markdown("### 🆔 UUIDv4 Generator")
    render_privacy_badge("client_side")
    
    count = st.slider("Quantity", 1, 50, 5)
    if st.button("Generate UUIDs", type="primary"):
        uuids = generate_uuids(count)
        st.code("\n".join(uuids), language="text")
        st.download_button("Download UUIDs", data="\n".join(uuids), file_name="uuids.txt")
```

### Step 3: Register Tool in `tools/__init__.py`
```python
# tools/__init__.py
from tools.registry import register_tool, ToolDefinition
from tools.uuid_generator_view import render_uuid_generator_view

register_tool(ToolDefinition(
    id="tool-uuid-generator",
    name="UUIDv4 Generator",
    description="Generate cryptographically secure version-4 UUID identifiers.",
    category="Identifiers",
    version="1.0.0",
    ui_entrypoint=render_uuid_generator_view,
    core_module="core.uuid_generator",
    input_output_spec={"input": "integer count", "output": "text/plain UUID list"},
    privacy_classification="client_side",
    dependency_requirements=["streamlit>=1.38.0"],
    deployment_support=["streamlit_community_cloud", "docker"],
    documentation_link="https://developeros.in/docs/tools/uuid-generator",
    related_tools=["tool-text-analyzer"]
))
```

### Step 4: Write Unit Tests (`tests/test_core_<tool_slug>.py`)
```python
import unittest
from core.uuid_generator import generate_uuids

class TestUuidGenerator(unittest.TestCase):
    def test_generate(self):
        res = generate_uuids(3)
        self.assertEqual(len(res), 3)
```

Run tests to verify:
```bash
python3 -m unittest discover -s tests -p "test_*.py"
```

---

## ☁️ Deployment Guide

### Deploying to Streamlit Community Cloud
1. Push your standalone suite repository to GitHub under `developerOSindia/<repo-name>`.
2. Visit [share.streamlit.io](https://share.streamlit.io).
3. Connect your repository, branch (`main`), and set Main file path to `app.py`.
4. The `.streamlit/config.toml` will automatically apply DeveloperOS themes.

---

---

## 🏷️ Recommended GitHub Topics

When configuring this repository on GitHub, apply these topics:
`developer-tools` `streamlit` `python` `open-source` `design-system` `template` `developeros`

---

## 📄 License & Ecosystem

This project is licensed under the [MIT License](LICENSE).
Part of the [DeveloperOS Open-Source Tools Ecosystem](https://developeros.in).

- **Live Application**: [https://devos-template.streamlit.app](https://devos-template.streamlit.app)
- **Main Website**: [https://developeros.in](https://developeros.in)
- **Central Tools Directory**: [https://toolkit.developeros.in](https://toolkit.developeros.in)
- **GitHub Organization**: [https://github.com/developerOSindia](https://github.com/developerOSindia)
