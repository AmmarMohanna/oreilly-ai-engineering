"""Execute every lab in its own fresh kernel; retain outputs and fail honestly.

In Colab, set GOOGLE_API_KEY from userdata in the parent process, then invoke
this script with subprocess.run. The key is inherited, never written to disk.
Install nbformat nbclient ipykernel before running. Use a CUDA/T4 runtime.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import time

import nbformat
from nbclient import NotebookClient


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--only', nargs='*', type=int)
    parser.add_argument('--output', default='validation-results')
    parser.add_argument('--gemini-branch', action='store_true', help='Also execute notebook 1 with its Gemini toggle enabled')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    out = Path(args.output).resolve()
    out.mkdir(parents=True, exist_ok=True)
    paths = sorted(root.glob('Day */*.ipynb'), key=lambda p: int(p.name.split('.')[0]))
    results = []
    for path in paths:
        number = int(path.name.split('.')[0])
        if args.only and number not in args.only:
            continue
        variants = ['default', 'gemini'] if number == 1 and args.gemini_branch else ['default']
        for variant in variants:
            nb = nbformat.read(path, as_version=4)
            if variant == 'gemini':
                for cell in nb.cells:
                    cell.source = cell.source.replace('use_gemini = False', 'use_gemini = True')
            run_dir = out / f'{number:02d}-{variant}'
            run_dir.mkdir(exist_ok=True)
            record = {'number': number, 'variant': variant, 'notebook': str(path.relative_to(root)),
                      'source_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                      'status': 'running', 'cells_total': sum(c.cell_type == 'code' for c in nb.cells)}
            started = time.monotonic()
            print(f'START {number} {variant}', flush=True)
            try:
                nbformat.validate(nb)
                client = NotebookClient(nb, timeout=1800, kernel_name='python3',
                                        resources={'metadata': {'path': str(run_dir)}})
                client.execute()
                record['status'] = 'passed'
            except Exception as exc:
                record['status'] = 'failed'
                message = str(exc)
                for name in ('GOOGLE_API_KEY', 'GEMINI_API_KEY', 'HF_TOKEN'):
                    if os.environ.get(name): message = message.replace(os.environ[name], '[REDACTED]')
                record['error'] = type(exc).__name__ + ': ' + message[-4000:]
            record['seconds'] = round(time.monotonic() - started, 1)
            record['cells_executed'] = sum(c.cell_type == 'code' and c.execution_count is not None for c in nb.cells)
            nbformat.write(nb, run_dir / path.name)
            results.append(record)
            (out/'summary.json').write_text(json.dumps(results, indent=2))
            print(f"RESULT {number} {variant}: {record['status']} ({record['seconds']}s; {record['cells_executed']}/{record['cells_total']} cells)", flush=True)
            if record.get('error'): print(record['error'][-1200:], flush=True)
    environment = {'python': platform.python_version(), 'platform': platform.platform()}
    try:
        import torch
        environment.update(torch=torch.__version__, cuda=torch.cuda.is_available(),
                           gpu=torch.cuda.get_device_name(0) if torch.cuda.is_available() else None)
    except ImportError: pass
    (out/'environment.json').write_text(json.dumps(environment, indent=2))
    with (out/'packages.txt').open('w') as f:
        subprocess.run([os.sys.executable, '-m', 'pip', 'freeze'], stdout=f, check=True)
    raise SystemExit(1 if any(r['status'] != 'passed' for r in results) else 0)


if __name__ == '__main__':
    main()
