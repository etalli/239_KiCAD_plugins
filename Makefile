all:
	make install

check-os:
	@if [ "$$(uname)" != "Darwin" ]; then \
		echo "ERROR: This Makefile is designed for MacOS only."; \
		echo "Current OS: $$(uname)"; \
		echo "Please run this on MacOS or modify the paths for your operating system."; \
		exit 1; \
	fi

install: check-os
	@echo "=== Installing files... ==="
	@files_updated=0; \
	for file in scritps/*.py scritps/*.png; do \
		if [ -f "$$file" ]; then \
			dest_file="$(HOME)/Documents/KiCAD/9.0/scripting/plugins/$$(basename "$$file")"; \
			if [ ! -f "$$dest_file" ] || [ "$$file" -nt "$$dest_file" ]; then \
				cp "$$file" "$$dest_file"; \
				files_updated=1; \
			fi; \
		fi; \
	done; \
	if [ $$files_updated -eq 0 ]; then \
		echo "No files were updated - all files are already up to date."; \
	else \
		echo "Files have been updated successfully."; \
		echo "=== File modification times (minutes ago) ==="; \
		find $(HOME)/Documents/KiCAD/9.0/scripting/plugins/ -name "*.py" -o -name "*.png" | sort | while read file; do \
			if [ -f "$$file" ]; then \
				current_time=$$(date +%s); \
				file_time=$$(date -r "$$file" +%s); \
				diff_seconds=$$(expr $$current_time - $$file_time); \
				minutes_ago=$$(expr $$diff_seconds / 60); \
				echo "$$minutes_ago minutes ago: $$(basename "$$file")"; \
			fi; \
		done; \
	fi

clean: check-os
	rm -f $(HOME)/Documents/KiCAD/9.0/scripting/plugins/backup.py
	rm -f $(HOME)/Documents/KiCAD/9.0/scripting/plugins/1_delete_unlocked_tracks.py
	rm -f $(HOME)/Documents/KiCAD/9.0/scripting/plugins/2_delete_all_tracks.py
	rm -f $(HOME)/Documents/KiCAD/9.0/scripting/plugins/3_delete_all_tracks_and_vias.py
	rm -f $(HOME)/Documents/KiCAD/9.0/scripting/plugins/insert_build_number.py
	rm -f $(HOME)/Documents/KiCAD/9.0/scripting/plugins/backup_icon.png
	rm -f $(HOME)/Documents/KiCAD/9.0/scripting/plugins/change_items_to_FSLK.png
	rm -f $(HOME)/Documents/KiCAD/9.0/scripting/plugins/delete_all_tracks_icon.png
	rm -f $(HOME)/Documents/KiCAD/9.0/scripting/plugins/delete_all_tracks_and_vias_icon.png
	rm -f $(HOME)/Documents/KiCAD/9.0/scripting/plugins/delete_unlocked_tracks_icon.png
	rm -f $(HOME)/Documents/KiCAD/9.0/scripting/plugins/insert_build_number_icon.png

clean-all: check-os
	@echo "=== Removing all files... ==="
	rm -rf $(HOME)/Documents/KiCAD/9.0/scripting/plugins/*
	@echo "=== Cleanup completed ==="

