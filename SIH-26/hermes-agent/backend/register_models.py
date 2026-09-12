import httpx
from pathlib import Path

key = 'wb_live_1234567890abcdef1234567890abcdef'

models_to_add = [
    {
        'name': 'qwen3.5-4b',
        'source': {'type':'local_path','path': 'models/Qwen_Qwen3.5-4B-Q4_K_M.gguf'},
        'backend': 'llamaswap', 'type': 'text', 'task_tags': ['chat','coding'], 'pinned': True, 'vram_mb': 3100
    },
    {
        'name': 'hermes-3-llama-8b',
        'source': {'type':'local_path','path': 'models/Hermes-3-Llama-3.1-8B-Q4_K_M.gguf'},
        'backend': 'llamaswap', 'type': 'text', 'task_tags': ['chat','reasoning'], 'pinned': True, 'vram_mb': 5500
    },
    {
        'name': 'gemma-2-2b-it',
        'source': {'type':'local_path','path': 'models/gemma-2-2b-it-Q4_K_M.gguf'},
        'backend': 'llamaswap', 'type': 'text', 'task_tags': ['chat'], 'pinned': False, 'vram_mb': 2500
    },
    {
        'name': 'qwen2-vl-ocr-2b-instruct',
        'source': {'type':'local_path','path': 'models/Qwen2-VL-OCR-2B-Instruct.Q4_K_M.gguf'},
        'backend': 'llamaswap', 'type': 'vlm', 'task_tags': ['vision','ocr'], 'pinned': False, 'vram_mb': 3500
    }
]

with httpx.Client(base_url='http://127.0.0.1:8000', headers={'Authorization': 'Bearer ' + key}) as c:
    for m in models_to_add:
        r = c.post('/v1/models', json=m)
        print(f"Registering {m['name']}: {r.status_code} - {r.text}")
