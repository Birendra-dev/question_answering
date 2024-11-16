```markdown
# Project Setup Guide

## To Run This Project

1. Create virtual environment using UV (recommended) or other package manager:
```bash
uv venv --seed --python 3.9
```

2. Activate the virtual environment (in bash):
```bash
source .venv/Scripts/activate
```

3. To download all packages:
```bash
uv sync
```

For downloading model, visit Telegram or DM me in Telegram.

---
*Note: UV package manager is recommended for better performance and dependency management.*
```
<!-- python -m ensurepip --upgrade -->
<!-- pip install spacy -->

<!-- python -m spacy download en_core_web_sm -->

<!-- clear and rebuild database -->
rm db.sqlite3
python manage.py migrate

<!-- anuj anuj@gmail.com anuj1234 -->