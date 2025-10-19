# Insert Build Number (KiCad 9.0.5)
import pcbnew
import datetime
import re
import os

class InsertBuildNumber(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "BuildTracker (KiCad 9.0.5)"
        self.category = "Utility"
        self.description = "Insert or update build number with current date/time in KiCad 9.0.5"
        self.icon_file_name = os.path.join(os.path.dirname(__file__), "insert_build_number_icon.png")
        self.show_toolbar_button = True
        
    def Run(self):
        board = pcbnew.GetBoard()
        build_prefix = "Build "

        # Find existing Build text
        existing_build_texts = []
        for item in board.GetDrawings():
            if isinstance(item, pcbnew.PCB_TEXT):
                text = item.GetText()
                if text.startswith(build_prefix):
                    existing_build_texts.append(item)

        # Find the current maximum build number
        max_build_num = 0
        for item in existing_build_texts:
            match = re.match(r"Build (\d+)", item.GetText())
            if match:
                num = int(match.group(1))
                if num > max_build_num:
                    max_build_num = num

        new_build_num = max_build_num + 1

        # Current date and time
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M")

        # New text
        new_text = f"Build {new_build_num:03d} @ {timestamp}"

        # Overwrite or create new
        if existing_build_texts:
            # Overwrite the first one (if multiple exist)
            target = existing_build_texts[0]
            target.SetText(new_text)
        else:
            # Create new
            text = pcbnew.PCB_TEXT(board)
            text.SetText(new_text)
            text.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(10), pcbnew.FromMM(10)))
            text.SetLayer(pcbnew.F_SilkS)
            text.SetTextHeight(pcbnew.FromMM(1.0))
            text.SetTextWidth(pcbnew.FromMM(1.0))
            board.Add(text)

        pcbnew.Refresh()
        print(f"Inserted/updated: {new_text}")

InsertBuildNumber().register()
