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

def generate_deps_python(name):
    return """# Add your dependencies here, one per line
# Example: requests==2.31.0
"""

def generate_deps_go(name):
    # module name matches the project name the user gave
    return f"""module {name}

go 1.21
"""

def generate_deps_java(name):
    # artifactId matches the project name the user gave
    return f"""<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.example</groupId>
  <artifactId>{name}</artifactId>
  <version>1.0</version>
</project>
"""

def generate_deps_ts(name):
    # name field matches the project name the user gave
    return f"""{{
  "name": "{name}",
  "version": "1.0.0",
  "scripts": {{
    "start": "ts-node main.ts"
  }},
  "dependencies": {{}}
}}
"""


def generate_react():
    # A minimal React component — the entry point of a React app
    return """import React from 'react';

function App() {
  return (
    <div>
      <h1>Hello from React</h1>
    </div>
  );
}

export default App;
"""

def generate_vue():
    # A Vue single file component — template, script, and style in one file
    return """<template>
  <div>
    <h1>Hello from Vue</h1>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
</style>
"""

def generate_svelte():
    # A Svelte component — simpler syntax, no boilerplate needed
    return """<script>
  let message = "Hello from Svelte";
</script>

<main>
  <h1>{message}</h1>
</main>

<style>
</style>
"""

def generate_html():
    # Plain HTML starter — no framework, just a basic page
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My App</title>
</head>
<body>
  <h1>Hello, world!</h1>
</body>
</html>
"""
