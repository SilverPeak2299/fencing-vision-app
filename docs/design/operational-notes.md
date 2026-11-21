# Deferred Operational Notes

These concerns came from the original requirements draft but are not product requirements yet. They should inform later architecture and infrastructure decisions.

## Runtime safety

- Bound worker concurrency, video duration and resolution, processing time, memory, and CPU or GPU consumption.
- Load and warm pose models once per worker process rather than once per job.
- Isolate temporary files per job and clean them up after success, failure, timeout, or cancellation.
- Give deployable web, API, and analytics components health and readiness checks when those components exist.

## Observability

- Monitor queue depth, job duration, failure rate, unsuitable-clip rate, storage use, and worker resource use.
- Include correlation and analysis identifiers in structured logs without recording credentials, tokens, or private media URLs.

## Environments and reproducibility

- Keep development, staging, and production secrets and data stores separate.
- Manage database and storage-schema changes through committed, repeatable migrations.
- Make dependency, model, and analytics-configuration versions reproducible for each deployment.
- Review model and dependency licences before public or commercial deployment.

## Verification fixture

Retain at least one fixed test clip for validating frame alignment, missing detections, result-schema validity, keypoint coverage, and deterministic derivation within defined tolerances once the testing approach is chosen.
