# Development instructions for Codex and contributors

- Keep the notebook beginner-friendly and runnable top-to-bottom in a clean Google Colab runtime.
- Do not require credentials, paid APIs, private files, or Drive mounts.
- Data must be clearly labeled synthetic, with a fixed seed.
- Keep reusable experiment logic in `src/experiment.py`; notebook imports it after cloning the repository.
- Add assertions or tests for behavior changes.
- Run `python -m pytest -q` and execute `notebooks/signup_experiment.ipynb` with nbclient before submitting a PR.
- Never commit user data, tokens, service account keys, or generated notebook checkpoints.
