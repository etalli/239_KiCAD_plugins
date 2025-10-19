import pcbnew
import os

class DeleteTracksAndVias(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Delete Tracks and Vias (KiCad 9.0.5)"
        self.category = "Cleanup"
        self.description = "Delete all tracks and vias from the PCB in KiCad 9.0.5"
        self.icon_file_name = os.path.join(os.path.dirname(__file__), "delete_all_tracks_and_vias_icon.png")
        self.show_toolbar_button = True
        
    def Run(self):
        board = pcbnew.GetBoard()
        track_list = list(board.GetTracks())
        deleted = 0

        for item in track_list:
            if type(item).__name__ in ["PCB_TRACK", "PCB_VIA"]:
                board.Remove(item)
                deleted += 1

        pcbnew.Refresh()
        print(f"Deleted {deleted} items (tracks + vias).")

DeleteTracksAndVias().register()
