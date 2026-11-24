"""Gera catalogo/referencias.csv a partir de catalogo/referencias.json e checa URLs duplicadas."""
import csv, json, pathlib, sys
base = pathlib.Path(__file__).resolve().parent.parent / "catalogo"
refs = json.loads((base / "referencias.json").read_text(encoding="utf-8"))
urls = [r["url"] for r in refs]
dup = {u for u in urls if urls.count(u) > 1}
if dup:
    sys.exit(f"URLs duplicadas: {dup}")
cols = ["id", "data_descoberta", "titulo", "url", "tecnica", "categoria", "nichos", "dificuldade", "status_implementacao"]
with open(base / "referencias.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(cols)
    for r in refs:
        w.writerow([("; ".join(r[c]) if isinstance(r[c], list) else r[c]) for c in cols])
print(f"{len(refs)} referências, sem duplicatas")
