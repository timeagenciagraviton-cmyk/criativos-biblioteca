# RADAR DE CRIATIVOS — 20/11/2026

**10 referências** (2 por categoria), todas com link real retornado pela busca e **nenhuma repetida** das 79 já catalogadas (07 a 19/11).
Arquivos: `referencias.json` (fichas completas), `galeria.html` (galeria visual), `catalogo/catalogo-central.csv` (agora 89 referências únicas).

## Limitações desta execução
- A rede da sessão continua bloqueando youtube.com, i.ytimg.com, vimeo.com, behance.net, tiktok.com e pexels.com (testado hoje). **Nenhum vídeo foi assistido.**
- "Observado" = só o que aparece no título ou no resumo da busca. Técnica, momento e criador são **não verificados**; o resto é hipótese e está marcado como tal.
- A galeria não mostra miniaturas originais: cada card tem uma **animação esquemática do efeito** (feita por nós) e o link original.
- Nenhum dado de desempenho foi encontrado nem afirmado.
- Meta Ads Library (BR, ativos, "reforma apartamento antes e depois", 246 resultados estimados): a ferramenta devolve só página, título do link e link do anúncio, sem o vídeo. Leads de arquitetura/reforma para olhar manualmente: [Cavalcanti Cronemberger Arquitetura](https://www.facebook.com/ads/library/?id=2056211841668051), [Efatahinteriores](https://www.facebook.com/ads/library/?id=1972476830789781), [Be Vitta Engenharia](https://www.facebook.com/ads/library/?id=1125776066935728), [les.lui.engenharia](https://www.facebook.com/ads/library/?id=1529865908971516), [MBrossi Engenharia](https://www.facebook.com/ads/library/?id=1834409714269862).

## Referências

| # | Categoria | Referência | Técnica | Dificuldade | Nichos |
|---|---|---|---|---|---|
| 1 | Legendas | [Premiere Pro Captions That Make Edits Look Expensive](https://www.youtube.com/watch?v=IITI8wU5HmA) | Legenda "premium" sem plugins | Básico | Alto padrão, estética |
| 2 | Legendas | [Viral Realtor Caption Reels in After Effects](https://www.youtube.com/watch?v=KtvnhD9OQ0M) | Legenda de tour imobiliário | Intermediário | Arquitetura, reformas |
| 3 | Composição | [Combine 9 videos with 3 by 3 Grid (Premiere)](https://www.youtube.com/watch?v=XBIKcMbFzJY) | Mosaico 3×3 | Básico | Arquitetura, estética, odonto |
| 4 | Composição | [Split Screen or Video Collage in DaVinci Resolve](https://www.youtube.com/watch?v=N9OHvsnSa-Q) | Painéis / colagem de vídeos | Intermediário | Serviços, arquitetura |
| 5 | Animações | [3 Viral Real Estate Transitions in After Effects](https://www.youtube.com/watch?v=et1g5t3jHxM) | Zoom na TV, match cut no armário, porta | Avançado | Arquitetura, reformas |
| 6 | Animações | [Smooth Speed Ramp TRANSITION Effects](https://www.youtube.com/watch?v=E9rpqk9tJ48) | Rampa de velocidade | Intermediário | Alto padrão, reformas |
| 7 | B-roll | [Documentary Collage Animation in After Effects](https://www.youtube.com/watch?v=7QkZGSo4_SE) | Colagem de fotos animada | Intermediário | Reformas, estética, odonto |
| 8 | B-roll | [6 Editing Interviews with B Roll in Premiere Pro](https://www.youtube.com/watch?v=sJ3qXY_of14) | B-roll cobrindo jump cuts | Básico | Odonto, estética, serviços |
| 9 | Edição completa | [Complete Viral Realtor Video Masterclass](https://www.youtube.com/watch?v=Xdq22d85fPY) | Head tracking + legendas + ramps + SFX | Avançado | Arquitetura |
| 10 | Edição completa | [How I Edit Trending Real Estate Reels](https://www.youtube.com/watch?v=gXt43lmwlyY) | Fluxo Premiere + AE | Intermediário | Arquitetura |

Variações de técnicas já catalogadas: ref. 4 amplia o split vertical (XuI8ar0FiQg) para painéis assimétricos; ref. 8 é variação de "B-roll sobre talking head" focada em esconder cortes; ref. 5 (porta) é parente do wipe por objeto de 19/11.

Análise individual (observado / hipótese / como reproduzir / uso no Graviton): ver `referencias.json` ou a galeria.

## Top 3 do dia — especificações

Os radares anteriores já especificaram karaokê, punch-in, split/antes-depois, PiP, wipe por objeto e parallax. O Top 3 de hoje traz recursos **novos**.

### 1. Rampa de velocidade (ref. 6)
- **Resultado:** o clipe desacelera, dispara no corte e chega ao próximo plano em velocidade normal.
- **Elementos:** dois clipes adjacentes, curva de velocidade, SFX opcional (whoosh).
- **Parâmetros:** preset de curva (suave, agressiva, só entrada, só saída), velocidade mínima 25–80%, pico 200–1000%, duração do pico 4–15 frames, motion blur 0–100%, alinhar o pico ao beat.
- **Comportamento:** curva bezier contínua; o corte cai no pico; áudio do clipe silenciado durante a rampa.
- **Aplicações:** tours de imóveis, obra pronta, revelação de ambientes, produtos.
- **Tecnologia:** remapeamento de tempo com interpolação (optical flow ou frame blending), motion blur por acúmulo de quadros, detecção de beat (ex.: onset detection).

### 2. Mosaico de portfólio (refs. 3–4)
- **Resultado:** vários projetos/casos no mesmo quadro, montados célula a célula.
- **Elementos:** 3–9 clipes ou fotos, fundo, opcional pessoa numa célula grande.
- **Parâmetros:** grade (2×2, 2×3, 3×3, assimétrica 1+2), gap 0–12px, raio dos cantos 0–16px, ordem de entrada (sequência, aleatória, diagonal), intervalo 2–8 frames, célula de saída que expande.
- **Comportamento:** células entram com escala 60%→100% + fade; no fim, uma célula cresce até tela cheia e vira o próximo plano.
- **Aplicações:** "5 projetos que entregamos", casos clínicos, depoimentos múltiplos.
- **Tecnologia:** compositor de camadas com crop "cover" por célula, keyframes de transformação, guia de zona segura 9:16.

### 3. Mural de resultados (ref. 7)
- **Resultado:** fotos de obras, sorrisos ou casos caem como fotos impressas sobre uma superfície enquanto a pessoa fala.
- **Elementos:** 2–8 fotos, textura de fundo, sombra, legenda manuscrita opcional.
- **Parâmetros:** borda 0–6% (cor), rotação aleatória ±0–10°, sombra, intervalo 3–10 frames, drift de câmera 0–4%, semente aleatória.
- **Comportamento:** cada foto entra com escala 115%→100% e pequena queda; conjunto deriva lentamente; saída com zoom numa foto.
- **Aplicações:** antes/depois de odontologia e estética, fotos de obra, prints de resultado.
- **Tecnologia:** camadas 2D com transformação e sombra; semente fixa para resultados repetíveis; reaproveita o motor do mosaico.

## Novas ideias de componentes
- **Esconder jump cuts:** ao remover silêncios, sugerir B-roll da biblioteca do cliente sobre cada corte (ref. 8).
- **Preset de legenda "Editorial premium":** serifa + sans, entrada com blur e subida, destaque em itálico (ref. 1).
- **Preset de legenda "Tour imobiliário":** posição central-alta, contorno sutil para fundos claros (ref. 2).
- **Transição "Entrar na tela":** clipe B mapeado em 4 pontos (TV, monitor, quadro) e expandido até tela cheia (ref. 5).
- **Template "Tour com apresentador":** reenquadramento por rosto + rampas + SFX automáticos (refs. 9–10).

## O QUE VALE IMPLEMENTAR NO EDITOR

| Prioridade | Proposta | Motivo |
|---|---|---|
| **Alta** | Esconder jump cuts com B-roll | Encaixa na remoção de silêncio e serve a todo depoimento de clínica e serviço |
| **Alta** | Rampa de velocidade com presets | Usada em tours de imóvel; só precisa de remapeamento de tempo |
| **Média** | Mosaico de portfólio | Vários projetos/casos num quadro; base para o mural |
| **Média** | Mural de resultados | Dá movimento a fotos estáticas de antes/depois e de obras |
| **Média** | Preset "Editorial premium" | Alternativa discreta ao karaokê colorido para alto padrão e estética |
| **Baixa** | Transição "Entrar na tela" | Visual forte, mas precisa de rastreamento de cantos |
| **Baixa** | Template "Tour com apresentador" | Assistir às refs. 9–10 antes de especificar |

## Próximo passo sugerido
1. Liberar youtube.com, i.ytimg.com, vimeo.com e behance.net na rede do ambiente agendado: sem isso, nenhuma referência pode ser assistida nem ter miniatura.
2. Assistir às refs. 5, 6 e 9 para confirmar a técnica e registrar os timestamps.
3. Juntar os branches dos radares no `main` (cada execução fica num branch separado); este branch já traz o catálogo consolidado.

Fontes: links da tabela acima, obtidos por busca web em 20/11/2026.
