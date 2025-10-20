# KiCad PCM Repo Example

This folder contains a minimal, working scaffold for distributing a KiCad Python plugin via the **Plugin & Content Manager (PCM)**.

## Files

- `repository.json` — The index file you give to users (Preferences → Manage Plugin and Content Repositories…).
  - Change the two placeholder URLs to where you will host `packages.json` and `resources.zip`.
- `packages.json` — Lists your packages. It currently lists one plugin and points to `download_url` (you must host the plugin zip and update the URL).
- `resources.zip` — Icons referenced from packages (here: `icons/myplugin.png`).
- `myplugin-1.0.0.zip` — A valid plugin archive (contains `plugins/`, `resources/`, `metadata.json`). You should upload this to GitHub Releases (or any static host) and copy its URL into `packages.json` → `versions[0].download_url`.

## How to publish

1. Upload **`myplugin-1.0.0.zip`** somewhere public (e.g., GitHub Releases).
2. Compute its SHA256 and size and update **`packages.json`** accordingly (already filled here for the local file; recalc after you upload if you rebuild).
3. Host **`packages.json`** and **`resources.zip`** (e.g., GitHub Pages) and replace the placeholder URLs in **`repository.json`**.
4. Share the **`repository.json`** URL with users. They add it in KiCad → Preferences → Manage Plugin and Content Repositories….

## Notes

- Plugin archive structure must be exactly:
  ```
  Archive root
  ├─ plugins/
  │   ├─ __init__.py
  │   └─ myplugin_action.py
  ├─ resources/
  │   └─ icon.png   (64x64, optional)
  └─ metadata.json
  ```
- The `metadata.json` inside the plugin **must not** include `download_*` fields. Those live in the repository metadata (`packages.json`).

