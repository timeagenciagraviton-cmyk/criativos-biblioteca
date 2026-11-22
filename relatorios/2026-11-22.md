# RADAR DE CRIATIVOS — 22/11/2026

**Referências catalogadas:** 10 (REF-0001 a REF-0010). Galeria visual: https://claude.ai/artifact/DDXvwffvbisKt6bqTr9S3W (fonte: `relatorios/2026-11-22.html`).

## Limitação desta execução (importante)

A rede desta sessão bloqueia youtube.com, vimeo.com, behance.net e tiktok.com. Só o índice de busca e a Meta Ads Library (via API) responderam. Consequências:

- Nenhum vídeo foi assistido. A coluna **Observado** reflete apenas o título e a descrição indexados de cada link. Tudo o que diz respeito à execução visual está marcado como **Hipótese**.
- **Momento no vídeo**: não verificado em nenhuma das 10.
- **Criador**: não confirmado (a página do vídeo não abriu).
- **Prévias**: miniaturas não puderam ser baixadas. A galeria usa simulações esquemáticas de cada técnica, identificadas como tal.
- Meta Ads Library: 6 anúncios ativos de arquitetura no Brasil foram listados em `catalogo/fila-meta-ads-library.json` para revisão visual manual. A API não devolve o vídeo do anúncio, então eles **não** entram como referências analisadas.
- Nenhum dado de desempenho foi verificado. Nada aqui afirma que um anúncio teve bom resultado.

**Para a próxima execução:** liberar `youtube.com`, `i.ytimg.com`, `vimeo.com` e `behance.net` nas configurações de rede do ambiente.

## Referências

| ID | Categoria | Técnica | Dificuldade | Link |
|---|---|---|---|---|
| REF-0001 | Legendas | Destaque automático da palavra falada + emojis animados | intermediário | [YouTube](https://www.youtube.com/watch?v=94gztkz9k_c) |
| REF-0002 | Legendas | Ênfase seletiva de palavras-chave | básico | [YouTube](https://www.youtube.com/watch?v=U3fbSFhQDRY) |
| REF-0003 | Composição | Tela dividida vertical (2 a 5 painéis) | básico | [YouTube](https://www.youtube.com/watch?v=XuI8ar0FiQg) |
| REF-0004 | Composição | Picture-in-picture do falante sobre o B-roll | básico | [YouTube](https://www.youtube.com/watch?v=DPGe5ziNrSo) |
| REF-0005 | Animações | Zoom lento contínuo (dynamic zoom) | básico | [YouTube](https://www.youtube.com/watch?v=SeMOS1akDAs) |
| REF-0006 | Animações | Toggle animado antes/depois | intermediário | [YouTube](https://www.youtube.com/watch?v=NDF3LmYo0YQ) |
| REF-0007 | B-roll | Slider/wipe antes e depois | básico | [YouTube](https://www.youtube.com/watch?v=_nIXhlMM9EY) |
| REF-0008 | B-roll | Moodboard de materiais → ambiente pronto | intermediário | [YouTube](https://www.youtube.com/watch?v=B6XuxGdsI9k) |
| REF-0009 | Edição completa | Estilo talking head de alta densidade (Hormozi) | intermediário | [YouTube](https://www.youtube.com/watch?v=y60ohM4nr4Y) |
| REF-0010 | Edição completa | 3 técnicas de retenção além do corte rápido | intermediário | [YouTube](https://www.youtube.com/watch?v=5ds2J1THdbY) |

A análise completa de cada uma (observado, hipótese, reprodução, nichos, uso no editor) está em `catalogo/referencias.json`.

## Top 3 técnicas do dia: especificações de implementação

### 1. Antes/Depois Slider (REF-0007, variante REF-0006)
- **Resultado visual:** duas mídias alinhadas; uma linha divisória com alça percorre o quadro e revela o "depois" sobre o "antes".
- **Elementos:** mídia A (antes), mídia B (depois), linha divisória, alça circular, rótulos ANTES/DEPOIS.
- **Parâmetros:** direção (horizontal, vertical, diagonal), duração (0,8–3 s), easing, pausa no meio (0–1 s em 50%), cor/espessura da linha, posição e estilo dos rótulos, variante "toggle" (REF-0006), SFX de clique.
- **Animação:** máscara de recorte `clip-path: inset()` animada de 0→50% (ease-out), pausa e 50→100% (ease-in-out). Os rótulos mudam de opacidade conforme o lado dominante.
- **Aplicações:** reforma, interiores (render × obra pronta), estética, odontologia (sorriso).
- **Tecnologia:** compositor com máscara por camada (FFmpeg `overlay` + `crop` animado por expressão, ou WebGL/Canvas em preview + render via FFmpeg); alinhamento opcional por homografia (OpenCV) quando as fotos têm ângulos levemente diferentes.

### 2. Legenda Karaokê com Ênfase (REF-0001 + REF-0002)
- **Resultado visual:** blocos de 2 a 4 palavras; a palavra falada muda de cor/fundo; palavras-chave recebem um estilo extra (cor da marca, scale maior, emoji opcional).
- **Elementos:** transcrição com timestamp por palavra, bloco de texto, estilo ativo, estilo ênfase, trilha de emojis.
- **Parâmetros:** palavras por bloco, fonte/peso, posição (terço inferior, centro), cor base, cor ativa, fundo da palavra ativa (nenhum, pill, caixa), scale ativo (1.00–1.15), estilo de entrada (pop, slide, fade), limite de ênfases por bloco, emojis on/off.
- **Animação:** troca de estado da palavra ativa em ≤ 80 ms; pop de entrada do bloco (scale 0.9→1.0, 120 ms); ênfase com overshoot leve (1.0→1.18→1.12).
- **Aplicações:** todos os nichos com falante; ênfase para números, preços, nomes de procedimento.
- **Tecnologia:** ASR com timestamps por palavra (WhisperX ou similar), detecção de palavra-chave por LLM ou lista, render ASS/libass com tags `\k`/`\t` ou camada Canvas/Remotion.

### 3. Câmera Viva: zoom dinâmico automático (REF-0005)
- **Resultado visual:** cada segmento entre cortes tem um zoom lento e suave, como se a câmera se movesse; em cortes, o enquadramento alterna (100% ↔ 115%).
- **Elementos:** detecção de rosto, lista de cortes, curva de escala por segmento.
- **Parâmetros:** intensidade (2–12%), direção (in, out, alternado), easing, âncora (rosto, centro, ponto manual), punch-in em ênfase (on/off, % e duração).
- **Animação:** scale linear ou ease-in-out ao longo do segmento; punch-in de 120–200 ms nas palavras de ênfase vindas da legenda.
- **Aplicações:** qualquer vídeo de pessoa falando; especialmente gravações estáticas de celular.
- **Tecnologia:** detecção facial (MediaPipe), FFmpeg `zoompan` ou `scale+crop` com expressão por tempo, sincronização com a trilha de legenda.

## Novas ideias de componentes
- **Template Moodboard → Ambiente** (REF-0008): grade de materiais com entrada escalonada, seguida de revelação do ambiente.
- **Layouts de composição** (REF-0003/0004): Split 50/50, Split 40/60, Mosaico 4, PiP com recorte de fundo.
- **Analisador de ritmo** (REF-0010): aponta trechos com mais de X segundos sem mudança visual.
- **Preset "Alta densidade"** (REF-0009): corte de silêncio + alternância de enquadramento + karaokê + SFX.

## O QUE VALE IMPLEMENTAR NO EDITOR

| Prioridade | Proposta | Motivo |
|---|---|---|
| **Alta** | Antes/Depois Slider + variante Toggle | Serve diretamente a reforma, interiores, estética e odontologia; baixa complexidade |
| **Alta** | Legenda Karaokê com Ênfase | Base de quase todo criativo com falante |
| **Alta** | Câmera Viva (zoom dinâmico) | Melhora qualquer gravação estática; básico de implementar |
| **Média** | Layouts Split e PiP com recorte | Abre espaço para B-roll de projeto sem perder o falante |
| **Média** | Template Moodboard → Ambiente | Específico de arquitetura e interiores |
| **Baixa** | Analisador de ritmo | Útil, mas depende das outras peças e de calibração |
| **Baixa** | Preset "Alta densidade" | Composição dos itens acima; o estilo pode não combinar com alto padrão |

Nenhuma alteração foi feita no editor em produção.
