# KiCad Python Plugin Collection

This repository contains a set of custom KiCad 9.0.4 plugins to automate common PCB tasks such as cleanup, backup, and metadata insertion. Each script is designed for easy operation and includes a toolbar button icon in the KiCad Application.

Why did I make this tool? Because deleting the existing tracks before running the auto-router was a hassle, so I made it possible to remove them all with a single click from an icon.


[English Version](README.md) | [日本語版](README-j.md)

## 📦 Plugin List

### 1. delete_track.py
Removes all track segments from the PCB.

- 🧹 Deletes only `PCB_TRACK` objects (not vias or zones)
- 🧪 Designed for use with KiCad 9.0.1
- Toolbar button included

### 2. delete_unlocked_track.py
Removes unlocked track segments from the PCB.

- 🧹 Deletes only unlocked `PCB_TRACK` objects
- Preserves locked tracks
- Toolbar button included

### 3. delete_all_tracks_and_vias.py
Removes both track segments and vias from the PCB.

- Deletes both `PCB_TRACK` and `PCB_VIA` objects
- Toolbar button included

### 4. insert_build_number.py
Inserts or updates a "Build Number" text on the PCB layout.

- Automatically increments build number (e.g., `Build 001`)
- Appends current date/time (e.g., `@ 2025-05-18 21:00`)
- Replaces existing text if found, otherwise adds new one
- Text added to front silkscreen layer at position (10mm, 10mm)

### 5. change_items_to_Fsilkscreen.py
Changes selected items to front silkscreen layer.

- Converts selected items to F.Silkscreen layer
- Useful for moving items between layers
- Toolbar button included

### 6 backup.py
Creates a ZIP archive backup of the current project with time stamp.

- ✅ Supports `.kicad_pro`, `.kicad_sch`, `.kicad_pcb`
- ✅ Includes custom footprints/symbols folders
- Excludes `.git` and previous backups
- Output saved in `backups/` folder under the project directory
- Then, open that backup directory with Finder to check the file.
  
## Installation

1. Open the plugins folder from the KiCAD application, Tools/Plugins folder, then copy all the python scripts and icons into the directory.  That's all.

Good luck!

[English Version](README.md) | [日本語版](README-j.md)
