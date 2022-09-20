import sys
import PySide6.QtWidgets as QtWidgets
import PySide6.QtGui as QtGui
import time

slider_widget = None


class ExampleWindow(QtWidgets.QWidget):
    def __init__(self, window_name: str):
        super().__init__()

        self.window_name = window_name
        self.setGeometry(640, 480, 640, 480)
        self.setWindowTitle(self.window_name)
        self.layout = QtWidgets.QGridLayout()

        btn = QtWidgets.QPushButton('', self)
        btn.clicked.connect(self.save_files)
        self.layout.addWidget(btn, 1, 0)

        # lbl1 = QtWidgets.QLabel(text="Home Work 31", parent=self)
        # self.layout.addWidget(lbl1, 0, 0)

        slider = QtWidgets.QSlider(QtGui.Qt.Horizontal)
        self.layout.addWidget(slider, 2, 0)

        slider.setMinimum(1)
        slider.setMaximum(100)

        slider.setSingleStep(5)
        slider.valueChanged.connect(self.value_changed)

        global slider_widget
        slider_widget = slider

        self.setLayout(self.layout)

        self.show()

    def value_changed(self, i):
        print(i)

    @staticmethod
    def save_files(self):
        slider_value = 1
        global slider_widget
        if slider_widget is not None:
            slider_value = slider_widget.value()
        # print(slider_value)
        for i in range(slider_value):
            print(f"Файл №{i + 1} сохранен")
            file = open(f"tmp/file_{i + 1}.txt", 'w')
            file.write(f"File number {i + 1}")
            file.close()
            time.sleep(0.1)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = ExampleWindow('HomeWork 31')
    sys.exit(app.exec())

# id = -1
# name = 3
# surname = 3
# age = 4
# salary = 5
