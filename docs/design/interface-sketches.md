# Interface Sketches

This document preserves the initial route and analytics-shape ideas. It is non-normative: names and boundaries may change when the application architecture is chosen. Product behaviour is defined by `docs/requirements`.

## Candidate web routes

```text
/
/login
/clips
/clips/new
/clips/:clipId
/clips/:clipId/analyses/:analysisId
/share/:shareToken
/settings
```

Authentication callback routes may be owned by the selected identity provider. A share token may be accepted before login, but no clip metadata or media should be revealed until the recipient has authenticated and the token has been validated.

## Candidate public API

If a public application API is needed, the initial proposal places routes under `/api/v1`:

```text
POST   /api/v1/clips
GET    /api/v1/clips
GET    /api/v1/clips/:clipId
PATCH  /api/v1/clips/:clipId
DELETE /api/v1/clips/:clipId

POST   /api/v1/clips/:clipId/analyses
GET    /api/v1/clips/:clipId/analyses
GET    /api/v1/analyses/:analysisId
GET    /api/v1/analyses/:analysisId/results

POST   /api/v1/clips/:clipId/share-links
GET    /api/v1/clips/:clipId/share-links
DELETE /api/v1/share-links/:shareLinkId
```

The analytics worker should use a separate internal interface and should not be exposed as an unauthenticated public API.

## Candidate analytics job contract

An analysis job should receive identifiers and configuration rather than a permanent public video URL. The worker should use short-lived authorised access to retrieve the source clip.

## Candidate result shape

```json
{
  "schemaVersion": "1.0",
  "analysisId": "analysis_123",
  "pipeline": {
    "name": "yolo-pose-lunge",
    "version": "0.1.0",
    "modelVersion": "initial-model",
    "configuration": {}
  },
  "status": "completed",
  "quality": {
    "score": 0.84,
    "warnings": []
  },
  "events": [
    {
      "type": "front_foot_contact",
      "timeSeconds": 1.42,
      "confidence": 0.76
    }
  ],
  "metrics": [
    {
      "type": "keypoint_acceleration",
      "subject": "weapon_wrist",
      "units": "normalised_coordinates_per_second_squared",
      "series": []
    }
  ],
  "observations": [
    {
      "type": "upward_wrist_motion",
      "startSeconds": 0.84,
      "endSeconds": 1.16,
      "confidence": 0.81,
      "message": "The weapon wrist travelled upward during the initial extension.",
      "supportingMetricIds": []
    }
  ],
  "artifacts": []
}
```

Large time series and artifacts may eventually be stored separately, provided clients receive a stable representation. Raw keypoint samples need source frame indices, timestamps, nullable coordinates, and confidence; the final schema should also describe the coordinate system and source media.
