install:
	cp scritps/*.py scritps/*.png $(HOME)/Documents/KiCAD/9.0/scripting/plugins/
	@echo "=== ファイルの更新時刻（何分前） ==="
	@find $(HOME)/Documents/KiCAD/9.0/scripting/plugins/ -name "*.py" -o -name "*.png" | while read file; do \
		if [ -f "$$file" ]; then \
			current_time=$$(date +%s); \
			file_time=$$(date -r "$$file" +%s); \
			diff_seconds=$$(expr $$current_time - $$file_time); \
			minutes_ago=$$(expr $$diff_seconds / 60); \
			echo "$$minutes_ago 分前: $$(basename "$$file")"; \
		fi; \
	done

clean:
	rm -f $(HOME)/Documents/KiCAD/9.0/scripting/plugins/backup.py
	rm -f $(HOME)/Documents/KiCAD/9.0/scripting/plugins/change_items_to_FSLK.py
	rm -f $(HOME)/Documents/KiCAD/9.0/scripting/plugins/delete_all_tracks.py
	rm -f $(HOME)/Documents/KiCAD/9.0/scripting/plugins/delete_all_tracks_and_vias.py
	rm -f $(HOME)/Documents/KiCAD/9.0/scripting/plugins/delete_unlocked_tracks.py
	rm -f $(HOME)/Documents/KiCAD/9.0/scripting/plugins/insert_build_number.py
	rm -f $(HOME)/Documents/KiCAD/9.0/scripting/plugins/backup_icon.png
	rm -f $(HOME)/Documents/KiCAD/9.0/scripting/plugins/change_items_to_FSLK.png
	rm -f $(HOME)/Documents/KiCAD/9.0/scripting/plugins/delete_all_tracks_icon.png
	rm -f $(HOME)/Documents/KiCAD/9.0/scripting/plugins/delete_all_tracks_and_vias_icon.png
	rm -f $(HOME)/Documents/KiCAD/9.0/scripting/plugins/delete_unlocked_tracks_icon.png
	rm -f $(HOME)/Documents/KiCAD/9.0/scripting/plugins/insert_build_number_icon.png

