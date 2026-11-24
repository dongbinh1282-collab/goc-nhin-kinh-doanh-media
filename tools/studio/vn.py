import sys
from pathlib import Path
from vieneu._v3_turbo_engine import onnx_runtime_lite as o
_orig=o.OnnxV3LiteEngine._fetch
def _f(repo,files,sub):
    p=Path(repo)
    if p.exists(): return p/(sub or '')
    return _orig(repo,files,sub)
o.OnnxV3LiteEngine._fetch=staticmethod(_f)
from vieneu import Vieneu
def load(): return Vieneu(backbone_repo=__import__('os').environ.get('VIENEU_DIR','/home/claude/vn/v3t'))
