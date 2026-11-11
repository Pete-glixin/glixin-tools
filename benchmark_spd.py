import os
import time
from glixin import GlixinClient

def run_benchmark():
    # Automatically picks up $env:GLIXIN_API_KEY
    client = GlixinClient()
    
    sample_prompt = (
        "Explain quantum computing in complete detail, covering superposition, "
        "entanglement, gate operations, error correction, and near-term NISQ applications "
        "in pharmaceutical research and cryptographic analysis."
    )
    
    print("--- Glixin SPD Benchmark Suite ---")
    print(f"Original Prompt Length: {len(sample_prompt.split())} words\n")
    
    start_time = time.time()
    response = client.dehydrate_prompt(prompt=sample_prompt, policy="standard")
    duration = time.time() - start_time
    
    print(f"Dehydration completed in {duration:.3f} seconds.")
    print(f"Original Tokens: {response.get('original_tokens')}")
    print(f"Dehydrated Tokens: {response.get('dehydrated_tokens')}")
    print(f"Compression Ratio: {response.get('compression_ratio')}")
    print(f"Optimized Payload:\n{response.get('dehydrated_prompt')}")

if __name__ == "__main__":
    run_benchmark()