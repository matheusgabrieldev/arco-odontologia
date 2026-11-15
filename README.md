# Arco Odontologia

Landing page de uma clínica odontológica **fictícia**, feita para portfólio. Nomes, CRO e números são exemplos.

**No ar:** https://arco-odontologia-bice.vercel.app

## Estrutura

- `wireframe/lp-v1.html`: a página (HTML, CSS e JS num arquivo só)
- `design-system/`: tokens, componentes e fotos da marca
- `marca/`, `pecas/`, `brandbook.html`: identidade visual
- `build-deploy.py`: monta a pasta `deploy/` para publicar

## Publicar

```bash
python build-deploy.py
cd deploy && npx vercel deploy --prod
```

Desenvolvido por Matheus.
