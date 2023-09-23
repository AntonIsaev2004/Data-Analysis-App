import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import pandas as pd

# Создание базы данных Pandas
df = pd.read_excel('df.xlsx')

# Создание модели данных
model = QStandardItemModel(df.shape[0], df.shape[1])
model.setHorizontalHeaderLabels(df.columns)

# Заполнение модели данными из базы данных Pandas
for row in range(df.shape[0]):
    for column in range(df.shape[1]):
        item = QStandardItem(str(df.iloc[row, column]))
        model.setItem(row, column, item)

# Создание приложения PyQt5
app = QApplication(sys.argv)

# Создание главного окна
window = QMainWindow()
window.setWindowTitle("База данных")

# Создание виджета QTabWidget
tab_widget = QTabWidget()
window.setCentralWidget(tab_widget)

# Создание виджета QTableView и добавление его в QTabWidget
table_view = QTableView()
table_view.setModel(model)
tab_widget.addTab(table_view, "База данных")

# Отображение главного окна
window.show()

# Запуск главного цикла приложения
sys.exit(app.exec_())