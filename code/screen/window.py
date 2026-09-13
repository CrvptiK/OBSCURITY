import pygame
import ctypes

user32 = ctypes.windll.user32

GWL_EXSTYLE = -20
WS_EX_LAYERED = 0x80000
WS_EX_TRANSPARENT = 0x20
WS_EX_TOPMOST = 0x00000008


class OverlayWindow:
    def __init__(self, width=1920, height=1080):
        pygame.init()

        # Borderless
        self.screen = pygame.display.set_mode(
            (width, height),
            pygame.NOFRAME
        )

        pygame.display.set_caption("Overlay")

        # windows handle
        self.hwnd = pygame.display.get_wm_info()["window"]

        self._make_window_layered()
        self.set_topmost(True)
        self.set_clickthrough(True)

        # transparency
        self.colorkey = (255, 0, 255)  # magenta = transparent
        self.screen.fill(self.colorkey)
        self.screen.set_colorkey(self.colorkey)


    # Win32 setup
    def _make_window_layered(self):
        style = user32.GetWindowLongW(self.hwnd, GWL_EXSTYLE)
        style |= WS_EX_LAYERED
        user32.SetWindowLongW(self.hwnd, GWL_EXSTYLE, style)

    def set_clickthrough(self, enabled: bool):
        style = user32.GetWindowLongW(self.hwnd, GWL_EXSTYLE)

        if enabled:
            style |= WS_EX_TRANSPARENT
        else:
            style &= ~WS_EX_TRANSPARENT

        user32.SetWindowLongW(self.hwnd, GWL_EXSTYLE, style)

    def set_topmost(self, enabled: bool):
        HWND_TOPMOST = -1
        HWND_NOTOPMOST = -2

        user32.SetWindowPos(
            self.hwnd,
            HWND_TOPMOST if enabled else HWND_NOTOPMOST,
            0, 0, 0, 0,
            0x0001 | 0x0002  # SWP_NOMOVE | SWP_NOSIZE
        )

    # rendering
    def clear(self):
        self.screen.fill(self.colorkey)

    def update(self):
        pygame.display.update()
