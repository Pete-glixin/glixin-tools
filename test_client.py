from glixin import GlixinClient

# Test initialization (will validate environment key checking)
try:
    client = GlixinClient(api_key="test-mock-key")
    print("SUCCESS: GlixinClient initialized!")
    print("Base URL configured as:", client.base_url)
except Exception as e:
    print("Error:", e)