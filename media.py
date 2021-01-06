from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent
from PyQt5.QtCore import QUrl

class Media:
    def __init__(self):
        self.player = QMediaPlayer()
        self.list = QMediaPlaylist()

        self.player.setPlaylist(self.list)

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