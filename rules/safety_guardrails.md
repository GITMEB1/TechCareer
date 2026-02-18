# Safety Guardrails (Hard Constraints)

## Terminal & file system safety
**Never** run destructive or irreversible commands without explicit user confirmation.
This includes (not exhaustive):
- `rm`, `rmdir`, `del`, `erase`, `format`, `mkfs`, `diskpart`, recursive deletes, glob deletes
- any command targeting root drives (e.g., `C:\`, `D:\`, `/`, `/home`, `/mnt`)
- “clean”, “wipe”, “purge” commands

## Allowed default actions
- Read-only inspection commands (`ls`, `dir`, `cat`, `type`, `git status`, `git diff`)
- Create *new* files in the workspace
- Run tests/builds that do not modify system state outside the repo

## Confirmation protocol
Before any risky command:
1. Show exact command
2. Explain impact in one sentence
3. Require the user to respond: **“CONFIRM: run it”**

## Data privacy
- Do not print secrets or credentials.
- Treat `.env`, tokens, cookies, API keys as sensitive.
- If found, redact and warn.

## Web browsing safety
- Prefer official documentation sources first.
- Do not paste large verbatim copyrighted text.
