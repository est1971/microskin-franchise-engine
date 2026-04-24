const state = {
  countries: [],
  selectedCountry: 'IN',
  selectedCity: null,
  selectedTerritory: null,
  currentCountryFinancial: null,  // financial profile for the active country
  map: null,
  mapLayers: [],
  calculatorAdjust: 1.0,
};

const statusColors = {
  available: '#268068',
  reserved: '#b9821f',
  sold: '#bb5d4a',
  under_review: '#5e7bc8',
};

// Region grouping for 22-country sidebar
const REGION_ORDER = [
  'South & South East Asia',
  'APAC',
  'North America',
  'Latin America',
  'Europe',
  'Middle East',
];

async function fetchJSON(url, options = {}) {
  const response = await fetch(url, options);
  if (!response.ok) throw new Error(`Request failed for ${url}`);
  return response.json();
}

// Format money in local currency for the active country
function money(value, currencyCode, currencySymbol) {
  const code = currencyCode || (state.currentCountryFinancial && state.currentCountryFinancial.currency_code) || 'USD';
  const sym = currencySymbol || (state.currentCountryFinancial && state.currentCountryFinancial.currency_symbol) || '$';
  // Use Intl for USD/EUR/GBP/AUD etc; fall back to manual formatting for less common codes
  const commonIntlCodes = ['USD','EUR','GBP','AUD','CAD','JPY','CHF','SEK','NOK','DKK','PLN','BRL','MXN','INR','THB','MYR','SGD'];
  if (commonIntlCodes.includes(code)) {
    try {
      return new Intl.NumberFormat('en-GB', {
        style: 'currency',
        currency: code,
        maximumFractionDigits: 0,
      }).format(value);
    } catch (_) { /* fall through */ }
  }
  // Manual fallback for non-standard codes (JOD, etc.)
  return `${sym}${Math.round(value).toLocaleString()}`;
}

function initMap() {
  state.map = L.map('map').setView([20, 10], 2);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors',
  }).addTo(state.map);
}

function clearMap() {
  state.mapLayers.forEach((layer) => state.map.removeLayer(layer));
  state.mapLayers = [];
}

function addTerritoriesToMap(territories) {
  clearMap();
  const bounds = [];
  territories.forEach((territory) => {
    const layer = L.geoJSON(territory.polygon_geojson, {
      style: {
        color: statusColors[territory.status],
        fillColor: statusColors[territory.status],
        fillOpacity: 0.22,
        weight: 2,
      },
    }).addTo(state.map);
    layer.on('click', () => selectTerritory(territory.territory_id));
    state.mapLayers.push(layer);
    try {
      bounds.push(layer.getBounds());
    } catch { /* ignore invalid bounds */ }
  });
  if (bounds.length) {
    const combined = bounds.reduce((acc, item) => acc.extend(item), bounds[0]);
    state.map.fitBounds(combined.pad(0.2));
  }
}

function renderSummary(summary) {
  const el = document.getElementById('summary-cards');
  // API returns cities_total and cities_loaded — not "cities"
  el.innerHTML = `
    <div class="metric"><span>Countries</span><strong>${summary.countries.length}</strong></div>
    <div class="metric"><span>Cities</span><strong>${summary.cities_total}</strong></div>
    <div class="metric"><span>Territories</span><strong>${summary.territories}</strong></div>
    <div class="metric"><span>Contract-ready</span><strong>${summary.contract_ready}</strong></div>
  `;
}

function renderCountries() {
  const el = document.getElementById('country-list');
  // Group by region, sorted in REGION_ORDER
  const byRegion = {};
  state.countries.forEach((country) => {
    const region = country.region || 'Other';
    if (!byRegion[region]) byRegion[region] = [];
    byRegion[region].push(country);
  });

  // Sort regions by REGION_ORDER, then alphabetically for unlisted
  const regionKeys = Object.keys(byRegion).sort((a, b) => {
    const ai = REGION_ORDER.indexOf(a);
    const bi = REGION_ORDER.indexOf(b);
    if (ai !== -1 && bi !== -1) return ai - bi;
    if (ai !== -1) return -1;
    if (bi !== -1) return 1;
    return a.localeCompare(b);
  });

  el.innerHTML = regionKeys.map((region) => `
    <div class="region-group">
      <p class="region-label">${region}</p>
      ${byRegion[region].map((country) => `
        <button class="${country.code === state.selectedCountry ? 'active' : ''}" data-country="${country.code}">
          <div class="row">
            <strong>${country.name}</strong>
            <span class="country-currency">${country.currency_symbol}${country.code}</span>
          </div>
          <div class="row">
            <span>${country.cities} cities</span>
            <span>${country.contract_ready} contract-ready</span>
          </div>
        </button>
      `).join('')}
    </div>
  `).join('');

  el.querySelectorAll('button[data-country]').forEach((button) => {
    button.addEventListener('click', () => loadCountry(button.dataset.country));
  });
}

function renderAnalysis(countryDetail) {
  const panel = document.getElementById('analysis-panel');
  // Show both loaded (with analysis) and unloaded (fixture-only) cities
  panel.innerHTML = countryDetail.cities.map(({ city, analysis, loaded }) => {
    if (!loaded || !analysis) {
      return `
        <div class="city-card lazy-city" data-city="${city.id}">
          <div class="row">
            <strong>${city.name}</strong>
            <span class="chip chip-muted">click to load</span>
          </div>
          <div class="row"><span>Pop.</span><strong>${(city.population_context || 0).toLocaleString()}</strong></div>
          <div class="row"><span>Phase</span><strong>${city.launch_phase || '—'}</strong></div>
        </div>
      `;
    }
    return `
      <div class="city-card" data-city="${city.id}">
        <div class="row"><strong>${city.name}</strong><span class="chip">${analysis.classification}</span></div>
        <div class="row"><span>City score</span><strong>${analysis.city_score}</strong></div>
        <div class="row"><span>Suggested cores</span><strong>${analysis.suggested_economic_cores}</strong></div>
        <div class="row"><span>Launch phase</span><strong>${analysis.launch_phase_recommendation}</strong></div>
        <div class="row"><span>Population-only flawed</span><strong>${analysis.population_only_is_flawed ? 'Yes' : 'No'}</strong></div>
      </div>
    `;
  }).join('');
  panel.querySelectorAll('.city-card').forEach((card) => {
    card.addEventListener('click', () => loadCity(card.dataset.city));
  });
}

function renderCity(cityDetail) {
  const panel = document.getElementById('city-panel');
  const territories = cityDetail.territories;
  const fin = state.currentCountryFinancial;
  panel.innerHTML = `
    <div class="kpi-grid">
      <div class="mini"><span>Detected cores</span><strong>${cityDetail.analysis.suggested_economic_cores}</strong></div>
      <div class="mini"><span>Clusters</span><strong>${cityDetail.clusters.length}</strong></div>
      <div class="mini"><span>Validated businesses</span><strong>${cityDetail.businesses.length}</strong></div>
      <div class="mini"><span>Territories</span><strong>${territories.length}</strong></div>
    </div>
    ${fin ? `
      <div class="mini fin-header">
        <div class="row"><span>Market currency</span><strong>${fin.currency_symbol} ${fin.currency_code}</strong></div>
        <div class="row"><span>Product price from</span><strong>${money(fin.product_price_local)}</strong></div>
        <div class="row"><span>Default consult fee</span><strong>${money(fin.consultation_fee_default)}</strong></div>
      </div>` : ''}
    ${territories.map((territory) => `
      <div class="territory-card" data-territory="${territory.territory_id}">
        <div class="row">
          <strong>${territory.territory_name}</strong>
          <div style="display:flex;gap:6px;align-items:center;">
            <span class="tier-badge tier-${territory.tier || 'Standard'}">${territory.tier || 'Standard'}</span>
            <span class="badge ${territory.status}">${territory.status.replace('_', ' ')}</span>
          </div>
        </div>
        <div class="row"><span>Opportunity score</span><strong>${(territory.opportunity_score || 0).toFixed(1)}</strong></div>
        <div class="row"><span>Viable opportunities</span><strong>${territory.opportunity_summary.weighted_viable_count}</strong></div>
        <div class="row"><span>Travel efficiency</span><strong>${territory.opportunity_summary.travel_efficiency}</strong></div>
        <div class="row"><span>Validation</span><strong>${territory.validation_status}</strong></div>
      </div>
    `).join('')}
  `;
  panel.querySelectorAll('.territory-card').forEach((card) => {
    card.addEventListener('click', () => selectTerritory(card.dataset.territory));
  });
  addTerritoriesToMap(territories);
  if (!state.selectedTerritory && territories.length) {
    selectTerritory(territories[0].territory_id, false);
  }
}

function renderTerritory(territory) {
  const expected = territory.scenarios.find((item) => item.name === 'expected');
  const fin = state.currentCountryFinancial;
  const adj = state.calculatorAdjust;

  // Scale financial values with territory adjust slider
  const adjustedConsults = Math.round(expected.monthly_consults * adj);
  const adjustedNet = expected.net_franchisee_income * adj;
  const adjustedLow = expected.recommended_franchise_price_low * adj;
  const adjustedHigh = expected.recommended_franchise_price_high * adj;

  // If the backend projected in USD but we have a local rate, convert
  const rate = (fin && fin.gbp_rate) ? (fin.gbp_rate / 1.27) : 1; // approx USD→local
  const localNet = money(adjustedNet * rate);
  const localLow = money(adjustedLow * rate);
  const localHigh = money(adjustedHigh * rate);
  const localGbpNet = `(£${Math.round(adjustedNet).toLocaleString()})`;

  const panel = document.getElementById('territory-panel');
  panel.innerHTML = `
    <div class="row">
      <strong>${territory.territory_name}</strong>
      <div style="display:flex;gap:6px;align-items:center;">
        <span class="tier-badge tier-${territory.tier || 'Standard'}">${territory.tier || 'Standard'}</span>
        <span class="badge ${territory.status}">${territory.status.replace('_', ' ')}</span>
      </div>
    </div>
    <p class="muted">${territory.written_boundary_description}</p>
    <div class="kpi-grid">
      <div class="mini"><span>Opportunity score</span><strong>${(territory.opportunity_score || 0).toFixed(1)}</strong></div>
      <div class="mini"><span>Contractability</span><strong>${territory.contractability_score}</strong></div>
      <div class="mini"><span>Viable count</span><strong>${territory.opportunity_summary.weighted_viable_count}</strong></div>
      <div class="mini"><span>Raw businesses</span><strong>${territory.opportunity_summary.raw_business_count}</strong></div>
    </div>
    <div class="calc-block">
      <label><strong>Territory calculator</strong></label>
      <p class="muted">Slide to model consult volume within validated territory capacity (80%–120%).</p>
      <input id="calculator-range" type="range" min="0.8" max="1.2" step="0.05" value="${adj}">
      <div class="row"><span>Monthly consults</span><strong>${adjustedConsults}</strong></div>
      <div class="row"><span>Annual net income</span><strong>${localNet} <span class="gbp-note">${localGbpNet}</span></strong></div>
      <div class="row"><span>Suggested franchise range</span><strong>${localLow} – ${localHigh}</strong></div>
      ${fin ? `<div class="row muted-row"><span>Consult fee (editable)</span><strong>${money(fin.consultation_fee_default)}</strong></div>` : ''}
    </div>
    <div class="scenarios">
      ${territory.scenarios.map((scenario) => {
        const scenNet = money(scenario.net_franchisee_income * rate);
        const scenGross = money(scenario.gross_profit * rate);
        return `
          <div class="mini">
            <div class="row"><strong>${scenario.name.replace('_', ' ')}</strong><span>${scenario.monthly_clinic_days} days/mo</span></div>
            <div class="row"><span>Consults</span><strong>${scenario.monthly_consults}</strong></div>
            <div class="row"><span>Gross profit</span><strong>${scenGross}</strong></div>
            <div class="row"><span>Net income</span><strong>${scenNet}</strong></div>
          </div>
        `;
      }).join('')}
    </div>
  `;
  document.getElementById('calculator-range').addEventListener('input', (event) => {
    state.calculatorAdjust = Number(event.target.value);
    renderTerritory(territory);
  });
  renderAdminPanel(territory);
  renderExportPanel(territory);
}

function renderAdminPanel(territory) {
  const panel = document.getElementById('admin-panel');
  panel.innerHTML = `
    <div class="row"><span>Version</span><strong>${territory.version_id}</strong></div>
    <div class="row"><span>Postal units</span><strong>${territory.postal_units.join(', ')}</strong></div>
    <div class="row"><span>Corridors</span><strong>${territory.corridor_streets.join(', ')}</strong></div>
    <div class="row"><span>Validation</span><strong>${territory.validation_status}</strong></div>
    <div class="row"><span>Status</span><strong>${territory.status}</strong></div>
    <p class="muted">Contract certification is driven by validation_status, viability score, and contractability score. Territories with status "valid" are export-ready.</p>
  `;
}

function renderExportPanel(territory) {
  const panel = document.getElementById('export-panel');
  panel.innerHTML = ['json', 'geojson', 'csv', 'pdf'].map((fmt) => `
    <div class="export-card">
      <div class="row"><strong>${fmt.toUpperCase()}</strong><a class="export-link" href="/api/territories/${territory.territory_id}/export/${fmt}" target="_blank">Download</a></div>
      <p class="muted">Contract-ready export for ${territory.territory_name}.</p>
    </div>
  `).join('');
}

async function selectTerritory(territoryId, fetchFresh = true) {
  state.selectedTerritory = territoryId;
  const territory = fetchFresh
    ? await fetchJSON(`/api/territories/${territoryId}`)
    : state.currentCityDetail.territories.find((item) => item.territory_id === territoryId);
  renderTerritory(territory);
}

async function loadCity(cityId) {
  state.selectedCity = cityId;

  // Show loading state immediately so the user knows something is happening
  document.getElementById('view-title').textContent = 'Loading…';
  document.getElementById('view-subtitle').textContent = 'Running territory discovery — first load may take 30–60 seconds while Google Places is queried across the full metro. Subsequent loads are instant.';
  document.getElementById('city-panel').innerHTML = '<p class="muted" style="padding:16px">Discovering businesses across the metro grid…</p>';
  document.getElementById('territory-panel').innerHTML = '<p class="muted" style="padding:16px">Territories will appear once discovery is complete.</p>';

  try {
    state.currentCityDetail = await fetchJSON(`/api/cities/${cityId}`);
    document.getElementById('view-title').textContent = state.currentCityDetail.city.name;
    document.getElementById('view-subtitle').textContent = `${state.currentCityDetail.analysis.classification} market · ${state.currentCityDetail.analysis.suggested_economic_cores} estimated cores · territory generation driven by validated opportunity clusters.`;
    renderCity(state.currentCityDetail);
  } catch (err) {
    document.getElementById('view-title').textContent = 'Discovery error';
    document.getElementById('view-subtitle').textContent = `Failed to load ${cityId}: ${err.message}`;
    document.getElementById('city-panel').innerHTML = `<p class="muted" style="padding:16px;color:var(--danger)">Error: ${err.message}</p>`;
  }
}

async function loadCountry(countryCode) {
  state.selectedCountry = countryCode;
  state.calculatorAdjust = 1.0;
  const countryRecord = state.countries.find((c) => c.code === countryCode);
  if (countryRecord) {
    state.currentCountryFinancial = countryRecord;
  }
  renderCountries();
  document.getElementById('analysis-panel').innerHTML = '<p class="muted" style="padding:16px">Loading cities…</p>';
  const countryDetail = await fetchJSON(`/api/countries/${countryCode}`);
  renderAnalysis(countryDetail);
  // Auto-load first already-discovered city; otherwise load first city in list
  const firstLoaded = countryDetail.cities.find((c) => c.loaded);
  const firstAny = countryDetail.cities[0];
  const target = firstLoaded || firstAny;
  if (target) await loadCity(target.city.id);
}

async function rerunCurrentMarket() {
  if (!state.selectedCity) return;
  const result = await fetchJSON(`/api/admin/rerun/${state.selectedCity}`, { method: 'POST' });
  document.getElementById('job-status').innerHTML = `<p>${result.job_type}</p><strong>${result.status}</strong><p>${result.completed_at}</p>`;
  await loadCity(state.selectedCity);
}

async function boot() {
  initMap();
  const [summary, countries] = await Promise.all([
    fetchJSON('/api/summary'),
    fetchJSON('/api/countries'),
  ]);
  renderSummary(summary);
  state.countries = countries;
  // Default to India on startup; fall back to first available country
  const defaultCode = countries.some((c) => c.code === 'IN') ? 'IN' : countries[0]?.code;
  if (defaultCode) {
    await loadCountry(defaultCode);
  }
  document.getElementById('rerun-market').addEventListener('click', rerunCurrentMarket);
}

boot().catch((error) => {
  document.getElementById('view-subtitle').textContent = `Boot error: ${error.message}`;
});
