(function(){
  const PAGE_SIZE = 10;
  let currentPage = 1;

  const table = document.getElementById('archiveTable');
  const tbody = table.querySelector('tbody');
  const allRows = Array.from(tbody.querySelectorAll('tr'));
  const yearFilter = document.getElementById('yearFilter');
  const searchBox = document.getElementById('searchBox');
  const pager = document.getElementById('pagination');
  const countEl = document.getElementById('archiveCount');
  const pagerWrap = document.getElementById('archivePager');

  function rowMatches(r, year, q) {
    const okYear = (year === 'all') || (r.dataset.year === year);
    if (!okYear) return false;
    if (!q) return true;
    return r.textContent.toLowerCase().includes(q.toLowerCase());
  }

  function filteredRows() {
    const year = yearFilter.value;
    const q = searchBox.value.trim();
    return allRows.filter(r => rowMatches(r, year, q));
  }

  function setVisible(rows, start, end) {
    allRows.forEach(r => r.style.display = 'none');
    rows.slice(start, end).forEach(r => r.style.display = '');
  }

  function makePageItem(label, disabled, active, onClick) {
    const li = document.createElement('li');
    li.className = 'page-item' + (disabled ? ' disabled' : '') + (active ? ' active' : '');
    const a = document.createElement('a');
    a.className = 'page-link';
    a.href = '#';
    a.textContent = label;
    if (!disabled) a.addEventListener('click', (e) => { e.preventDefault(); onClick(); });
    li.appendChild(a);
    return li;
  }

  // Build a compact list like: 1 … 4 5 6 … 20
  function pageWindow(total, current, maxLen = 7) {
    if (total <= maxLen) return Array.from({length: total}, (_, i) => i+1);
    const side = Math.floor((maxLen - 3) / 2);
    const left = Math.max(2, current - side);
    const right = Math.min(total - 1, current + side);
    const pages = [1];
    if (left > 2) pages.push('…');
    for (let i = left; i <= right; i++) pages.push(i);
    if (right < total - 1) pages.push('…');
    pages.push(total);
    return pages;
  }

  function render() {
    const rows = filteredRows();
    const total = rows.length;
    const totalPages = Math.max(1, Math.ceil(total / PAGE_SIZE));
    if (currentPage > totalPages) currentPage = totalPages;

    // Show current page rows
    const start = (currentPage - 1) * PAGE_SIZE;
    const end = Math.min(start + PAGE_SIZE, total);
    setVisible(rows, start, end);

    // Count text
    countEl.textContent = total
      ? `${start + 1}–${end} of ${total}`
      : 'No results';

    // Build pagination
    pager.innerHTML = '';
    pagerWrap.style.display = (total > PAGE_SIZE) ? '' : 'none';
    if (total <= PAGE_SIZE) return;

    pager.appendChild(
      makePageItem('«', currentPage === 1, false, () => { currentPage--; render(); })
    );

    for (const p of pageWindow(totalPages, currentPage)) {
      if (p === '…') {
        const li = document.createElement('li');
        li.className = 'page-item disabled';
        li.innerHTML = '<span class="page-link">…</span>';
        pager.appendChild(li);
      } else {
        pager.appendChild(
          makePageItem(String(p), false, p === currentPage, () => { currentPage = p; render(); })
        );
      }
    }

    pager.appendChild(
      makePageItem('»', currentPage === totalPages, false, () => { currentPage++; render(); })
    );
  }

  // Events
  yearFilter.addEventListener('change', () => { currentPage = 1; render(); });
  searchBox.addEventListener('input', () => { currentPage = 1; render(); });

  // Initial render
  render();
})();


