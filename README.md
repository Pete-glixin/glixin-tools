# glixin-tools

Official lightweight Python client for Glixin Sovereign Cloud & Token Economics APIs. 

Provides unified client access to three core intelligence and policy enforcement utilities:
1. **SPD (Semiotic Prompt Dehydrator)** � Token optimization and semantic compression.
2. **SWD (Semiotic Website Dehydrator)** � High-density semantic DOM and web extraction.
3. **PE Engine (Policy Enforcement)** � Bi-directional transactional screening and token ledger validation.

---

## Installation

Install the package directly from PyPI:

\\\ash
pip install glixin-tools
\\\

---

## Quickstart

Initialize the \GlixinClient\ using your API key or environment variable (\GLIXIN_API_KEY\):

\\\python
import os
from glixin import GlixinClient

client = GlixinClient(api_key=os.getenv("GLIXIN_API_KEY"))
\\\

### 1. Semiotic Prompt Dehydration (SPD)
\\\python
result = client.dehydrate_prompt(
    prompt="Analyze the distributed transaction pipeline and identify latency bottlenecks.",
    policy="standard"
)
print("Compressed Prompt:", result["dehydrated_prompt"])
print("Compression Ratio:", result["compression_ratio"])
\\\

### 2. Semiotic Website Dehydration (SWD)
\\\python
extraction = client.extract_website("https://example.com")
print("Extracted Payload:", extraction)
\\\

### 3. Policy Enforcement (PE) Engine
\\\python
screening = client.screen_transaction(
    transaction_data={"payload": "Execute settlement pipeline"},
    service_level="Bronze"
)
print("Decision:", screening["decision"])
\\\

---

## License & Support
* **Documentation & Web:** [glixin.com](https://glixin.com/)
* **Support:** support@glixin.com
