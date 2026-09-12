"""Exercise the real indra launcher and preserve complete output for review."""
import os
import subprocess
import time
from pathlib import Path

root = Path(__file__).resolve().parents[1]
env = dict(os.environ, PYTHONUTF8="1", PYTHONIOENCODING="utf-8")
for model in ("gemma-2-2b-it", "phi-4-mini-instruct", "qwen3.5-4b"):
    prompt = "What is 17 + 25? Answer in one short sentence."
    start = time.monotonic()
    result = subprocess.run(
        [str(root / "bin/indra.cmd"), "--model", model, "chat", "-q", prompt, "--cli"],
        cwd=root, env=env, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=240,
    )
    output = result.stdout + result.stderr
    (root / "runtime" / f"check-{model}.log").write_text(output, encoding="utf-8")
    print(f"MODEL {model}, exit={result.returncode}, seconds={time.monotonic()-start:.1f}", flush=True)
    print(output, flush=True)
