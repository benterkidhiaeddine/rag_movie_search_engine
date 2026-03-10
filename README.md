# RAG Search Engine

A keyword-based movie search engine built with Python, using token stemming and stop-word filtering.

## Prerequisites

- Python 3.13 or higher
- [uv](https://docs.astral.sh/uv/) (recommended) **or** `pip`

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd rag_course
```

### 2. Create and activate a virtual environment

**Using uv (recommended):**

```bash
uv venv
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\activate      # Windows
```

### 3. Install dependencies

**Using uv:**

```bash
uv  sync
```

## Usage

Run the search CLI from the `cli/` directory:

```bash
cd cli
python keyword_search_cli.py search "space adventure"
```

### Available commands

| Command          | Description              |
| ---------------- | ------------------------ |
| `search <query>` | Search movies by keyword |

### Example

```
$ python keyword_search_cli.py search "dark knight"
Searching for: dark knight
1. The Dark Knight
2. The Dark Knight Rises
```

## Project Structure

```
rag_course/
├── pyproject.toml          # Project metadata and dependencies
├── README.md
├── cli/
│   ├── keyword_search_cli.py   # CLI entry point
│   └── lib/
│       ├── keyword_search.py   # BM25-style keyword search logic
│       └── search_utils.py     # Tokenization, stop-word removal, stemming
└── data/
    ├── movies.json             # Movie database
    └── stopwords.txt           # Stop-words list
```
