# Open Decisions

These questions are deliberately unresolved. They should not be encoded as architecture or deployment requirements until a decision is made.

## Product and media limits

- Supported identity providers.
- Maximum clip duration, file size, resolution, frame rate, and video formats.
- Storage retention periods and the account-deletion process.
- Minimum recording-quality thresholds for the first YOLO pose experiment.

## Application shape

- One deployable application or separate frontend and backend applications.
- Whether the analytics worker lives in the same codebase/package as the application or behind an internal service boundary.
- Where stable public API contracts are necessary versus in-process interfaces.

## Technology and operations

- Job queue, object storage, and database technologies.
- Deployment targets and environment topology.
- Whether infrastructure begins with a Dockerfile, Helm, Terraform, or another approach.
- Concrete limits for worker concurrency, processing time, memory, CPU, and GPU use.
- Monitoring, alerting, backup, and disaster-recovery choices.

The repository may gain an `/infra` directory when one of these choices produces real configuration. No speculative deployment configuration is required yet.
