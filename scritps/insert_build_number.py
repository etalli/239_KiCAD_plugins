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

        # 既存のBuildテキストを探す
        existing_build_texts = []
        for item in board.GetDrawings():
            if isinstance(item, pcbnew.PCB_TEXT):
                text = item.GetText()
                if text.startswith(build_prefix):
                    existing_build_texts.append(item)

        # 現在の最大ビルド番号を調べる
        max_build_num = 0
        for item in existing_build_texts:
            match = re.match(r"Build (\d+)", item.GetText())
            if match:
                num = int(match.group(1))
                if num > max_build_num:
                    max_build_num = num

        new_build_num = max_build_num + 1

        # 現在の日時
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M")

        # 新しいテキスト
        new_text = f"Build {new_build_num:03d} @ {timestamp}"

        # 上書きまたは新規追加
        if existing_build_texts:
            # 最初のものに上書き（複数ある場合）
            target = existing_build_texts[0]
            target.SetText(new_text)
        else:
            # 新規作成
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
