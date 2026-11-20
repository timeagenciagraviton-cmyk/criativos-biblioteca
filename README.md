# criativos-biblioteca

Biblioteca de referências de edição para o Graviton Video Editor, alimentada pelo Radar Diário de Criativos.

- `catalogo/catalogo-central.csv` — catálogo central (data, URL, técnica, categoria, nicho, dificuldade, status de implementação, nível de verificação). Consolida os radares de 07/11 em diante (89 referências em 20/11).
- `radar/AAAA-MM-DD/` — relatório, fichas (`referencias.json`) e galeria de cada dia.
- `scripts/consolidar_catalogo.py` — refaz o catálogo central a partir dos catálogos anteriores + fichas do dia, sem duplicar URLs.
