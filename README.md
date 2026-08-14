# Eric's Daily CS Learning Path

A practical computer science topic, published automatically every day.

This repository answers one question each morning: **what useful technical concept should I learn today?**

<!-- DAILY_LEARNING:START -->
## Today's learning mission

| Field | Value |
|---|---|
| Day | **3** |
| Topic | **[HTTP status codes that matter](learning/2026-08-15-http-status-codes-that-matter.md)** |
| Track | API & Web |
| Time box | 45–60 minutes |
| Curriculum position | 3 of 110 |
| Next | Headers, cookies, and tokens |

### Focus

Bedakan 200, 201, 202, 204, 400, 401, 403, 404, 409, 422, 429, dan kelompok 5xx.

### Practical task

Buat tabel status code untuk flow registrasi akun.

[Open today's complete lesson →](learning/2026-08-15-http-status-codes-that-matter.md)

<!-- DAILY_LEARNING:END -->

## What gets published

Every daily lesson contains:

- A focused technical concept
- The reason it matters in real engineering work
- A 45–60 minute learning plan
- A practical design or coding exercise
- A definition-of-done checklist
- Checkpoint questions
- Space for personal notes
- A preview of the next topic

## Curriculum

The curriculum currently contains **110 practical topics** across:

- API and web engineering
- Networking
- Databases and caching
- Programming and software design
- Testing and security
- DevOps and cloud
- Distributed systems
- System design
- Core computer science
- Architecture and engineering practice

Topics progress one per day and repeat only after the full curriculum is complete.

## Automation

GitHub Actions runs every day at **00:17 WIB**. It selects the next curriculum item, creates a dated lesson under `learning/`, refreshes this README, and commits the generated material.

```text
Curated curriculum -> Daily lesson generator -> Markdown lesson -> GitHub commit
```

The workflow can also be launched manually from the Actions tab.

## Project structure

```text
.
├── .github/workflows/daily-update.yml
├── curriculum/topics.json
├── learning/
├── scripts/update_dashboard.py
└── README.md
```

## Run locally

```bash
python scripts/update_dashboard.py
```

Python 3.9 or newer is enough. No third-party packages are required.

---

<sub>One focused concept a day. Learn it, build something small, then move forward.</sub>
