# Copilot Instructions for Python_Course_Felix_Kjellberg_DE25

## Project Overview
This repository is a Python course focused on teaching fundamental programming concepts through code-alongs, exercises, and video tutorials. The structure is organized for incremental learning, with each topic in its own directory and supporting Jupyter notebooks.

## Directory Structure
- `code_alongs/` — Step-by-step instructional notebooks for each topic (e.g., input/output, control structures).
- `exercises/` — Practice notebooks and markdown files. Not compulsory, but essential for mastering concepts. Glossary sections may be included.
- `Video_tutorials/` — Supplementary notebooks for each topic, mirroring code_alongs structure.

## Key Patterns & Conventions
- All instructional content is in Jupyter notebooks (`.ipynb`). Each notebook is self-contained and uses clear markdown explanations followed by Python code cells.
- Exercises may include glossary sections. Summarize glossary terms in your own words for deeper understanding.
- Naming conventions: Folders and files use topic-based names (e.g., `04_input_output`, `a)_if_statements.ipynb`).
- No build system or test framework is present; focus is on interactive notebook execution.
- No external dependencies are required for most notebooks. If a notebook requires a package, it should be installed in the notebook itself.

## Developer Workflow
- Open notebooks in VS Code or Jupyter and run cells interactively.
- For exercises, use any tool (including LLMs) to assist, but prioritize learning and understanding over copying solutions.
- No automated testing or CI/CD is configured; manual validation by running notebook cells is expected.

## Integration Points
- No cross-component communication or advanced architecture. Each notebook is independent.
- No external APIs or data sources are integrated by default.

## Examples
- See `code_alongs/05_control_structures/a)_if_statements.ipynb` for patterns: markdown explanation, code cell, and nested if statement example.
- See `exercises/exercise_0.ipynb` for exercise format.

## Special Notes
- If adding new exercises, follow the existing markdown + code cell pattern.
- If updating glossary, encourage summarization in user's own words.
- No `.github/copilot-instructions.md` previously existed; this file now serves as the authoritative guide for AI agents.

---
For questions or unclear conventions, review the main `README.md` and exercise `README.md` for additional context. Iterate and ask for feedback if any section is incomplete or ambiguous.
