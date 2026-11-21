# User Journeys

These journeys describe the intended experience at product level. Detailed, testable behaviour belongs in the StrictDoc requirements.

## 1. Establish an identity and recording context

A fencer signs in with a magic link or supported identity provider. They can sign out and manage their active session. They record their weapon hand, stance, and direction of travel so anatomical left/right keypoints can be interpreted as lead/rear and weapon/non-weapon sides.

## 2. Prepare and upload a clip

The fencer reviews recording guidance, chooses a short fencing video, adds context such as action type and camera view, and selects the portion containing the action. If the recording or file is unsupported, the product explains why and how to correct it.

## 3. Manage a private clip library

The fencer sees their clips, thumbnails, dates, processing states, and available analysis versions. They can open a clip, edit its title or notes, and permanently delete the clip and its associated data.

## 4. Run and inspect an analysis

Before processing, the fencer can correct inferred handedness, stance, or movement direction. Processing happens asynchronously and communicates whether the analysis is queued, processing, complete, unsuitable, or failed.

For a completed analysis, the fencer watches the video with a synchronised skeleton overlay and explores events, trajectories, metric charts, observations, confidence, and quality warnings. Playback, scrubbing, overlays, charts, and event markers remain aligned.

## 5. Experiment and compare

The fencer can re-run an existing clip with a newer pipeline or configuration without replacing earlier results. They can compare versions and download raw keypoints or derived metrics for further exploration.

Developers and researchers can reproduce a result from its source-media metadata, pipeline and model versions, configuration, timestamps, raw detections, and derived outputs.

## 6. Share a result safely

The fencer creates a revocable link to one clip and a selected analysis, optionally with an expiry time. After authenticating, the recipient receives a read-only view without access to the owner's library or account. Revocation removes access immediately.
