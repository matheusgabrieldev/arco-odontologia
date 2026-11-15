A Arco Odontologia é uma clínica de implantes e lentes de contato dental em Ribeirão Preto (projeto fictício de portfólio). O posicionamento é premium acessível: técnica de ponta com conversa de gente. A interface precisa parecer precisa sem ser fria, e acolhedora sem ser popular. A landing page tem uma só ação, agendar a avaliação pelo WhatsApp, e 85% das visitas vêm do Instagram, no celular.

## Conteúdo e voz

Escreva como a doutora fala na cadeira: com calma, tratando por "você", trocando termo técnico por palavra comum e sem prometer o que não dá para garantir.

- Escreva assim: "Antes de começar, você vê na tela como o seu sorriso vai ficar." · "Tem medo de dentista? A gente trabalha com sedação consciente." · "Na avaliação você sai com o plano, o prazo e o valor por escrito."
- Não escreva assim: "O melhor implante de Ribeirão com resultado garantido!" · "Reabilitação oral com carga imediata sobre implantes osseointegráveis." · "PROMOÇÃO! Lentes a partir de R$ 499!!!"
- Use frase comum (só a primeira letra maiúscula) em títulos, rótulos e botões. Caixa alta só na linha legal.
- Não use emoji, exclamação nem urgência ("só hoje", "últimas vagas").
- **Regras do CFO (Código de Ética Odontológica, art. 44), valem para toda tela:** não mostrar preço, serviço gratuito ou forma de pagamento ("sem custo", "24x"); não usar "o melhor"; antes e depois só com autorização escrita (TCLE) e legenda do caso; nome e CRO da responsável técnica visíveis, no estilo `rotulo-legal`.

## Cor

A paleta é Porcelana e Sálvia; o azul hospitalar fica de fora. Use as cores na proporção do brandbook: muito `fundo`, texto em `texto`, `marca` nas áreas de marca, `marca-suave` em destaques e `destaque` só no que se clica.

- `fundo-pagina` é a mesa; `fundo` e `fundo-elevado` são as placas e os cartões. `fundo-suave` fica para chips e áreas de imagem sem foto.
- Texto corrido em `texto`; subtítulos e legendas em `texto-suave`. Os dois passam de 4,5:1 sobre `fundo`, `fundo-elevado` e `fundo-suave` nos dois temas.
- `marca` (sálvia) serve para o botão primário, links, ícones e o `rotulo` de seção. Sobre ela, use `sobre-marca`.
- `marca-suave` (menta) é fundo de destaque: faixa de prova, círculo de ícone, fundo de post. Texto sobre ela: `texto` ou `marca`.
- `destaque` (âmbar) aparece só no botão de WhatsApp e no arco interno do símbolo, nunca como cor de texto sobre fundo claro (2,1:1). O texto sobre ele é `sobre-destaque`.
- Faixas escuras de largura total (CTA final e rodapé) usam `grafite` com texto `sobre-grafite`.
- O tema **Escuro** é o das seções em grafite e do modo escuro do aparelho: `marca` clareia para menta-acinzentado e o texto sobre ela fica grafite (`sobre-marca`).
- Bordas de campo e controle usam `linha-forte` (3:1). `linha` é só decorativa.

## Tipografia

Títulos grandes e leves fazem a página parecer de clínica séria, não de promoção. Três famílias do Google Fonts:

- **Bricolage Grotesque** (`display`) em peso **Regular 400**: `titulo-hero` (72px; 44px no celular), `titulo-secao` (48px; 34px no celular), `numero` (56px) e `citacao`. Peso 500 só em `titulo-cartao`. O ExtraBold 800 fica para o logotipo e para as peças de redes sociais; na LP, nunca.
- Títulos em duas frases e dois tons: a primeira afirma, em `texto`; a segunda explica ou acalma, em `texto-suave`, dentro de um `<span>`. Não destaque uma palavra solta.
- **Figtree** (`texto`): `texto-destaque`, `texto-corpo`, `texto-botao` (500), `rotulo` e `texto-pequeno`. Nunca menos de 16px em texto corrido no celular.
- Rótulo de seção (`rotulo`) em frase comum, 14px, com um ponto quadrado em `marca` antes. Nada de caixa alta.
- **IBM Plex Mono** (`mono`) só em `rotulo-legal`: a linha de CRO e o aviso de imagem ilustrativa.

## Layout, forma e camadas

- **Placas sobre a mesa.** A página tem fundo `fundo-pagina` e cada seção é uma placa com cantos `raio-lg`, afastada `margem-placa` (12px) da borda da tela e da placa vizinha. Placas alternam `fundo` e `fundo-elevado`; o CTA final e o rodapé são a placa `grafite`.
- **Hero claro com as pessoas grandes.** Texto à esquerda; à direita, o casal ocupa 60% da largura, do topo à base, dissolvido no `fundo` por um degradê. Embaixo do texto, os números da clínica separados por um fio; na base, uma faixa `grafite` com as garantias correndo devagar. Pessoas nunca em moldura pequena no hero.
- **Botão-pílula com ícone num círculo.** O do WhatsApp é sálvia com o círculo claro e o ícone de conversa. Nenhum botão usa âmbar. Rótulo em Figtree 600; o botão sobe 1px no hover e afunda no clique.
- **Menu em barra reta** com fio de 1px em `linha`, links no centro e botão à direita; ao rolar, prende no topo e troca o fio por `sombra-flutuante`.
- Cartões sem borda: o branco sobre a placa basta. Foto de cartão encaixada com 8px de margem interna.
- Depoimentos correm em duas fileiras em sentidos opostos, com as bordas dissolvidas; param no hover e com `prefers-reduced-motion`.
- Etapas marcadas por uma barra fina de progresso, não por numerais grandes. Perguntas em lista com fios, sem caixas.
- Espaçamento de `espaco-1` (4px) a `espaco-10` (128px). Seções com `espaco-9` de respiro vertical no desktop e `espaco-8` no celular.
- Sombra só em `sombra-flutuante` (menu fixo e WhatsApp). Área de toque mínima `altura-toque` (48px).
- Foco do teclado: anel sólido de 2px em `foco`, afastado 3px, em tudo que é clicável.

## Imagem

- Fotos de luz natural, tom levemente quente, pessoas de 35 a 65 anos, sorriso com cor de dente e bastante espaço vazio para texto. Use as de `assets/Fotos`.
- Evite dente 3D brilhante, estrelinhas, modelo de 20 anos com sorriso branco-papel, instrumentos cirúrgicos, sangue e filtro azul frio.
- O grafismo de arcos (PadraoArcos) vai em fundos `marca` ou `grafite`, nunca sobre foto.

## Logo e ícones

- Logo principal: `assets/Logos/logo-horizontal.svg` sobre fundo claro. Em fundo escuro, `logo-vertical-negativo.svg` ou `simbolo-negativo.svg`. Avatar e favicon: só o símbolo.
- Deixe em volta do logo um espaço livre igual à altura do "a". Tamanho mínimo: 110px de largura (horizontal) e 20px (símbolo).
- Não troque o âmbar do arco interno, não ponha dente ou brilho no símbolo, não escreva "ARCO" em caixa alta nem em outra fonte.
- Ícones: o conjunto de 6 em `assets/Icones`, com traço de 1,75px, cantos redondos, cor `marca` e um ponto em `destaque` quando pedem destaque. Não misture com outra biblioteca de ícones.
