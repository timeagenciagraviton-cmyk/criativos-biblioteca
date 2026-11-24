"""Gera galeria/<data>.html a partir do template e das referências daquela data."""
import json, pathlib, sys
root = pathlib.Path(__file__).resolve().parent.parent
data = sys.argv[1]
refs = [r for r in json.loads((root/"catalogo/referencias.json").read_text(encoding="utf-8")) if r["data_descoberta"] == data]
d, m, y = data[8:], data[5:7], data[:4]
html = (root/"scripts/galeria_template.html").read_text(encoding="utf-8")
html = html.replace("__DATA__", f"{d}/{m}/{y}").replace("__REFS__", json.dumps(refs, ensure_ascii=False).replace("</", "<\\/"))
(root/"galeria"/f"{data}.html").write_text(html, encoding="utf-8")
print(f"galeria/{data}.html com {len(refs)} referências")
