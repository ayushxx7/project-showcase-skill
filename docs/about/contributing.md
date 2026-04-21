# Contributing 🤝

We love contributions! Whether you're fixing a bug, adding a new feature, or improving the documentation, your help is appreciated.

## Development Setup

1. **Clone the Repo**:
   ```bash
   git clone https://github.com/ayushxx7/project-showcase-skill
   cd project-showcase-skill
   ```

2. **Setup Virtual Environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Install Documentation Tools**:
   ```bash
   pip install mkdocs-material
   ```

## Workflow

1. Create a new branch for your feature or bugfix.
2. Ensure any new logic is covered by tests in the `tests/` folder.
3. Update the `docs/` folder if you're adding new features or changing existing ones.
4. Open a Pull Request!

## Testing

Run the tests using `pytest`:

```bash
pytest tests/
```
