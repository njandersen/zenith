import os 
os.add_dll_directory("C:\\Dev\\opencv\\install\\x64\\vc17\\bin")

import cv2
from managers import WindowManager, CaptureManager

class Zenith(object): 

    def __init__(self):
        self._windowManager = WindowManager('Zenith', self.onKeypress)
        self._captureManager = CaptureManager(
            cv2.VideoCapture(1), self._windowManager, True)
        
    def run(self):
        """Run the main loop."""
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame
        
            if frame is not None:
                # TODO: Filter the frame (Chapter 3).
                pass
        
            self._captureManager.exitFrame()
            self._windowManager.processEvents()

    def onKeypress(self, keycode):
        """Handle a keypress.
        
        space  -> Take a screenshot.
        tab    -> Start/stop recording a screencast.
        escape -> Quit.
        
        """
        if keycode == 32: # space
            self._captureManager.writeImage('screenshot.png')
        elif keycode == 9: # tab
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo(
                    'screencast.avi')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27: # escape
            self._windowManager.destroyWindow()

if __name__=="__main__":
    Zenith().run()