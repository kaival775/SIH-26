from pathlib import Path
import yaml, shutil
from dotenv import dotenv_values,set_key
root=Path.cwd(); backend=root/'hermes-agent/backend'
backup=backend/'data/setup-backup-20260909'; backup.mkdir(exist_ok=True)
for p in [root/'config.yaml', backend/'config/llama-swap.yaml',backend/'.env']:
    dest=backup/(p.parent.name+'-'+p.name)
    if not dest.exists(): shutil.copy2(p,dest)
c=yaml.safe_load((root/'config.yaml').read_text(encoding='utf-8'))
c['model'].update(default='qwen3.5-4b',base_url='http://127.0.0.1:8000/v1',context_length=16384,max_tokens=2048)
p=c['providers']['workbench']; p.update(api='http://127.0.0.1:8000/v1',base_url='http://127.0.0.1:8000/v1',context_length=16384,default_model='qwen3.5-4b')
p['models']={'qwen3.5-4b':{'context_length':16384}}
c['compression'].update(enabled=True,threshold=0.7,target_ratio=0.35,protect_last_n=4)
c.setdefault('auxiliary',{})['compression']={'provider':'workbench','model':'qwen3.5-4b','base_url':'http://127.0.0.1:8000/v1','context_length':16384}
(root/'config.yaml').write_text(yaml.safe_dump(c,sort_keys=False),encoding='utf-8')
cmd=f'"{(backend/"bin/llama-server.exe").as_posix()}" --host 127.0.0.1 --port ${{PORT}} --model "{(backend/"models/Qwen_Qwen3.5-4B-Q4_K_M.gguf").as_posix()}" --alias qwen3.5-4b --n-gpu-layers 99 --ctx-size 16384 --parallel 1 --batch-size 256 --ubatch-size 128 --threads 8 --flash-attn on --cache-type-k q8_0 --cache-type-v q8_0 --jinja --reasoning-budget 0'
(backend/'config/llama-swap.yaml').write_text(yaml.safe_dump({'healthCheckTimeout':180,'models':{'qwen3.5-4b':{'cmd':cmd,'ttl':0}}},sort_keys=False))
for k,v in {'LLAMASWAP_BIN':str(backend/'bin/llama-swap.exe'),'PUBLIC_API_BASE':'http://127.0.0.1:8000','WORKBENCH_API_BASE':'http://127.0.0.1:8000'}.items():set_key(str(backend/'.env'),k,v)
# Preserve the corrupt database and use a distinct replacement database.
set_key(str(backend/'.env'),'DB_PATH','data/workbench-local.db')
print('Configured 16K context, compression, local URL, Qwen GPU settings; original files preserved.')
