import os
import pcbnew

class MoveToSilk(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Move Selected to F.SilkS"
        self.category = "Modify"
        self.description = "Move selected objects to F.SilkS (9.0.4)"
        self.icon_file_name = os.path.join(os.path.dirname(__file__), "Change_items_to_Fsilkscreen.png")
        self.show_toolbar_button = True
        
    def Run(self):
        board = pcbnew.GetBoard()
        items = 0
        selection = pcbnew.GetCurrentSelection()
        for item in selection:
            try:
                items += 1
                item.SetLayer(pcbnew.F_SilkS)
            except AttributeError:
                pass
        pcbnew.Refresh()
        print(f"Chanegd {items} items.")

MoveToSilk().register()
