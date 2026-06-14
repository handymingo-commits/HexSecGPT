import requests

API_KEY = "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"
url = "https://openrouter.ai/api/v1/models"

headers = {
    "Authorization": f"Bearer {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}"
}

r = requests.get(url, headers=headers)
data = r.json()["data"]

free_models = []

for m in data:
    model_id = m["id"]
    pricing = m.get("pricing", {})

    is_free_suffix = model_id.endswith(":free")
    is_free_pricing = (
        pricing.get("prompt", 1) == 0 and
        pricing.get("completion", 1) == 0
    )
