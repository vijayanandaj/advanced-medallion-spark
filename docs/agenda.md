# Four-Day Advanced Agenda (8 Half-Days)

**Format:** Day 1 (H1–H2), Day 2 (H3–H4), Day 3 (H5–H6), Day 4 (H7–H8)  
**Tooling:** Azure Databricks (DBR 15.x LTS + Photon), ADLS Gen2, Event Hubs/Kafka, Unity Catalog if enabled

## Half-Day 1 — Environment Setup & Validation
- Workspace, autoscaling cluster, storage access (SP + secrets), UC schema
- Event Hubs/Kafka topic smoke test; repo clone  
**Lab:** `labs-advanced/hd1_env_setup/01_env_validation.py`

## Half-Day 2 — Incremental Bronze (Batch) + Spark Basics
- Auto Loader: schema inference/evolution, corrupt record handling, checkpoints
- Idempotent batch reruns; partitioning basics  
**Lab:** `labs-advanced/hd2_incremental_bronze_batch/01_auto_loader_bronze.py`

## Half-Day 3 — Incremental Silver (CDC) + Joins
- Dedup (windows), surrogate keys, `MERGE INTO` for CDC
- Broadcast vs shuffle joins; shuffle partitions  
**Lab:** `labs-advanced/hd3_incremental_silver_cdc/01_incremental_merge_silver.py`

## Half-Day 4 — Streaming Bronze (Event Hubs/Kafka)
- Structured Streaming, watermarks, exactly-once patterns
- Replay/backfill drill; streaming internals primer  
**Lab:** `labs-advanced/hd4_streaming_bronze_eventhubs/01_stream_bronze_eventhubs.py`

## Half-Day 5 — Streaming Silver (Dedup + Late Data)
- Stateful dedup with event-time watermarks; out-of-order events
- Merge to Silver; negative test: broken checkpoint recovery  
**Lab:** `labs-advanced/hd5_streaming_silver_dedup_late/01_stream_silver_dedup.py`

## Half-Day 6 — Gold Serving (KPIs)
- Dim/fact modeling, sessionization, KPIs (CTR, dwell time)
- Enrichment joins; windows & performance implications  
**Lab:** `labs-advanced/hd6_gold_serving_kpis/01_gold_kpis.py`

## Half-Day 7 — Advanced Spark Transformations & Performance
- Shuffle minimization, skew handling (salting/hints), AQE  
**Lab:** `labs-advanced/hd7_advanced_spark_perf/01_perf_transformations.py`

## Half-Day 8 — Delta Optimization & Ops
- Compaction/OPTIMIZE, CLUSTER BY/Z-ORDER, statistics
- DQ expectations, alerts, Jobs workflow (Bronze→Silver→Gold)  
**Lab:** `labs-advanced/hd8_delta_optimization_ops/01_delta_ops_ops.py`
