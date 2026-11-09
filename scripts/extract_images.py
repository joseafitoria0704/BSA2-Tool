"""
Extrae imágenes base64 del Concept Report y las guarda en docs/assets/metodologia/.
Las referencias tienen el formato: [imageN]: data:image/png;base64,...

El Concept Report ya no forma parte del árbol del repositorio (se retiró la carpeta
referencias/), pero se conserva en el historial. Para recuperarlo:

    git show "v0.3.0:referencias/01_metodologia/BSA 2.0 Concept Report.md" > concept_report.md
    python scripts/extract_images.py concept_report.md
"""
import sys
import re
import base64
import os
from pathlib import Path

SOURCE = Path(sys.argv[1] if len(sys.argv) > 1 else "concept_report.md")
OUTPUT = Path("docs/assets/metodologia")
OUTPUT.mkdir(parents=True, exist_ok=True)

pattern = re.compile(r'^\[(image\d+)\]:\s*<?data:image/(\w+);base64,(.+?)>?$')

saved = []
with open(SOURCE, "r", encoding="utf-8") as f:
    for line in f:
        m = pattern.match(line.strip())
        if m:
            name, ext, b64data = m.group(1), m.group(2), m.group(3)
            ext = ext if ext != "jpeg" else "jpg"
            out_path = OUTPUT / f"{name}.{ext}"
            try:
                img_bytes = base64.b64decode(b64data)
                out_path.write_bytes(img_bytes)
                saved.append(str(out_path))
                print(f"  Guardado: {out_path} ({len(img_bytes):,} bytes)")
            except Exception as e:
                print(f"  ERROR {name}: {e}")

print(f"\nTotal: {len(saved)} imagen(es) extraída(s).")
