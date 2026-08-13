#!/usr/bin/env python3
"""Publish one practical computer science learning topic every day."""

import json
import re
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
TOPICS_FILE = ROOT / "curriculum" / "topics.json"
LEARNING_DIR = ROOT / "learning"
START_DATE = date(2026, 8, 13)
TIMEZONE = ZoneInfo("Asia/Jakarta")


def slugify(value):
    value = value.lower().replace("&", "and")
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")


def topic_for_day(today, topics):
    day_number = (today - START_DATE).days
    return day_number, topics[day_number % len(topics)]


def lesson_markdown(today, number, topic, next_topic):
    return f"""# Day {number + 1}: {topic["title"]}

> **Track:** {topic["category"]}  
> **Date:** {today.isoformat()}  
> **Estimated time:** 45–60 minutes

## Why this matters

{topic["focus"]}

This topic appears in real engineering decisions. Learn the trade-offs first. Memorizing terminology without understanding the decision is not enough.

## Learning plan

1. **Understand, 15 minutes**  
   Define the main concepts in your own words. Identify the problem each concept solves.

2. **Compare, 10 minutes**  
   Write at least three trade-offs. Include performance, complexity, reliability, or maintainability where relevant.

3. **Build, 20 minutes**  
   {topic["exercise"]}

4. **Verify, 5 minutes**  
   Answer the checkpoint questions below without reopening your notes.

## Practical task

{topic["exercise"]}

### Definition of done

- [ ] I can explain the concept without reading a definition.
- [ ] I can name one appropriate use case.
- [ ] I can name one case where it is a poor choice.
- [ ] I completed the practical task or wrote its pseudocode.
- [ ] I recorded one remaining question.

## Checkpoint

1. What problem does this concept solve?
2. What is its main trade-off?
3. What breaks when it is implemented carelessly?
4. How would you explain it to another developer in two minutes?

## Personal notes

Add your notes below if you study this topic manually.

- Key insight:
- Example:
- Remaining question:

## Next topic

**{next_topic["title"]}**, in the **{next_topic["category"]}** track.
"""


def dashboard_markdown(today, number, topic, next_topic, lesson_path, total):
    progress = (number % total) + 1
    return f"""## Today's learning mission

| Field | Value |
|---|---|
| Day | **{number + 1}** |
| Topic | **[{topic["title"]}]({lesson_path.as_posix()})** |
| Track | {topic["category"]} |
| Time box | 45–60 minutes |
| Curriculum position | {progress} of {total} |
| Next | {next_topic["title"]} |

### Focus

{topic["focus"]}

### Practical task

{topic["exercise"]}

[Open today's complete lesson →]({lesson_path.as_posix()})
"""


def main():
    now = datetime.now(TIMEZONE)
    today = now.date()
    topics = json.loads(TOPICS_FILE.read_text(encoding="utf-8"))
    number, topic = topic_for_day(today, topics)
    next_topic = topics[(number + 1) % len(topics)]

    LEARNING_DIR.mkdir(exist_ok=True)
    lesson_path = Path("learning") / f"{today.isoformat()}-{slugify(topic['title'])}.md"
    absolute_lesson = ROOT / lesson_path
    absolute_lesson.write_text(
        lesson_markdown(today, number, topic, next_topic),
        encoding="utf-8",
    )

    readme = README.read_text(encoding="utf-8")
    start = "<!-- DAILY_LEARNING:START -->"
    end = "<!-- DAILY_LEARNING:END -->"
    before, remainder = readme.split(start, 1)
    _, after = remainder.split(end, 1)
    dashboard = dashboard_markdown(
        today, number, topic, next_topic, lesson_path, len(topics)
    )
    README.write_text(
        f"{before}{start}\n{dashboard}\n{end}{after}",
        encoding="utf-8",
    )
    print(f"Published Day {number + 1}: {topic['title']}")


if __name__ == "__main__":
    main()
