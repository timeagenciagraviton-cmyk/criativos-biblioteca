# RADAR DE CRIATIVOS — 2026-11-08

## Limitações desta execução (leia primeiro)
- O ambiente bloqueou youtube.com (curl 403 / DNS no WebFetch). **Nenhum vídeo foi assistido nem teve metadados confirmados.** Títulos e URLs vêm de resultados de busca; criador só foi preenchido quando constava no resultado.
- Não foi possível acessar Instagram, TikTok, Meta Ads Library ou Behance com conteúdo real. Nenhum dado de desempenho foi coletado (nenhuma afirmação de performance é feita).
- Os campos "técnica" refletem apenas título/descrição do resultado de busca (**observado na descrição**), e os passos de reprodução abaixo são **hipóteses** de implementação. Os momentos (timestamps) **não puderam ser identificados** — revisar manualmente.
- Miniaturas: galeria em `galeria.html` usa o padrão `img.youtube.com/vi/<id>/hqdefault.jpg` (não testado aqui).

## Referências (10) — dados completos em `radar/catalogo.json`
| # | Categoria | Título | Link | Dif. |
|---|---|---|---|---|
| 1 | Legendas | Motion Typography Smooth Animation in CapCut | https://www.youtube.com/watch?v=CBE1PkDRONc | interm. |
| 2 | Legendas | Legenda animada/dinâmica p/ Reels (PT-BR, +3 anos) | https://www.youtube.com/watch?v=aVssfmEuS8o | básico |
| 3 | Composição | Vertical Split Screen no Premiere | https://www.youtube.com/watch?v=XuI8ar0FiQg | interm. |
| 4 | Composição | Viral Floating Head Effect | https://www.youtube.com/watch?v=nTjWYw4LcFo | interm. |
| 5 | Animações | Camera Shake Zoom-in Transition | https://www.youtube.com/watch?v=JzklfBui588 | básico |
| 6 | Animações | Whip Pan Transition | https://www.youtube.com/watch?v=7WR8t7HKO08 | interm. |
| 7 | Materiais compl. | Before & After Color Palettes Transition | https://www.youtube.com/watch?v=8SDCVSVkE5c | interm. |
| 8 | Materiais compl. | Modi's residence – Cinematic interior videography (Studio BluOra) | https://www.youtube.com/watch?v=AITwPQwJMjg | avançado |
| 9 | Edição completa | Clean Talking Head Video | https://www.youtube.com/watch?v=unFgmAsRHvs | básico |
| 10 | Edição completa | Edit Vertical Video for Reels/Shorts | https://www.youtube.com/watch?v=fuheoHYBtlM | básico |

Observação: são majoritariamente tutoriais, não anúncios reais; falta exemplos de anúncios de Meta Ads Library (bloqueado/não consultado).

## Parâmetros de referência encontrados (fontes de blog de fornecedores, não testados)
- Punch-in: salto de escala ~8–15%, ease curto, <12 frames; zoom a cada ~3–7 s (Pippit). Sem estudo que comprove ganho de retenção.
- Legenda karaoke no CapCut: sem modo nativo segundo uma fonte; usa keyframe de cor + tempo por palavra (VideoWizardTools).

## Top 3 técnicas → especificações

### 1. Legenda karaoke palavra-a-palavra (refs 1–2)
- Resultado: frase em 2–3 linhas; palavra falada destacada (cor + escala).
- Elementos: transcrição com timestamps por palavra; fonte; paleta.
- Parâmetros: fonte, tamanho, cor base/destaque, escala do destaque (ex.: 100→115%), palavras por linha, posição (safe-zone), contorno/sombra, animação de entrada (pop/fade/slide), duração do easing.
- Comportamento: ativa por palavra no timestamp; entrada ~100–150 ms; linha sai ao fim da frase.
- Aplicações: todos os nichos, especialmente odontologia/estética e marketing.
- Tecnologia: ASR com word timestamps, renderização por Canvas/WebGL ou ASS/FFmpeg, keyframes.

### 2. Layout empilhado/ "floating head" (refs 3–4)
- Resultado: pessoa falando sobre/ao lado de B-roll (projeto, antes/depois) em 9:16.
- Elementos: vídeo principal, B-roll, máscara de segmentação da pessoa (opcional), divisória.
- Parâmetros: proporção do split (50/50, 60/40), PIP (posição/tamanho/cantos), borda, transição entre layouts, recorte/zoom por painel.
- Comportamento: alterna layout por marcadores na timeline; transição de 200–300 ms.
- Aplicações: arquitetura (projeto + arquiteto), reformas (comparação), serviços.
- Tecnologia: compositor multi-camada, segmentação de pessoa (ex.: modelo de matting), máscaras.

### 3. Transição whip pan / zoom com shake (refs 5–6)
- Resultado: corte com movimento rápido e blur direcional ligando duas cenas.
- Elementos: clipe A/B, blur direcional, shake, som whoosh opcional.
- Parâmetros: direção, duração (6–12 frames), intensidade do blur, curva de easing, amplitude do shake, escala do zoom.
- Comportamento: A acelera e borra até o fim; B entra desacelerando.
- Aplicações: tour de ambientes, mudança de assunto, antes/depois.
- Tecnologia: shaders (blur direcional), keyframes com bezier, mixagem de áudio.

## O QUE VALE IMPLEMENTAR NO EDITOR
- **Alta:** legenda karaoke por palavra; layouts split/PIP com preset de proporção.
- **Média:** transições whip pan/zoom-shake; auto punch-in (escala 8–15% a cada ~3–7 s, configurável); reveal antes/depois (wipe).
- **Baixa:** floating head com segmentação; troca de paleta de cor no reveal.

## Próximo passo sugerido
Liberar youtube.com (e Meta Ads Library/Instagram/TikTok/Behance) na política de rede do ambiente para que as próximas execuções possam confirmar criador, duração e momentos das técnicas.
