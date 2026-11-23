"""Consolida catálogos dos radares anteriores (um por branch) + radar do dia em catalogo/catalogo-central.csv.
Uso: python3 scripts/consolidar_catalogo.py <dir_com_catalogos_anteriores> <referencias_do_dia.json>"""
import csv, json, os, re, sys

COLS = ["data_descoberta","url","titulo","tecnica","categoria","nicho","dificuldade","status_implementacao","verificacao"]

def norm_url(u):
    u = (u or "").strip().rstrip(".")
    m = re.search(r"(?:v=|shorts/|youtu\.be/|embed/)([\w-]{11})", u)
    if "youtube" in u and m: return "yt:" + m.group(1)
    return u.lower()

def j(v):
    if isinstance(v, list): return "; ".join(map(str, v))
    return "" if v is None else str(v)

def from_obj(o):
    return {
        "data_descoberta": o.get("data") or o.get("data_descoberta") or "",
        "url": o.get("url",""),
        "titulo": o.get("titulo") or o.get("anunciante") or o.get("origem") or "",
        "tecnica": j(o.get("tecnica")),
        "categoria": j(o.get("categoria")),
        "nicho": j(o.get("nicho") or o.get("nichos")),
        "dificuldade": j(o.get("dificuldade")),
        "status_implementacao": j(o.get("status") or o.get("status_implementacao")),
        "verificacao": j(o.get("verificado") or o.get("status_verificacao") or ("link de busca; vídeo não assistido" if "facebook.com/ads" not in o.get("url","") else "Ad Library; criativo não inspecionado")),
    }

rows = {}
def add(r):
    k = norm_url(r["url"])
    if not k: return
    if k in rows:  # mantém a primeira descoberta, registra redescoberta
        if r["data_descoberta"] and r["data_descoberta"] not in rows[k]["verificacao"]:
            rows[k]["verificacao"] += f" | revisto {r['data_descoberta']}"
        return
    rows[k] = r

prev_dir, today = sys.argv[1], sys.argv[2]
for f in sorted(os.listdir(prev_dir)):
    p = os.path.join(prev_dir, f)
    if f.endswith(".json"):
        d = json.load(open(p, encoding="utf-8"))
        items = d.get("referencias", []) if isinstance(d, dict) else d
        for o in items: add(from_obj(o))
    elif f.endswith(".csv"):
        for o in csv.DictReader(open(p, encoding="utf-8")):
            o = {k: v for k, v in o.items() if k}
            o.setdefault("data", o.get("data_descoberta"))
            add(from_obj(o))
for o in json.load(open(today, encoding="utf-8")): add(from_obj(o))

out = sorted(rows.values(), key=lambda r: (r["data_descoberta"], r["categoria"]))
os.makedirs("catalogo", exist_ok=True)
with open("catalogo/catalogo-central.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=COLS); w.writeheader(); w.writerows(out)
print(len(out), "referências únicas")
