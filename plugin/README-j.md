# KiCad PCM リポジトリ例

このフォルダには、**プラグイン & コンテンツマネージャー (PCM)** を通じてKiCad Pythonプラグインを配布するための最小限の動作するスキャフォールドが含まれています。

## ファイル

- `repository.json` — ユーザーに提供するインデックスファイル（設定 → プラグインとコンテンツリポジトリの管理…）。
  - 2つのプレースホルダーURLを、`packages.json`と`resources.zip`をホストする場所に変更してください。
- `packages.json` — パッケージの一覧。現在は1つのプラグインをリストし、`download_url`を指しています（プラグインzipをホストし、URLを更新する必要があります）。
- `resources.zip` — パッケージから参照されるアイコン（ここでは：`icons/myplugin.png`）。
- `myplugin-1.0.0.zip` — 有効なプラグインアーカイブ（`plugins/`、`resources/`、`metadata.json`を含む）。これをGitHub Releases（または任意の静的ホスト）にアップロードし、そのURLを`packages.json` → `versions[0].download_url`にコピーしてください。

## 公開方法

1. **`myplugin-1.0.0.zip`** をどこか公開場所（例：GitHub Releases）にアップロードします。
2. SHA256とサイズを計算し、**`packages.json`** をそれに応じて更新します（ローカルファイル用に既に記入済み；再ビルド後にアップロードした場合は再計算）。
3. **`packages.json`** と **`resources.zip`** をホストし（例：GitHub Pages）、**`repository.json`** のプレースホルダーURLを置き換えます。
4. **`repository.json`** URLをユーザーと共有します。ユーザーはKiCad → 設定 → プラグインとコンテンツリポジトリの管理…で追加します。

## 注意事項

- プラグインアーカイブの構造は正確に以下の通りである必要があります：
  ```
  アーカイブルート
  ├─ plugins/
  │   ├─ __init__.py
  │   └─ myplugin_action.py
  ├─ resources/
  │   └─ icon.png   (64x64、オプション)
  └─ metadata.json
  ```
- プラグイン内の`metadata.json`には`download_*`フィールドを**含めてはいけません**。これらはリポジトリメタデータ（`packages.json`）にあります。

