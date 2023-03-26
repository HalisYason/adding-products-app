

import sys

from PyQt5.QtWidgets import *
from mainpage import mainPage


app = QApplication(sys.argv)

pencere = mainPage()
pencere.show()

sys.exit(app.exec_())






