import sys
from threading import Lock
from pynput.keyboard import Controller, Listener, Key
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QGroupBox, QRadioButton, QApplication

from config import Config


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.modes = Config.get_modes()

        self.setup_ui()

        self.macro_running = False

        self.config = Config.get_melon_pumpkin()

        self.keyboard = Controller()
        self.lock = Lock()
        self.holding_keys = []

    def setup_ui(self):
        self.setWindowTitle("Hypixel Farming Macro")
        self.resize(280, 150)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout()

        self.mode_group = QGroupBox("Select Mode:")
        self.mode_layout = QVBoxLayout()
        self.mode_radios = {}

        for i, label in enumerate(self.modes):
            mode_radio = QRadioButton(label)
            self.mode_layout.addWidget(mode_radio)
            self.mode_radios[label] = mode_radio

            if i == 0:
                mode_radio.setChecked(True)

        self.mode_group.setLayout(self.mode_layout)
        self.layout.addWidget(self.mode_group)

        self.toggle_button = QPushButton('Start', self)
        self.layout.addWidget(self.toggle_button)
        self.main_widget.setLayout(self.layout)

        self.toggle_button.clicked.connect(self.toggle_macro)

        self.show()

    def toggle_macro(self):
        if self.macro_running:
            self.macro_running = False
            self.toggle_button.setText('Start')
        else:
            self.macro_running = True
            self.toggle_button.setText('Stop')
            self.config = self.get_current_config()

    def setup_keypress_listener(self):
        '''
        Set up asynchronous listener to detect keypress events and send
        hold keys according to current config.
        '''

        def on_press(key: Key):

            if not self.macro_running or key not in [Key.left, Key.right, Key.up, Key.down, Key.shift_r]:
                return

            try:
                release_keys()

                if key == Key.left:
                    self.holding_keys = list(self.config.left)
                elif key == Key.right:
                    self.holding_keys = list(self.config.right)
                elif key == Key.up:
                    self.holding_keys = list(self.config.up)
                elif key == Key.down:
                    self.holding_keys = list(self.config.down)
                elif key == Key.shift_r:
                    self.holding_keys = []

                hold_keys()
                print("pressing")
            except Exception as e:
                print('error', e)

        def on_release(key):
            if key == Key.ctrl:
                self.key_modpfx = ''
            elif key == Key.cmd:
                self.key_modpfx = ''

        def hold_keys():
            with self.lock:
                for key in self.holding_keys:
                    self.keyboard.press(key)

        def release_keys():
            with self.lock:
                for key in self.holding_keys:
                    self.keyboard.release(key)
                self.holding_keys.clear()

        self.listener = Listener(
            on_press=on_press,
            on_release=on_release
        )
        self.listener.start()

    def get_current_config(self):
        label: str = [mode.text() for mode in self.mode_radios.values() if mode.isChecked()][0]
        config = Config.get_modes().get(label)()
        return config


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Main()
    main.setup_keypress_listener()
    sys.exit(app.exec_())

# https://github.com/moses-palmer/pynput/issues/511
