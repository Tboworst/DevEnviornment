def generate_readme(name, backend, database):
    # Join the list of selected databases into a readable string e.g. "Postgres, Sqlite"
    db_list = ", ".join(database) if database else "None"

    return f"""# {name}

## About
Backend language: {backend}
Databases: {db_list}

## Getting Started
1. Navigate into the project folder: `cd {name}`
2. Open `main.{backend}` to start coding

## Files
- `main.{backend}` — entry point for your {backend} backend
- `README.md` — this file

## License
MIT
"""


# Each gitignore function returns the patterns for that language.
# Git reads .gitignore line by line and skips any file matching those patterns.

def generate_gitignore_python():
    return """# Python
__pycache__/
*.pyc
*.pyo
.venv/
.env
*.egg-info/
dist/
build/
"""

def generate_gitignore_go():
    return """# Go
# Compiled binary (same name as the project folder)
/main

# Environment variables
.env
"""

def generate_gitignore_java():
    return """# Java
*.class
*.jar
target/
.env
"""

def generate_gitignore_ts():
    return """# TypeScript / Node
node_modules/
dist/
.env
*.js.map
"""


# Each dependencies function returns the starter file for managing packages.
# This gives the project a foundation to add libraries later.

def generate_deps_python():
    return """# Add your dependencies here, one per line
# Example: requests==2.31.0
"""

def generate_deps_go():
    return """module myapp

go 1.21
"""

def generate_deps_java():
    return """<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.example</groupId>
  <artifactId>myapp</artifactId>
  <version>1.0</version>
</project>
"""

def generate_deps_ts():
    return """{
  "name": "myapp",
  "version": "1.0.0",
  "scripts": {
    "start": "ts-node main.ts"
  },
  "dependencies": {}
}
"""
