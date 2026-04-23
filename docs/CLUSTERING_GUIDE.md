# Clustering Guide

The cluster engine is designed around weighted opportunity density rather than raw population.

## Current sandbox implementation

- weighted density grouping around metro cores
- distance-based neighborhood expansion
- explainable metrics: raw count, weighted count, category mix, density, radius, travel efficiency, confidence

## Production evolution

The module boundary is intentionally ready for DBSCAN or HDBSCAN replacement without changing downstream territory generation or validation contracts.

