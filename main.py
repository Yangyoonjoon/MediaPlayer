from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QListWidgetItem
from PyQt5.uic import loadUi
import sys
from media import Media

class Form(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('form.ui', self)

        # 음악 재생기
        self.md = Media(self)

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
        self.lw.itemDoubleClicked.connect(self.OnDbClick)

    def secToHMS(self, pos):
        hour = pos//3600
        remain = pos%3600
        min = remain//60
        sec = remain%60

        sh = format(hour, '02')
        sm = format(min, '02')
        ss = format(sec, '02')

        return f'{sh}:{sm}:{ss}'

    def OnPosChanged(self, pos):
        if hasattr(self, 'pt'):
            self.sld.setValue(pos)
            pos = pos//1000

            t1 = self.secToHMS(pos)
            t2 = self.secToHMS(self.pt)

            self.label.setText(f'{t1} / {t2}')

    def OnMusicChanged(self, pt):
        self.sld.setRange(0, pt)
        self.pt = pt//1000

        row = self.md.getCurrentIdx()
        self.lw.setCurrentRow(row)

    def OnDbClick(self, item):
        row = self.lw.row(item)
        self.md.OnPlay(row)

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
        self.md.OnPlay(row+1)

    def OnPrev(self):
        row = self.lw.currentRow()
        if row == 0:
            row = self.lw.count()
        self.lw.setCurrentRow(row-1)
        self.md.OnPlay(row-1)

    def OnVol(self, vol):
        self.md.OnVol(vol)

    def closeEvent(self, e):
        cnt = self.lw.count()
        if cnt > 0:

            f = open('list.txt', 'w', encoding='utf-8')

            for i in range(cnt):
                item = self.lw.item(i)
                f.write(item.text() + '\n')

            f.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
