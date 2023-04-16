from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QAction, QMessageBox
from PyQt5.QtCore import Qt

class DoStock(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configurar la ventana principal
        self.setWindowTitle('DoStock v0.1')
        self.setGeometry(100, 100, 600, 400)

        # Crear el widget central y el diseño vertical
        widget_central = QWidget()
        layout_principal = QVBoxLayout()
        widget_central.setLayout(layout_principal)

        # Crear la tabla para mostrar los productos
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Producto', 'Piezas', 'Costo'])
        layout_principal.addWidget(self.table)

        # Crear el widget de entrada de datos y el diseño horizontal
        widget_entrada = QWidget()
        layout_entrada = QHBoxLayout()
        widget_entrada.setLayout(layout_entrada)

        # Crear los campos de entrada de texto
        self.input_producto = QLineEdit()
        self.input_piezas = QLineEdit()
        self.input_costo = QLineEdit()
        layout_entrada.addWidget(QLabel('Producto:'))
        layout_entrada.addWidget(self.input_producto)
        layout_entrada.addWidget(QLabel('Piezas:'))
        layout_entrada.addWidget(self.input_piezas)
        layout_entrada.addWidget(QLabel('Costo:'))
        layout_entrada.addWidget(self.input_costo)

        # Crear el botón de agregar producto
        btn_agregar = QPushButton('Agregar')
        btn_agregar.clicked.connect(self.agregar_producto)
        layout_entrada.addWidget(btn_agregar)

        # Agregar el widget de entrada de datos al diseño principal
        layout_principal.addWidget(widget_entrada)

        # Crear la etiqueta para mostrar el costo total
        self.label_total_costo = QLabel('Costo total: $0.00')
        layout_principal.addWidget(self.label_total_costo)

        # Crear la acción de archivo y la barra de menú
        accion_agregar = QAction('Agregar producto', self)
        accion_agregar.setShortcut('Ctrl+A')
        accion_agregar.triggered.connect(self.agregar_producto)
        accion_borrar = QAction('Borrar producto', self)
        accion_borrar.setShortcut('Ctrl+B')
        accion_borrar.triggered.connect(self.borrar_producto)
        self.menu_archivo = self.menuBar().addMenu('Archivo')
        self.menu_archivo.addAction(accion_agregar)
        self.menu_archivo.addAction(accion_borrar)

        # Configurar la ventana principal
        self.setCentralWidget(widget_central)

    def agregar_producto(self):
        # Obtener los datos del producto desde los campos de entrada de texto
        producto = self.input_producto.text()
        piezas = self.input_piezas.text()
        costo = self.input_costo.text()

        # Verificar si los campos están vacíos
        if producto == '' or piezas == '' or costo == '':
            QMessageBox.warning(self, 'Campos vacíos', 'Por favor, completa todos los campos.')
            return

         # Agregar una nueva fila a la tabla
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)
        self.table.setItem(row_count, 0, QTableWidgetItem(producto))
        self.table.setItem(row_count, 1, QTableWidgetItem(piezas))
        self.table.setItem(row_count, 2, QTableWidgetItem(costo))

        # Actualizar el costo total
        self.actualizar_total_costo()

        # Limpiar los campos de entrada de texto
        self.input_producto.clear()
        self.input_piezas.clear()
        self.input_costo.clear()

    def borrar_producto(self):
        # Obtener la fila seleccionada en la tabla
        row = self.table.currentRow()

        # Verificar si hay una fila seleccionada
        if row == -1:
            QMessageBox.warning(self, 'Producto no seleccionado', 'Por favor, selecciona un producto de la tabla.')
            return

        # Eliminar la fila de la tabla
        self.table.removeRow(row)

        # Actualizar el costo total
        self.actualizar_total_costo()

    def actualizar_total_costo(self):
        # Calcular el costo total sumando los costos de todos los productos en la tabla
        total_costo = 0.0
        for row in range(self.table.rowCount()):
            piezas = self.table.item(row, 1)
            costo = self.table.item(row, 2)
            if piezas is not None and costo is not None:
                total_costo += float(piezas.text()) * float(costo.text())

        # Actualizar la etiqueta con el costo total
        self.label_total_costo.setText(f'Costo total: ${total_costo:.2f}')



if __name__ == '__main__':
    app = QApplication([])
    ventana = DoStock()
    ventana.show()
    app.exec_()
