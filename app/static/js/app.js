const state = {
  countries: [],
  selectedCountry: 'IN',
  selectedCity: null,
  selectedTerritory: null,
  map: null,
  mapLayers: [],
  calculatorAdjust: 1,
};

const statusColors = {
  available: '#268068',
  reserved: '#b9821f',
  sold: '#bb5d4a',
  under_review: '#5e7bc8',
};

async function fetchJSON(url, options = {}) {
  const response = await fetch(url, options);
  if (!response.ok) throw new Error(`Request failed for ${url}`);
  return response.json();
}

function money(value) {
  return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: 0 }).format(value);
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
    } catch {
      // Ignore invalid bounds for sandbox-safe rendering.
    }
  });
  if (bounds.length) {
    const combined = bounds.reduce((acc, item) => acc.extend(item), bounds[0]);
    state.map.fitBounds(combined.pad(0.2));
  }
}

function renderSummary(summary) {
  const el = document.getElementById('summary-cards');
  el.innerHTML = `
    <div class="metric"><span>Countries</span><strong>${summary.countries.length}</strong></div>
    <div class="metric"><span>Cities</span><strong>${summary.cities}</strong></div>
    <div class="metric"><span>Territories</span><strong>${summary.territories}</strong></div>
    <div class="metric"><span>Pop-only warnings</span><strong>${summary.population_logic_warning_count}</strong></div>
  `;
}

function renderCountries() {
  const el = document.getElementById('country-list');
  el.innerHTML = state.countries.map((country) => `
    <button class="${country.code === state.selectedCountry ? 'active' : ''}" data-country="${country.code}">
      <strong>${country.name}</strong>
      <div class="row"><span>${country.cities} cities</span><span>${country.contract_ready} contract-ready</span></div>
    </button>
  `).join('');
  el.querySelectorAll('button').forEach((button) => {
    button.addEventListener('click', () => loadCountry(button.dataset.country));
  });
}

function renderAnalysis(countryDetail) {
  const panel = document.getElementById('analysis-panel');
  panel.innerHTML = countryDetail.cities.map(({ city, analysis }) => `
    <div class="city-card" data-city="${city.id}">
      <div class="row"><strong>${city.name}</strong><span class="chip">${analysis.classification}</span></div>
      <div class="row"><span>City score</span><strong>${analysis.city_score}</strong></div>
      <div class="row"><span>Suggested cores</span><strong>${analysis.suggested_economic_cores}</strong></div>
      <div class="row"><span>Launch phase</span><strong>${analysis.launch_phase_recommendation}</strong></div>
      <div class="row"><span>Population-only flawed</span><strong>${analysis.population_only_is_flawed ? 'Yes' : 'No'}</strong></div>
    </div>
  `).join('');
  panel.querySelectorAll('.city-card').forEach((card) => {
    card.addEventListener('click', () => loadCity(card.dataset.city));
  });
}

function renderCity(cityDetail) {
  const panel = document.getElementById('city-panel');
  const territories = cityDetail.territories;
  panel.innerHTML = `
    <div class="kpi-grid">
      <div class="mini"><span>Detected cores</span><strong>${cityDetail.analysis.suggested_economic_cores}</strong></div>
      <div class="mini"><span>Clusters</span><strong>${cityDetail.clusters.length}</strong></div>
      <div class="mini"><span>Validated businesses</span><strong>${cityDetail.businesses.length}</strong></div>
      <div class="mini"><span>Recommended territories</span><strong>${territories.length}</strong></div>
    </div>
    ${territories.map((territory) => `
      <div class="territory-card" data-territory="${territory.territory_id}">
        <div class="row"><strong>${territory.territory_name}</strong><span class="badge ${territory.status}">${territory.status.replace('_', ' ')}</span></div>
        <div class="row"><span>Viability</span><strong>${territory.viability_score}</strong></div>
        <div class="row"><span>Weighted viable count</span><strong>${territory.opportunity_summary.weighted_viable_count}</strong></div>
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
  const boundedConsults = Math.round(expected.monthly_consults * state.calculatorAdjust);
  const panel = document.getElementById('territory-panel');
  panel.innerHTML = `
    <div class="row"><strong>${territory.territory_name}</strong><span class="badge ${territory.status}">${territory.status.replace('_', ' ')}</span></div>
    <p class="muted">${territory.written_boundary_description}</p>
    <div class="kpi-grid">
      <div class="mini"><span>Opportunity score</span><strong>${territory.viability_score}</strong></div>
      <div class="mini"><span>Contractability</span><strong>${territory.contractability_score}</strong></div>
      <div class="mini"><span>Weighted count</span><strong>${territory.opportunity_summary.weighted_viable_count}</strong></div>
      <div class="mini"><span>Raw businesses</span><strong>${territory.opportunity_summary.raw_business_count}</strong></div>
    </div>
    <div>
      <label><strong>Territory-aware calculator</strong></label>
      <p class="muted">Slider bounded to territory capacity. It scales the expected case without exceeding 120% of validated capacity.</p>
      <input id="calculator-range" type="range" min="0.8" max="1.2" step="0.05" value="${state.calculatorAdjust}">
      <div class="row"><span>Monthly consults</span><strong>${boundedConsults}</strong></div>
      <div class="row"><span>Annual net income</span><strong>${money(expected.net_franchisee_income * state.calculatorAdjust)}</strong></div>
      <div class="row"><span>Suggested franchise range</span><strong>${money(expected.recommended_franchise_price_low)} - ${money(expected.recommended_franchise_price_high)}</strong></div>
    </div>
    ${territory.scenarios.map((scenario) => `
      <div class="mini">
        <div class="row"><strong>${scenario.name.replace('_', ' ')}</strong><span>${scenario.monthly_clinic_days} clinic days/mo</span></div>
        <div class="row"><span>Consults</span><strong>${scenario.monthly_consults}</strong></div>
        <div class="row"><span>Gross profit</span><strong>${money(scenario.gross_profit)}</strong></div>
        <div class="row"><span>Net income</span><strong>${money(scenario.net_franchisee_income)}</strong></div>
      </div>
    `).join('')}
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
    <p class="muted">Tier A ingestion, Tier B reconciliation, and Tier C contract certification are all surfaced via provenance, scores, and export readiness.</p>
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
  state.currentCityDetail = await fetchJSON(`/api/cities/${cityId}`);
  document.getElementById('view-title').textContent = state.currentCityDetail.city.name;
  document.getElementById('view-subtitle').textContent = `${state.currentCityDetail.analysis.classification} market with ${state.currentCityDetail.analysis.suggested_economic_cores} suggested cores and territory generation driven by validated opportunity clusters.`;
  renderCity(state.currentCityDetail);
}

async function loadCountry(countryCode) {
  state.selectedCountry = countryCode;
  renderCountries();
  const countryDetail = await fetchJSON(`/api/countries/${countryCode}`);
  renderAnalysis(countryDetail);
  const firstCity = countryDetail.cities[0]?.city?.id;
  if (firstCity) await loadCity(firstCity);
}

async function rerunCurrentMarket() {
  if (!state.selectedCity) return;
  const result = await fetchJSON(`/api/admin/rerun/${state.selectedCity}`, { method: 'POST' });
  document.getElementById('job-status').innerHTML = `<p>${result.job_type}</p><strong>${result.status}</strong><p>${result.completed_at}</p>`;
  await loadCity(state.selectedCity);
}

async function boot() {
  initMap();
  const summary = await fetchJSON('/api/summary');
  renderSummary(summary);
  state.countries = await fetchJSON('/api/countries');
  renderCountries();
  await loadCountry(state.selectedCountry);
  document.getElementById('rerun-market').addEventListener('click', rerunCurrentMarket);
}

boot().catch((error) => {
  document.getElementById('view-subtitle').textContent = error.message;
});

