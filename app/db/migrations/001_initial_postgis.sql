CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE countries (
  id text PRIMARY KEY,
  name text NOT NULL,
  iso3 text NOT NULL,
  region text NOT NULL DEFAULT '',
  supported boolean NOT NULL DEFAULT true
);

CREATE TABLE country_profiles (
  country_id text PRIMARY KEY REFERENCES countries(id),
  profile_json jsonb NOT NULL
);

CREATE TABLE cities (
  id text PRIMARY KEY,
  country_id text NOT NULL REFERENCES countries(id),
  name text NOT NULL,
  region text NOT NULL DEFAULT '',
  metro_name text NOT NULL DEFAULT '',
  population_context integer NOT NULL DEFAULT 0,
  maturity_level text NOT NULL DEFAULT '',
  center geometry(Point, 4326),
  discovery_json jsonb NOT NULL DEFAULT '{}'::jsonb
);

CREATE TABLE metro_cores (
  id text PRIMARY KEY,
  city_id text NOT NULL REFERENCES cities(id),
  name text NOT NULL,
  center geometry(Point, 4326),
  notes text NOT NULL DEFAULT ''
);

CREATE TABLE source_records (
  id text PRIMARY KEY,
  city_id text NOT NULL REFERENCES cities(id),
  source_name text NOT NULL,
  source_record_id text NOT NULL,
  confidence numeric NOT NULL DEFAULT 0,
  raw_payload jsonb NOT NULL DEFAULT '{}'::jsonb
);

CREATE TABLE canonical_businesses (
  id text PRIMARY KEY,
  city_id text NOT NULL REFERENCES cities(id),
  name text NOT NULL,
  address text NOT NULL DEFAULT '',
  category text NOT NULL DEFAULT '',
  geom geometry(Point, 4326),
  confidence numeric NOT NULL DEFAULT 0,
  provenance_json jsonb NOT NULL DEFAULT '[]'::jsonb
);

CREATE TABLE territories (
  id text PRIMARY KEY,
  city_id text NOT NULL REFERENCES cities(id),
  core_id text NOT NULL REFERENCES metro_cores(id),
  name text NOT NULL,
  status text NOT NULL DEFAULT 'under_review',
  current_version_id text NOT NULL DEFAULT ''
);

CREATE TABLE territory_versions (
  id text PRIMARY KEY,
  territory_id text NOT NULL REFERENCES territories(id),
  version_number text NOT NULL,
  geom geometry(Polygon, 4326),
  coordinate_csv text NOT NULL DEFAULT '',
  boundary_description text NOT NULL DEFAULT '',
  locked boolean NOT NULL DEFAULT false
);

