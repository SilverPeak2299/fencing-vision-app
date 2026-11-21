# Formal Requirements

This directory is the normative requirements source for Fencing Vision. The requirements describe externally observable system behaviour and data integrity without assuming a particular application or deployment architecture.

## Documents

- `core-product.sdoc` — identity, clip management, media handling, and lifecycle behaviour.
- `analysis.sdoc` — analysis processing, analytics data, result exploration, and reproducibility.
- `sharing-and-privacy.sdoc` — private access, controlled sharing, security, retention, and deletion.
- `requirements.sgra` — the shared StrictDoc grammar.
- `strictdoc_config.py` — project-level StrictDoc configuration.

## Requirement conventions

- UIDs use stable domain prefixes such as `REQ-AUTH`, `REQ-CLIP`, `REQ-ANALYSIS`, and `REQ-PRIVACY`.
- `SOURCE` points to a capability in `docs/product/product-brief.md`.
- New requirements begin as `Draft`. `Active`, `Deferred`, and `Retired` are reserved lifecycle states.
- A requirement statement describes one independently verifiable behaviour using **shall**.
- `VERIFICATION` records the intended verification approach. It does not imply that coverage automation has already been configured.

## Local StrictDoc usage

With StrictDoc installed:

```sh
strictdoc export docs/requirements
strictdoc server docs/requirements
```

Generated output belongs under `docs/requirements/output/` and should not be committed.
