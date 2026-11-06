# ChatGPT + GitHub + Google Colab Workflow

![Workflow banner](assets/banner.svg)

[![Tests](https://github.com/javidjamae/chatgpt-github-colab-workflow/actions/workflows/test.yml/badge.svg)](https://github.com/javidjamae/chatgpt-github-colab-workflow/actions/workflows/test.yml)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/javidjamae/chatgpt-github-colab-workflow/blob/main/notebooks/signup_experiment.ipynb)

**A copyable starter project for developing Jupyter notebooks with ChatGPT and Codex, testing them in GitHub, and sharing interactive results through Google Colab.**

This repo is intentionally a complete working example: fictional signup data, statistical analysis, visualizations, optional interactive widgets, reusable Python code, tests, and GitHub Actions.

> **Beginner-friendly path:** Fork this repository or click **Use this template** if the owner enables GitHub's template setting. Then connect your own GitHub account to ChatGPT and Codex. No one needs access to the original owner's accounts.

## Quick start: run the example

1. Click **[Open the notebook in Colab](https://colab.research.google.com/github/javidjamae/chatgpt-github-colab-workflow/blob/main/notebooks/signup_experiment.ipynb)**.
2. In Colab, choose **Runtime → Run all**. Colab may ask for approval to execute notebook code.
3. Inspect the synthetic data preview, conversion charts, z-test, confidence interval, and sampling simulation.
4. Change `SAMPLE_SIZE`, `SEED`, and `RELATIVE_LIFT` to explore different scenarios. The optional widget sliders provide another way to experiment.

The notebook runs from a GitHub checkout. In a fresh Colab runtime it clones the public repository; in GitHub Actions it uses the local checkout. The notebook uses **fake data only**, and it requires no API keys.

## Set up your own copy, step by step

### Step 1: Make a GitHub repository

You need a GitHub account. On this repository choose **Fork** to create `YOUR_USERNAME/chatgpt-github-colab-workflow`. Alternatively, if the original owner enables GitHub's **Template repository** setting, choose **Use this template → Create a new repository** to start without fork history.

**Keep your fork public for the simplest Colab workflow.** For private repositories, GitHub and Colab authentication and file access require additional configuration; the direct public launch URL and built-in notebook clone won't work unchanged.

Replace `javidjamae/chatgpt-github-colab-workflow` in the following places with your own `YOUR_USERNAME/YOUR_REPO`:
- The notebook's `REPO_URL` and any links you intend to publish.
- The README's Colab links and GitHub Actions badge.
- Any course or documentation links pointing to the original example.

If you fork the project and leave the notebook's `REPO_URL` unchanged, the Colab notebook will import Python code from the original repository, **not your fork**.

### Step 2: Connect GitHub to ChatGPT

1. In **ChatGPT**, open **Settings → Apps** (the wording/location may vary by client) and look for **GitHub**.
2. Select **Connect** or the equivalent action and follow GitHub's authorization prompts.
3. Select the GitHub account or organization and explicitly grant access to **your repository** (or a limited selection of repositories). If already connected, use the GitHub app's configuration/permissions controls to add your new repository.
4. Back in ChatGPT, verify access by asking: **“Read the README from `YOUR_USERNAME/YOUR_REPO` and tell me which branch it uses.”**
5. For repository edits, use **Codex** with GitHub access or an available GitHub write integration. A read-only GitHub connection in ChatGPT does **not** by itself authorize or enable write actions.

**Permissions and security:** GitHub access is governed by the specific app authorization and your own GitHub account rights. Start with access to only the example repository. Review access later under GitHub **Settings → Applications**. Do not paste personal access tokens, secrets, or credentials into chat or notebooks.

### Step 3: Connect Google Drive to ChatGPT (optional, but useful)

This connection is for accessing **files in your Google Drive**, including Colab notebooks saved there. It is **not necessary** to run the public GitHub notebook in Colab.

1. In ChatGPT, open **Settings → Apps** and locate **Google Drive**.
2. Choose **Connect** and sign into the Google account that owns your Drive notebooks.
3. Review Google's permission request and approve only if you want ChatGPT to access your Drive content.
4. Verify the connection by asking ChatGPT to find a specific notebook in Google Drive, or by sharing its Drive link in the conversation.
5. Remember that a Drive connection does **not** give ChatGPT access to the live Google Colab execution kernel, GPU, or running cell state.

Google Workspace or organization administrators may restrict app connections. Available ChatGPT tools and write privileges depend on your plan, workspace, and connected app.

### Step 4: Connect GitHub to Codex for actual development

1. Open **[Codex](https://chatgpt.com/codex)** and connect your GitHub account if prompted.
2. Allow the Codex GitHub integration to access **your fork/repository**. Confirm repository selection if GitHub prompts for specific repositories.
3. Start a task against your repository. Ask Codex to create a feature branch, implement a notebook change, run tests, and open a pull request.
4. Review the diff and GitHub Actions checks before merging to `main`. Codex environment/network permissions and execution capabilities depend on the environment.

**Example Codex task:**

> In `YOUR_USERNAME/YOUR_REPO`, create a feature branch and extend `notebooks/signup_experiment.ipynb` with a plot showing signup rates over different sample sizes. Put reusable calculations into `src/experiment.py`, add tests, execute the entire notebook from a clean Python kernel, and open a pull request. Do not modify `main` directly.

### Step 5: Verify your GitHub-to-Colab link

For a public repo, the direct launch URL follows this pattern:

```text
https://colab.research.google.com/github/YOUR_USERNAME/YOUR_REPO/blob/main/notebooks/signup_experiment.ipynb
```

Open it after your fork's `main` contains the notebook. In Colab, run **Runtime → Run all**. A Colab session is a copy/runtime workspace: editing cells in Colab does not automatically commit changes to GitHub.

### Step 6: Test changes automatically

GitHub Actions runs on pushes and pull requests:
- `python -m pytest -q` tests deterministic data generation and the experiment calculations.
- `nbclient` executes **every notebook cell from a fresh kernel** so CI fails on unexpected exceptions.

In GitHub, open **Actions → Test notebook and experiment** or inspect the checks on your pull request. If the Actions workflow is disabled on your fork, enable it after reviewing the YAML. The CI environment is not the same as a hosted Colab runtime, so also test Colab-specific widgets or GPU features in Colab.

## Repository contents

```text
.github/workflows/test.yml       GitHub Actions tests + notebook execution
assets/banner.svg               README banner
notebooks/signup_experiment.ipynb Interactive Colab notebook
src/experiment.py                Deterministic fake data + frequentist A/B analysis
tests/test_experiment.py         Pytest unit tests
requirements.txt                 Python dependencies
AGENTS.md                        Guidance for Codex / coding agents
README.md                        You are here
```

## What the notebook demonstrates

- **Synthetic data:** 12,000 fictional visitors randomized between control and treatment, with device-level base conversion differences.
- **Visualizations:** Conversion-rate comparisons, device segmentation, a confidence interval, and sampling variability across repeated experiments.
- **Statistical analysis:** Two-sided pooled z-test for conversion-rate difference, plus an approximate 95% confidence interval for absolute lift.
- **Interactivity:** Optional sliders for sample size, treatment effect, and random seed.
- **Quality controls:** Reproducible random number generation, unit tests, and headless notebook execution on CI.

The data and experiment outcomes are fabricated for education. Do not interpret results as real product research. Normal-approximation methods have assumptions and may be unsuitable for very small samples or extreme proportions.

## Local development

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
python -m pip install -r requirements.txt
python -m pytest -q
python - <<'PY'
import nbformat
from nbclient import NotebookClient
nb = nbformat.read("notebooks/signup_experiment.ipynb", as_version=4)
NotebookClient(nb, timeout=180, kernel_name="python3", resources={"metadata":{"path":"."}}).execute()
print("Notebook executed successfully")
PY
```

## Suggested ongoing workflow

1. Describe a notebook change to ChatGPT or Codex.
2. Codex creates a feature branch and implements the change.
3. Unit tests and clean-kernel notebook execution pass in GitHub Actions.
4. Review and merge the pull request.
5. Launch the **latest** notebook from the GitHub-to-Colab link. For stable course material, replace `main` in the URL with an immutable release tag or commit and use a matching `REPO_REF` in the notebook.

If a notebook is already open in someone's browser, it won't automatically reload after a GitHub commit. Participants should reopen it to pick up the new version.

## Troubleshooting

| Problem | Check |
| --- | --- |
| ChatGPT can't find the repository | Correct account and repository selection in the GitHub connection; workspace restrictions |
| ChatGPT can read but not edit | Reading and writing are different capabilities. Use a Codex environment or GitHub integration with write access |
| Codex can't see your fork | Update the Codex GitHub installation's repository access |
| ChatGPT can't see Drive files | Connect Google Drive to the correct account, verify permissions and admin restrictions |
| Colab loads code from the wrong repo | Update `REPO_URL` in the notebook to your fork |
| Colab says repository not found | Verify the repo is public or configure a private-repo authentication strategy |
| GitHub Actions isn't running | Enable Actions on your fork after reviewing the workflow |
| Notebook works in CI but not Colab | Compare library versions, runtime configuration, hardware, and interactive widgets |

## Official references

- [OpenAI Codex](https://chatgpt.com/codex)
- [ChatGPT Help Center](https://help.openai.com/)
- [GitHub app permission management](https://github.com/settings/installations)
- [Google Colab](https://colab.research.google.com/)
- [GitHub Actions documentation](https://docs.github.com/en/actions)

## License

See [LICENSE](LICENSE).
