from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog
from PyQt5.uic import loadUi
import sys
from media import Media

class Form(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('form.ui', self)

        # 음악 재생기
        self.md = Media()

        self.dial.setValue(50)
        self.dial.setRange(0, 100)

        # 시그널
        self.dial.valueChanged.connect(self.OnVol)
        self.btn_add.clicked.connect(self.OnAdd)
        self.btn_del.clicked.connect(self.OnDel)
        self.btn_play.clicked.connect(self.OnPlay)
        self.btn_stop.clicked.connect(self.OnStop)
        self.btn_pause.clicked.connect(self.OnPause)
        self.btn_prev.clicked.connect(self.OnPrev)
        self.btn_ff.clicked.connect(self.OnFF)

    def OnAdd(self):
        result = QFileDialog.getOpenFileNames(self, '음악추가', '', '음악파일 (*.wav *.mp3 *.ogg *.flac)')
        
        if result[0]:
            self.lw.addItems(result[0])
            self.md.addMedia(result[0])

    def OnDel(self):
        row = self.lw.currentRow()
        self.lw.takeItem(row)
        self.md.delMedia(row)

    def OnPlay(self):
        row = self.lw.currentRow()
        self.md.OnPlay(row)

    def OnStop(self):
        self.md.OnStop()

    def OnPause(self):
        self.md.OnPause()

    def OnFF(self):
        row = self.lw.currentRow()
        if row == self.lw.count()-1:
            row = -1
        self.lw.setCurrentRow(row+1)

    def OnPrev(self):
        row = self.lw.currentRow()
        if row == 0:
            row = self.lw.count()
        self.lw.setCurrentRow(row-1)

    def OnVol(self, vol):
        self.md.OnVol(vol)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
