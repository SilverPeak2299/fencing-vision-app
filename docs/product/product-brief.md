# Fencing Vision Product Brief

## Vision

Build a web application for exploring fencing movement with computer vision. A fencer uploads a short video of an action and receives visualisations, measurements, detected events, and plain-language observations derived from pose keypoints.

The initial product is an experimentation platform, not a definitive coaching or fault-diagnosis system. Its user experience and analytics contract should remain stable while pose models, measurements, and interpretation logic evolve independently.

## Initial audience

- Fencers who want to inspect their own movement.
- Authenticated coaches or other viewers invited to review one result.
- Developers and researchers iterating on the analytics pipeline.

## First supported recording

The first supported recording contains one fencer performing one lunge, filmed side-on with a stationary camera and the entire body visible.

## Product capabilities

These identifiers provide stable origins for the formal requirements in `docs/requirements`.

### CAP-ACCESS — Account and access

Fencers can authenticate without a password, manage their session, and record the context needed to interpret anatomical pose keypoints correctly.

### CAP-CLIPS — Private clip management

Fencers can prepare, upload, organise, inspect, edit, and delete short private fencing clips.

### CAP-ANALYSIS — Movement analysis and experimentation

Fencers can process a supported clip, inspect synchronised pose-derived results, understand quality limitations, and compare reproducible analysis versions.

### CAP-SHARING — Controlled review

Fencers can grant and revoke authenticated, read-only access to one clip and a selected analysis without exposing the rest of their library.

### CAP-TRUST — Privacy and data control

Private media and derived data remain access-controlled throughout upload, processing, viewing, export, sharing, retention, and deletion.

## Initial scope

- Mandatory passwordless authentication using magic links and selected identity providers.
- Private upload and storage of short fencing clips.
- A clip library and individual clip pages.
- Asynchronous analysis with clear processing states.
- A replaceable analytics worker, initially using a YOLO pose model.
- Playback with pose overlays, event markers, metric charts, and exploratory observations.
- Revocable sharing of individual clips and selected results.
- Versioned analytics results so experiments can be reproduced and compared.

## Non-goals

- Real-time or live-camera feedback.
- Authoritative coaching judgements or automatic scoring.
- Guaranteed real-world biomechanical measurements without camera calibration.
- Multi-person bout analysis, opponent tracking, or referee decisions.
- Blade-tip tracking or weapon-specific keypoints unless a later model supplies them.
- Support for every fencing action, camera angle, and recording environment.
- Coach accounts, comments, teams, subscriptions, or social features beyond read-only share links.
- Anonymous accounts, guest uploads, unauthenticated sharing, or migration of guest data into registered accounts.
