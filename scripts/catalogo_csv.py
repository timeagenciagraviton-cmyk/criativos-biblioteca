"""Gera catalogo/referencias.csv a partir de catalogo/referencias.json (colunas do item 8 do radar)."""
import csv, json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
refs = json.loads((root / "catalogo/referencias.json").read_text(encoding="utf-8"))
cols = ["id", "data_descoberta", "url", "tecnica", "categoria", "nichos", "dificuldade", "status_implementacao", "titulo"]
with open(root / "catalogo/referencias.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(cols)
    for r in refs:
        w.writerow(["; ".join(r[c]) if isinstance(r[c], list) else r[c] for c in cols])
# checagem de duplicidade por URL
urls = [r["url"] for r in refs]
dups = {u for u in urls if urls.count(u) > 1}
print(f"{len(refs)} referências; duplicadas: {sorted(dups) or 'nenhuma'}")
