# Delete Unlocked Tracks (KiCad 9.0.5)
import pcbnew
import os

class DeleteAllTracks(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Delete All Tracks (Skip Locked) (KiCad 9.0.5"
        self.category = "Cleanup"
        self.description = "Delete all unlocked tracks from the PCB in KiCad 9.0.5"
        self.icon_file_name = os.path.join(os.path.dirname(__file__), "delete_unlocked_tracks_icon.png")
        self.show_toolbar_button = True

    def Run(self):
        board = pcbnew.GetBoard()
        track_list = list(board.GetTracks())
        deleted = 0
        skipped = 0

        for item in track_list:
            if isinstance(item, pcbnew.PCB_TRACK):  # Only process tracks
                if item.IsLocked():
                    skipped += 1
                    continue
                board.Remove(item)
                deleted += 1

        pcbnew.Refresh()
        print(f"Deleted {deleted} tracks. Skipped {skipped} locked tracks.")

DeleteAllTracks().register()
