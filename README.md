# Eric's Daily Dev Dashboard

A small automated snapshot of my GitHub activity, refreshed every day.

<!-- DASHBOARD:START -->
## Daily snapshot

| Metric | Value |
|---|---:|
| Last refresh | Preparing first run |
| Public repositories | Pending |
| Recent activity | Pending |
| Daily byte | Good systems make consistency repeatable |

<!-- DASHBOARD:END -->

## About

This repository turns public GitHub activity into a compact daily engineering log. A scheduled GitHub Actions workflow collects current data, generates a dated snapshot, and refreshes this README.

## Features

- Daily public GitHub activity summary
- Repository and language statistics
- Dated Markdown snapshots
- A rotating Daily Byte
- Automatic updates through GitHub Actions
- Manual workflow runs when needed

## How it works

```text
GitHub API -> Python generator -> Daily snapshot -> Automated commit
```

## Project structure

```text
.
├── .github/workflows/daily-update.yml
├── daily/
├── scripts/update_dashboard.py
└── README.md
```

## Run locally

```bash
GITHUB_USER=erick-surbakti python scripts/update_dashboard.py
```

No third-party Python packages are required.

---

<sub>Keeping the contribution garden watered, one useful snapshot at a time.</sub>
