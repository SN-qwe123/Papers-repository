(() => {
  const root = document.querySelector('#library');
  if (!root) return;
  const query = root.querySelector('#query');
  const tag = root.querySelector('#tag');
  const rows = [...root.querySelectorAll('.paper')];
  const update = () => {
    const terms = query.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
    let count = 0;
    rows.forEach(row => {
      const tags = [...row.querySelectorAll('.tag')].map(el => el.textContent);
      row.hidden = !(terms.every(term => row.dataset.search.includes(term)) && (!tag.value || tags.includes(tag.value)));
      if (!row.hidden) count++;
    });
    root.querySelector('#empty').hidden = count > 0;
    root.querySelector('#results').textContent = query.value || tag.value ? `找到 ${count} 篇论文` : '';
  };
  root.querySelector('.filters').hidden = false;
  query.addEventListener('input', update);
  tag.addEventListener('change', update);
  root.querySelector('#reset').addEventListener('click', () => {
    query.value = tag.value = '';
    update(); query.focus();
  });
  update();
})();
