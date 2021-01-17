from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent
from PyQt5.QtCore import QUrl, QObject, pyqtSignal

class Media(QObject):

    mc_signal = pyqtSignal(int)
    pos_signal = pyqtSignal(int)

    def __init__(self, w):
        super().__init__()
        self.parent = w
        self.player = QMediaPlayer()
        self.list = QMediaPlaylist()

        self.player.setPlaylist(self.list)

        # 시그널
        self.player.durationChanged.connect(self.OnMusicChanged)
        self.player.positionChanged.connect(self.OnPosChanged)

        # 사용자 시그널
        self.mc_signal.connect(self.parent.OnMusicChanged)
        self.pos_signal.connect(self.parent.OnPosChanged)

    def OnPosChanged(self, pos):
        self.pos_signal.emit(pos)

    def OnMusicChanged(self, pt):
        self.mc_signal.emit(pt)

    def addMedia(self, files):
        for f in files:
            url = QUrl(f)
            self.list.addMedia(QMediaContent(url))

    def delMedia(self, idx):
        self.list.removeMedia(idx)

    def OnPlay(self, idx):
        self.list.setCurrentIndex(idx)
        self.player.play()

    def OnStop(self):
        self.player.stop()

    def OnPause(self):
        self.player.pause()

    def OnVol(self, vol):
        self.player.setVolume(vol)

    def getCurrentIdx(self):
        return self.list.currentIndex()