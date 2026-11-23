# RADAR DE CRIATIVOS — 19/11/2026

**10 referências** (2 por categoria), todas com link real retornado pela busca e **nenhuma repetida** dos radares de 07 a 18/11.
Galeria publicada: https://claude.ai/artifact/7wBySdcY6cJtJ4zuschbkf (privada). Arquivos: `referencias.json`, `galeria.html`, `catalogo/catalogo-central.csv` (catálogo consolidado, 79 referências únicas; script `scripts/consolidar_catalogo.py`).

## Limitações desta execução
- A rede da sessão bloqueia youtube.com, img.youtube.com, vimeo.com, behance.net, tiktok.com, instagram.com, facebook.com/fbcdn e videohive.net. **Nenhum vídeo foi assistido.**
- "Observado" = só o que aparece no título ou no resumo da busca. Técnica, timestamps ("momento") e criador são **não verificados**; o resto é hipótese e está marcado como tal.
- A galeria não exibe miniaturas originais: a página publicada não pode carregar imagens de outros sites. Cada card traz uma **animação esquemática do efeito** (ilustrativa, feita por nós) e o link original.
- Nenhum dado de desempenho foi encontrado nem afirmado.
- Meta Ads Library (BR, ativos, "harmonização facial") retornou anúncios de estética e odontologia, mas sem acesso ao criativo. Leads para análise manual: [Ortobrasil](https://www.facebook.com/ads/library/?id=1123375240542739), [Fernandes Martins Odontologia](https://www.facebook.com/ads/library/?id=2229361608005932), [Jaiana Maués Harmonização](https://www.facebook.com/ads/library/?id=1670104867896086), [Dra. Diully Rodrigues](https://www.facebook.com/ads/library/?id=3338682582998223), [Adriana Schnell Estética](https://www.facebook.com/ads/library/?id=1403069334942834).

## Referências

| # | Categoria | Referência | Técnica | Dificuldade | Nichos |
|---|---|---|---|---|---|
| 1 | Legendas | [Pop-up Captions: One Word at a Time (CapCut 2026)](https://www.youtube.com/watch?v=4Ldj-B5NfXc) | Pop de 1 palavra por vez | Básico | Todos |
| 2 | Legendas | [10 VIRAL Caption Styles Using CapCut](https://www.youtube.com/watch?v=Q04FF5KZyt4) | Coleção de presets | Intermediário | Todos |
| 3 | Composição | [Circle Talking Head Overlay (CapCut PC)](https://www.youtube.com/watch?v=fmieZvYtXS8) | PiP circular com borda | Básico | Arquitetura, serviços, marketing |
| 4 | Composição | [Text Behind Moving Objects – 4 Rotoscoping Techniques](https://www.youtube.com/watch?v=Iyuftoajtg0) | Texto atrás da pessoa | Avançado | Alto padrão, estética |
| 5 | Animações | [Mask Transitions for Real Estate Videos](https://www.youtube.com/watch?v=Qi1IIyCX8sY) | Wipe por objeto (walk-by) | Intermediário | Arquitetura, reformas |
| 6 | Animações | [2.5D Parallax Tutorial](https://www.youtube.com/watch?v=aQWnmF6UG5s) | Parallax de foto | Avançado | Arquitetura, interiores |
| 7 | B-roll | [From Simple Floor Plan to 3D Perspective](https://www.youtube.com/watch?v=ils3LgT6zbU) | Planta → 3D → render | Intermediário | Arquitetura |
| 8 | B-roll | [Before and After Renovation (Time-lapse)](https://www.youtube.com/shorts/N82kr2SxS5I) | Time-lapse antes/depois vertical | Básico | Reformas |
| 9 | Edição completa | [Talking Head Reels That Keep People Watching](https://www.youtube.com/watch?v=HSqc7RdLW90) | Ritmo de talking head | Intermediário | Todos |
| 10 | Edição completa | [Edit Ali Abdaal Shorts (Premiere/AE)](https://www.youtube.com/watch?v=5bFGfjDxHFg) | Estilo educacional limpo | Intermediário | Saúde, serviços |

Análise individual (observado / hipótese / como reproduzir / uso no Graviton): ver `referencias.json` ou a galeria.

## Top 3 do dia — especificações

Os radares anteriores já especificaram legenda karaokê, punch-in automático e split antes/depois. Hoje o Top 3 cobre recursos **novos**, voltados aos nichos de arquitetura e reforma.

### 1. Wipe por objeto (transição de passagem)
- **Resultado:** um elemento em primeiro plano (parede, batente, coluna) cruza o quadro e revela o ambiente seguinte.
- **Elementos:** clipe A, clipe B, máscara (linear inclinada no modo simples; contorno rastreado no modo avançado).
- **Parâmetros:** direção (E→D, D→E), ângulo da borda (0–30°), duração (8–20 frames), suavização da borda (0–40px), curva de velocidade (linear, ease-in-out, acompanhar movimento do clipe A), sombra na borda opcional.
- **Comportamento:** a borda da máscara se move junto com o movimento lateral da câmera no clipe A; o clipe B aparece atrás da borda, sem dissolve.
- **Aplicações:** tours de apartamentos, reformas cômodo a cômodo, alto padrão.
- **Tecnologia:** máscara animada por keyframes (Canvas/WebGL ou ffmpeg `overlay` + `geq`/alphamerge); modo avançado com estimativa de movimento (optical flow) para sincronizar a velocidade.

### 2. Foto viva (parallax 2.5D)
- **Resultado:** render ou foto estática ganha profundidade com câmera em movimento lento.
- **Elementos:** imagem, mapa de profundidade, preenchimento das áreas reveladas.
- **Parâmetros:** movimento (dolly-in, pan, órbita curta), amplitude (1–6%), duração (2–6s), intensidade da profundidade, foco/blur de fundo opcional.
- **Comportamento:** planos próximos se deslocam mais que o fundo; ease-in-out suave; sem cortes durante o movimento.
- **Aplicações:** renders de arquitetura, fotos de ambientes prontos, portfólio de interiores; também fotos de clínica.
- **Tecnologia:** estimativa de profundidade monocular (modelo tipo Depth Anything/MiDaS), inpainting das bordas, render por malha deslocada em WebGL ou por camadas.

### 3. Bolha do apresentador (PiP circular)
- **Resultado:** a pessoa fica num círculo sobre o projeto, a obra ou uma tela, sem sair de cena.
- **Elementos:** camada da pessoa, camada de fundo (B-roll, render, foto), máscara circular, borda.
- **Parâmetros:** posição (cantos ou livre, respeitando a zona segura do Reels), diâmetro (20–45% da largura), borda (cor, 0–10px), sombra, animação de entrada/saída (pop, slide), troca automática entre tela cheia e bolha.
- **Comportamento:** quando entra um B-roll, a pessoa encolhe para a bolha em 8–12 frames com ease-out; quando o B-roll termina, volta para tela cheia.
- **Aplicações:** arquiteto comentando o projeto, dentista explicando um caso, especialista comentando resultados.
- **Tecnologia:** compositor de camadas com máscara e keyframes de transformação; detecção de rosto para centralizar o recorte.

## Novas ideias de componentes
- **Bloco "Da planta ao render":** recebe 2–4 imagens alinhadas e gera a sequência com wipe ou dissolve (ref. 7).
- **Template "Obra em time-lapse":** speed ramp, freeze de 0,5s no antes e no depois, rótulos (ref. 8).
- **Título atrás do apresentador:** precisa de matte de pessoa; reaproveita a mesma segmentação da bolha (ref. 4).
- **Preset "Educacional limpo":** menos elementos gráficos, legenda discreta; alternativa ao estilo saturado para saúde (ref. 10).
- **Biblioteca de presets de legenda:** registrar os 10 estilos da ref. 2 depois de assistir.

## O QUE VALE IMPLEMENTAR NO EDITOR

| Prioridade | Proposta | Motivo |
|---|---|---|
| **Alta** | Bolha do apresentador (PiP circular com troca automática) | Simples de fazer e resolve a alternância pessoa ↔ projeto em todos os nichos |
| **Alta** | Wipe por objeto, modo simples (máscara linear inclinada) | Transição própria de arquitetura e imóveis, sem precisar de IA |
| **Média** | Foto viva (parallax 2.5D) | Grande ganho para renders, mas exige profundidade + inpainting |
| **Média** | Bloco "Da planta ao render" e template de time-lapse de obra | Reaproveitam transições já existentes |
| **Média** | Legenda pop de 1 palavra (preset) | Variação barata do motor de legendas |
| **Baixa** | Texto atrás do apresentador | Depende de segmentação de pessoa por quadro |
| **Baixa** | Preset "Educacional limpo" | Assistir à ref. 10 antes de especificar |

## Próximo passo sugerido
1. Liberar youtube.com, img.youtube.com, vimeo.com e behance.net na rede do ambiente agendado, para permitir miniaturas e verificação de canal/título.
2. Assistir às refs. 5, 6 e 3 para confirmar a técnica e registrar os timestamps.
3. Juntar os branches dos radares no `main` (hoje cada execução fica num branch separado); o catálogo central deste branch já consolida todos.

Fontes: links da tabela acima, obtidos por busca web em 19/11/2026.
