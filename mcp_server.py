import os
from mcp.server.fastmcp import FastMCP
from glixin import GlixinClient

# Initialize FastMCP server
mcp = FastMCP("Glixin SPD Server")
client = GlixinClient()

@mcp.tool()
def dehydrate_prompt(prompt: str, policy: str = "standard") -> str:
    """Dehydrate and compress LLM prompts to reduce token overhead and latency.
    
    Args:
        prompt: The raw text prompt to compress.
        policy: Dehydration policy level ('standard', 'aggressive', 'conservative').
    """
    try:
        response = client.dehydrate_prompt(prompt=prompt, policy=policy)
        return (
            f"Status: {response.get('status')}\n"
            f"Original Tokens: {response.get('original_tokens')}\n"
            f"Dehydrated Tokens: {response.get('dehydrated_tokens')}\n"
            f"Compression Ratio: {response.get('compression_ratio')}\n"
            f"Dehydrated Prompt:\n{response.get('dehydrated_prompt')}"
        )
    except Exception as e:
        return f"Dehydration failed: {str(e)}"

if __name__ == "__main__":
    mcp.run()