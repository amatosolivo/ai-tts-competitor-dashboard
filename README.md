# Competitor Dashboard

An autonomous system for discovering, scraping, and normalizing AI TTS competitor data.

## Project Structure

- `data/`: Contains `data.json` (the source of truth).
- `src/`: Core logic.
  - `discovery/`: Discovery engine to find relevant pages.
  - `scraping/`: Intelligent scraper.
  - `normalization/`: Data normalization and scoring.

## How to Run Discovery

```bash
python3 src/discovery/discovery_engine.py <homepage_url>
```

## JSON Schema

The system uses a hierarchical schema in `data/data.json` to store:

- Competitor metadata
- Positioning and market segment
- Pricing structures
- Capabilities and maturity levels
- Normalized innovation/affordability scores
