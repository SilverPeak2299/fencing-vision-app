# Initial Product Roadmap

This sequence describes product outcomes and does not prescribe a monolith or a frontend/backend split.

1. Establish the application routes, passwordless authentication, private clip records, and access control. Do not create anonymous users or guest sessions.
2. Add private media upload, the clip library, clip details, and complete deletion.
3. Add the asynchronous analysis lifecycle using a fake worker and representative versioned result data.
4. Build a generic result viewer for overlays, timeline events, metric charts, observations, and quality warnings.
5. Replace the fake worker with the first YOLO pose adapter while preserving raw keypoints and timestamps.
6. Add exploratory calculations for wrist trajectory, keypoint acceleration profiles, torso/hip timing, and estimated foot contact.
7. Add revocable sharing after private access controls have been tested.
