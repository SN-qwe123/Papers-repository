# Copyright (c) 2026 JustinN (SN-qwe123).
# Original repository: https://github.com/SN-qwe123/Papers-repository
# See NOTICE.md for provenance and third-party attribution.

from pathlib import Path
from html import escape
import yaml

def catalog(docs_dir):
    result = []
    for path in sorted((Path(docs_dir) / 'papers').glob('*.md')):
        raw = path.read_text(encoding='utf-8')
        parts = raw.split('---', 2)
        if len(parts) != 3 or parts[0].strip():
            raise ValueError(f'{path.name}: YAML front matter is required')
        data = yaml.safe_load(parts[1])
        if not isinstance(data, dict) or not isinstance(data.get('title'), str) or not data['title'].strip():
            raise ValueError(f'{path.name}: title is required')
        tags = data.get('tags', [])
        if not isinstance(tags, list) or any(not isinstance(t, str) or not t.strip() for t in tags):
            raise ValueError(f'{path.name}: tags must be a list of strings')
        data['tags'] = tags
        data['url'] = 'papers/' + path.with_suffix('.html').name
        data['source'] = 'papers/' + path.name
        result.append(data)
    return sorted(result, key=lambda p: p['title'].casefold())


def on_files(files, config):
    """Use the catalog's title order for navigation on every build."""
    papers = catalog(config['docs_dir'])
    config['nav'] = [{'Paper Library': 'index.md'}]
    if papers:
        config['nav'].append({'Papers': [{p['title']: p['source']} for p in papers]})
    included = {'index.md', *(p['source'] for p in papers)}
    # Retain any additional documentation pages added outside the paper folder.
    config['nav'].extend(
        f.src_uri for f in files.documentation_pages()
        if f.src_uri not in included and f.inclusion.is_in_nav()
    )
    return files

def on_page_markdown(markdown, page, config, files):
    if page.file.src_uri != 'index.md':
        return markdown
    papers = catalog(config['docs_dir'])
    tags = sorted({tag for p in papers for tag in p['tags']})
    controls = '<div class="filters" hidden><div class="filter-field"><label for="query">Search papers</label><input id="query" type="search" placeholder="Title, author, or tag"></div><div class="filter-field"><label for="tag">Tags</label><select id="tag"><option value="">All tags</option>'
    controls += ''.join(f'<option>{escape(t)}</option>' for t in tags)
    controls += '</select></div><button id="reset" type="button">Reset</button></div>'
    rows = []
    for number, p in enumerate(papers, start=1):
        search = ' '.join(str(p.get(k, '')) for k in ('title', 'authors', 'tags')).lower()
        labels = ''.join(f'<span class="tag">{escape(t)}</span>' for t in p['tags'])
        rows.append(f'<tr class="paper" data-search="{escape(search, quote=True)}"><td class="paper-number">{number:02d}</td><td><a href="{escape(p["url"], quote=True)}">{escape(p["title"])}</a></td><td>{labels}</td></tr>')
    html = '<section id="library" aria-label="Paper list">' + controls
    html += '<table><thead><tr><th scope="col" class="number-heading">No.</th><th scope="col">Paper title</th><th scope="col">Tags</th></tr></thead><tbody>' + ''.join(rows) + '</tbody></table>'
    html += '<p id="empty" hidden>No matching papers. Try another search or reset the filters.</p><p id="results" role="status" aria-live="polite"></p></section>'
    return markdown.replace('<!-- library -->', html)
