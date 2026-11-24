# criativos-biblioteca

Biblioteca de referências de edição audiovisual para o **Graviton Video Editor**, alimentada pelo Radar Diário de Criativos.

| Pasta | Conteúdo |
|---|---|
| `catalogo/referencias.json` | Catálogo central (fonte da verdade): data, URL, técnica, categoria, nicho, dificuldade, status de implementação |
| `catalogo/referencias.csv` | Versão tabular gerada por `scripts/gerar_csv.py` (também checa URLs duplicadas) |
| `relatorios/AAAA-MM-DD-radar.md` | Relatório diário com Top 3 e prioridades |
| `galeria/AAAA-MM-DD.html` | Galeria visual do dia, gerada por `scripts/gerar_galeria.py AAAA-MM-DD` |

Status de implementação: `não iniciado` → `em especificação` → `em desenvolvimento` → `implementado` / `descartado`.

O radar não modifica o editor em produção.
