from pathlib import Path
import yaml
p=Path('hermes-agent/backend/config/llama-swap.yaml');c=yaml.safe_load(p.read_text());c['models']['qwen3.5-4b']['cmd']+=' --reasoning off --predict 2048';p.write_text(yaml.safe_dump(c,sort_keys=False))
p=Path('config.yaml');c=yaml.safe_load(p.read_text());c['auxiliary']['title_generation']={'provider':'workbench','model':'qwen3.5-4b','max_tokens':64};c['auxiliary']['compression']['max_tokens']=2048;c['mcp_servers']['clickup']['enabled']=False;p.write_text(yaml.safe_dump(c,sort_keys=False))
