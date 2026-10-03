# AI Command Center (local-first)
## Quick start
1. `python -m venv .venv` then activate it (Windows: `.venv\Scripts\activate`; Mac/Linux: `source .venv/bin/activate`)
2. `pip install -r requirements.txt`
3. `copy .env.example .env` (Windows) or `cp .env.example .env`, then set `OBSIDIAN_VAULT_PATH` to your vault folder.
4. `python run.py`, then open http://localhost:8765
5. In **Connections**, paste your Anthropic API key (and Brave Search key for the Research Bot). Keys go to your OS keychain, never to the vault.
6. Ask Jarvis: "Research trending keywords for handmade candles and save a note."
The first start creates `CommandCenter/` in your vault with Jarvis.md, ResearchBot.md, Brain.md and the folders.
## Etsy
1. Create an app at https://www.etsy.com/developers/register and copy the **keystring**; paste it in Connections.
2. In the Etsy app settings add the redirect URI exactly: `http://localhost:8765/api/etsy/callback`
3. Click **Connect Etsy**, approve, then **Test Etsy**. Commercial access needs Etsy's approval; until then limits are low.
## Safety
Bots start at Level 1 (every write needs your approval). Kill switch: dashboard button or create a file named `STOP` in `CommandCenter/`. Hard-blocked at every level: delete, refund, bulk, spend, security tools.
## Auto-start
Windows: Task Scheduler > run `.venv\Scripts\python.exe run.py` at logon. macOS: a launchd plist running the same command. Linux: a systemd user service with `ExecStart=/path/.venv/bin/python run.py`.
## Add a bot
Copy `Bots/ResearchBot.md` in the vault, edit the frontmatter (`schedule` is a cron string like `0 9 * * *`) and the prompt. Restart to load new schedules.
