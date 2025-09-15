import pcbnew
import os
import zipfile
from datetime import datetime
import subprocess

class BackupProject(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Backup Project to ZIP manually (KiCad 9.0.4)"
        self.category = "Project Tools"
        self.description = "Create a zip backup of the current project with timestamp"
        self.icon_file_name = os.path.join(os.path.dirname(__file__), "backup_icon.png")
        self.show_toolbar_button = True

    def Run(self):
        board = pcbnew.GetBoard()
        project_path = board.GetFileName()

        if not project_path:
            print("Error: Project path is empty.")
            return

        project_dir = os.path.dirname(project_path)
        project_name = os.path.splitext(os.path.basename(project_path))[0]

        now = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"{project_name}_{now}.zip"
        backup_dir = os.path.join(project_dir, "backups")
        os.makedirs(backup_dir, exist_ok=True)
        backup_full_path = os.path.join(backup_dir, backup_filename)

        print(f"Backing up to: {backup_full_path}")

        try:
            with zipfile.ZipFile(backup_full_path, "w", zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(project_dir):
                    # 除外対象
                    rel_root = os.path.relpath(root, project_dir)
                    if rel_root.startswith(".git") or rel_root.startswith("backups"):
                        continue

                    for file in files:
                        full_path = os.path.join(root, file)
                        rel_path = os.path.relpath(full_path, project_dir)

                        # .kicad_* や _symbols/_footprints の全ファイルを含める
                        if (
                            file.endswith((".kicad_pro", ".kicad_sch", ".kicad_pcb"))
                            or "_symbols" in rel_path
                            or "_footprints" in rel_path
                        ):
                            try:
                                zipf.write(full_path, arcname=rel_path)
                                print(f"Added: {rel_path}")
                            except Exception as e:
                                print(f"Failed to add {rel_path}: {e}")

        except Exception as e:
            print(f"Backup failed: {e}")
            return

        print("Backup complete.")
        # Open the backup directory in Finder on macOS
        try:
            subprocess.run(["open", backup_dir], check=False)
        except Exception as e:
            print(f"Failed to open Finder: {e}")
        pcbnew.Refresh()

BackupProject().register()
