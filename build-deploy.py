"""Monta a pasta deploy/ (site estático pronto para a Vercel) a partir de wireframe/lp-v1.html.
Uso: python build-deploy.py"""
import re, shutil
from pathlib import Path

raiz = Path(__file__).parent
src = raiz / 'wireframe' / 'lp-v1.html'
out = raiz / 'deploy'
ds = raiz / 'design-system' / 'project'

out.mkdir(exist_ok=True)
for item in out.iterdir():  # limpa tudo menos .vercel (vínculo com o projeto na Vercel)
    if item.name.startswith('.'):  # .vercel, .env.local, .gitignore
        continue
    shutil.rmtree(item) if item.is_dir() else item.unlink()
(out / 'assets').mkdir(parents=True)

html = src.read_text(encoding='utf-8')
usados = sorted(set(re.findall(r'\.\./design-system/project/([^"\'\s),?#]+)', html)))
for rel in usados:
    destino = out / 'assets' / rel
    destino.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ds / rel, destino)
html = html.replace('../design-system/project/', 'assets/')

# favicon com o símbolo da marca
shutil.copy2(ds / 'assets' / 'Logos' / 'simbolo.svg', out / 'favicon.svg')
html = html.replace('<title>', '<link rel="icon" href="favicon.svg" type="image/svg+xml">\n<title>', 1)

# imagem de compartilhamento precisa do endereço completo
SITE = 'https://arco-odontologia-bice.vercel.app'
html = html.replace('<meta property="og:image" content="assets/', f'<meta property="og:image" content="{SITE}/assets/')
html = html.replace('<title>', f'<link rel="canonical" href="{SITE}/">\n<title>', 1)

(out / 'index.html').write_text(html, encoding='utf-8')
(out / 'robots.txt').write_text('User-agent: *\nDisallow: /\n', encoding='utf-8')
print(f'ok: {len(usados)} arquivos copiados para {out}')
