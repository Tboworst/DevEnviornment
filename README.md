# DevEnvironment

A CLI tool that scaffolds a project for you based on the options you select.

## What it generates

- Backend file in your chosen language (`main.go`, `main.py`, `main.java`, `main.ts`)
- Database setup file for Postgres or SQLite
- Frontend starter file in a `frontend/` folder (React, Vue, Svelte, or HTML)
- `.gitignore` tailored to your backend language
- Dependency file (`requirements.txt`, `go.mod`, `package.json`, or `pom.xml`)
- `Dockerfile` for your backend language
- `README.md` describing the generated project

## Installation

```bash
git clone https://github.com/Tboworst/DevEnviornment.git
cd DevEnviornment
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Usage

```bash
python main.py <project-name>
```

You will be prompted to select:
1. Backend language — Go, Python, Java, or TypeScript
2. Frontend framework — React, Vue, Svelte, HTML, or None
3. Database — Postgres, SQLite, or neither

## Example

```bash
python main.py myapp
```

Generates:
```
myapp/
  main.go
  postgres.go
  frontend/
    App.jsx
  .gitignore
  go.mod
  Dockerfile
  README.md
```

## Project Structure

| File | Purpose |
|------|---------|
| `main.py` | CLI entry point, wires everything together |
| `languages.py` | Backend code templates |
| `databases.py` | Database setup templates |
| `dockergeneration.py` | Dockerfile templates |
| `others.py` | README, gitignore, deps, and frontend templates |
