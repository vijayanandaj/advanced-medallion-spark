# Four-Day Advanced Agenda (8 Half-Days)

**Format:** Day 1 (H1–H2), Day 2 (H3–H4), Day 3 (H5–H6), Day 4 (H7–H8)  
**Tooling:** Azure Databricks (DBR 15.x LTS + Photon), ADLS Gen2, Event Hubs/Kafka, Unity Catalog if enabled

---

## Day 1 (Half-Day 1) — Environment Setup & Validation
- Azure Databricks workspace (DBR 15.x LTS with Photon)
- Autoscaling clusters (e.g., 2–8 workers)
- ADLS Gen2 storage access with service principal + secrets
- Unity Catalog schema (if enabled)
- Event Hubs/Kafka topic (clickstream) setup + streaming test
- Git repo cloning (starter notebooks, test templates)  
**Deliverable:** A ready lab environment for all participants.

---

## Day 1 (Half-Day 2) — Incremental Bronze (Batch) + Spark Basics
- Auto Loader ingestion with schema inference & evolution
- Handling corrupt records + checkpointing
- Idempotent batch reruns
- Spark primer #1: Partitioning basics (repartition vs coalesce)  
**Deliverable:** Incremental Bronze table with idempotent ingestion.

---

## Day 2 (Half-Day 3) — Incremental Silver (CDC) + Spark Joins Primer
- Deduplication patterns (dropDuplicates, window functions)
- Surrogate key generation for joins
- Incremental `MERGE INTO` for CDC
- Spark primer #2: Broadcast joins vs shuffle joins, shuffle partitions  
**Deliverable:** Incremental Silver table with CDC logic + test notebook.

---

## Day 2 (Half-Day 4) — Streaming Bronze (Event Hubs/Kafka)
- Structured Streaming ingestion from Event Hubs/Kafka
- Watermarks + late data tolerance
- Exactly-once semantics
- Replay/backfill drill (stop → restart → verify no duplicates)
- Spark primer #3: Streaming internals (micro-batch, state, triggers)  
**Deliverable:** Streaming Bronze pipeline + replay runbook.

---

## Day 3 (Half-Day 5) — Streaming Silver (Dedup + Late Data)
- Stateful deduplication with event-time watermarks
- Handling late/out-of-order data
- `MERGE INTO` Silver with upserts
- Negative test: broken checkpoint recovery  
**Deliverable:** Streaming Silver pipeline + validation notebook.

---

## Day 3 (Half-Day 6) — Gold Serving (KPIs)
- Dimension & fact modeling from Silver
- Window functions: sessionization, CTR, dwell time
- Enrichment with metadata dataset
- Visualize KPIs in Databricks SQL/Note
EOF
- Spark primer #4: Shuffle impact of window functions  
**Deliverable:** Gold fact/dim tables + KPI dashboard.

---

## Day 4 (Half-Day 7) — Advanced Spark Transformations & Performance
- Shuffle minimization (map-side combine, narrow vs wide transformations)
- Broadcast joins vs shuffle joins (real examples)
- Skew handling (salting, skew join hints)
- Adaptive Query Execution (AQE)  
**Deliverable:** Optimized transformations with Spark UI screenshots (before/after).

---

## Day 4 (Half-Day 8) — Delta Optimization & Ops
- File compaction (OPTIMIZE, autoOptimize)
- Z-ORDER / CLUSTER BY, ANALYZE STATISTICS
- Data Quality expectations on Silver
- Alerts on failures (SQL Alerts/Jobs)
- Orchestration: build Bronze→Silver→Gold workflow in Jobs  
**Deliverable:** Tuned Gold tables, DQ checks, alerting & workflows.
