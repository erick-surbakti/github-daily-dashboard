#!/usr/bin/env python3
"""Generate a compact daily GitHub activity dashboard."""

import json
import os
import random
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

USER = os.getenv("GITHUB_USER", "erick-surbakti")
TOKEN = os.getenv("GH_TOKEN", "")
ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DAILY_DIR = ROOT / "daily"

BYTES = [
    "Automate the repeatable. Think carefully about the rest.",
    "Small commits make progress easier to inspect.",
    "Readable code is a feature for your future self.",
    "A useful metric should change a decision.",
    "Good systems make consistency repeatable.",
    "Ship small, verify, then improve.",
    "Documentation reduces the cost of returning.",
]


def request(path):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "github-daily-dashboard",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    req = urllib.request.Request(f"https://api.github.com{path}", headers=headers)
    with urllib.request.urlopen(req, timeout=20) as response:
        return json.load(response)


def compact_number(value):
    if value >= 1000:
        return f"{value / 1000:.1f}k"
    return str(value)


def main():
    now = datetime.now(timezone.utc)
    date = now.date().isoformat()
    repos = request(f"/users/{USER}/repos?per_page=100&sort=updated")
    events = request(f"/users/{USER}/events/public?per_page=100")

    owned = [repo for repo in repos if not repo.get("fork")]
    languages = Counter(
        repo["language"] for repo in owned if repo.get("language")
    )
    stars = sum(repo.get("stargazers_count", 0) for repo in owned)
    forks = sum(repo.get("forks_count", 0) for repo in owned)
    active_today = [
        event for event in events if event.get("created_at", "").startswith(date)
    ]
    event_types = Counter(event.get("type", "Activity") for event in active_today)
    latest = owned[0]["name"] if owned else "No public repository yet"

    random.seed(date)
    daily_byte = random.choice(BYTES)
    language_text = ", ".join(
        f"{name} ({count})" for name, count in languages.most_common(5)
    ) or "Not enough public data"
    activity_text = ", ".join(
        f"{name.removesuffix('Event')} ({count})"
        for name, count in event_types.most_common()
    ) or "Quiet build day"

    dashboard = f"""## Daily snapshot

| Metric | Value |
|---|---:|
| Last refresh | {now.strftime("%Y-%m-%d %H:%M UTC")} |
| Public repositories | {len(owned)} |
| Public events today | {len(active_today)} |
| Stars received | {compact_number(stars)} |
| Forks received | {compact_number(forks)} |
| Recently updated | [{latest}](https://github.com/{USER}/{latest}) |

### Current signals

- Languages: {language_text}
- Today's activity: {activity_text}
- Daily Byte: {daily_byte}
"""

    text = README.read_text(encoding="utf-8")
    start = "<!-- DASHBOARD:START -->"
    end = "<!-- DASHBOARD:END -->"
    before, remainder = text.split(start, 1)
    _, after = remainder.split(end, 1)
    README.write_text(
        f"{before}{start}\n{dashboard}\n{end}{after}", encoding="utf-8"
    )

    DAILY_DIR.mkdir(exist_ok=True)
    snapshot = f"""# Daily snapshot: {date}

| Metric | Value |
|---|---:|
| Public repositories | {len(owned)} |
| Public events | {len(active_today)} |
| Stars | {stars} |
| Forks | {forks} |
| Recently updated | [{latest}](https://github.com/{USER}/{latest}) |

## Signals

- Languages: {language_text}
- Activity: {activity_text}
- Daily Byte: {daily_byte}
"""
    (DAILY_DIR / f"{date}.md").write_text(snapshot, encoding="utf-8")
    print(f"Dashboard updated for {date}")


if __name__ == "__main__":
    main()
