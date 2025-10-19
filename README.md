# KiCad Plugin Collection

This repository contains a set of custom KiCad 9.0.5 plugins to automate common PCB tasks such as cleanup, backup, and metadata insertion. Each script is designed for easy operation and includes a toolbar button icon in the KiCad Application.

Why did I make this tool? Because deleting existing wiring before running the auto-router was troublesome, so I made it possible to quickly operate with features like bulk deletion with a single click from an icon.

[English Version](README.md) | [日本語版](README-j.md)

## 📦 Plugin List

### 1. delete_unlocked_tracks.py

Removes unlocked track segments from the PCB.

- 🧹 Deletes only unlocked `PCB_TRACK` objects
- Preserves locked tracks
- Toolbar button included

### 2. delete_all_tracks.py

Removes all track segments from the PCB (tracks only, no vias).

- Deletes all `PCB_TRACK` objects (including locked tracks)
- Preserves vias and zones
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

### 5. change_items_to_FSLK.py

Changes selected items to front silkscreen layer.

- Converts selected items to F.Silkscreen layer
- Useful for moving items between layers
- Toolbar button included

### 6. backup.py

Creates a ZIP archive backup of the current KiCad project.

- ✅ Supports `.kicad_pro`, `.kicad_sch`, `.kicad_pcb` files
- ✅ Includes custom footprint/symbol folders
- 🧹 Excludes `.git` and previous backups
- 📁 Output saved in `MyBackups/` folder under the project directory
  
## Installation

### Method 1: Manual Installation

1. Open the plugins folder from the KiCAD application, Tools/Plugins folder, then copy all the python scripts and icons into the directory.  That's all.

### Method 2: Automated Installation with Makefile

For easier installation and management, you can use the included Makefile:

```bash
# Install all plugins and icons
make install

# Remove all installed plugins and icons
make clean
```

**Features:**
- ✅ Automatically copies all `.py` and `.png` files to the correct KiCAD plugins directory
- ✅ Shows installation status with file timestamps
- ✅ Safe clean operation that only removes files from this project
- ✅ Uses portable paths (works on any system)

**Requirements:**
- Make utility (usually pre-installed on macOS/Linux)
- KiCAD 9.0.5 installed in the default location

Good luck!

[English Version](README.md) | [日本語版](README-j.md)
