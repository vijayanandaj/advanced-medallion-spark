# Advanced Medallion + Spark Program — Template-ready

> Session 2 (Advanced): production-grade Medallion with Spark — incremental, streaming, CDC, replay/late data, performance tuning, and ops.

## Executive Overview

> See **[Program Overview](docs/overview.md)** and the **[Four-Day Agenda (8 Half-Days)](docs/agenda.md)**.

This is a **code-backed advanced training portfolio**. Each topic has runnable notebook-style scripts and synthetic datasets.

- **Focus**: real-time ingestion, incremental & idempotent pipelines, CDC, late data, Spark performance, Delta optimization, ops.
- **Audience**: Data/Analytics Engineers, Platform teams
- **Format**: 4 days (8 half-days)
- **Prereqs**: Session 1 foundations (Delta, Medallion) or equivalent

> Full plan: **[Program Overview](docs/overview.md)** • **[Four-Day Agenda (8 Half-Days)](docs/agenda.md)**

## Quick Start
**Databricks**
1) Repos → Add (URL) → attach cluster (DBR 15.x LTS + Photon).  
2) Open a folder under `labs-advanced/*`, set widgets (catalog/schema/paths), and run.

**Local (smoke tests only)**
```bash
python3.11 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python datasets/generate_clickstream.py

> Workspace setup: see **[Secrets & Config](docs/secrets-and-config.md)**.

> **Optional:** Local Spark/Delta smoke requires a JDK. If you don’t want to install Java now, skip it and run the labs later in Databricks.
