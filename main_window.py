from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog)
from data.loader import load_data
from visualization.plot_2d import plot_pressure
from visualization.plot_3d import create_3d_plot

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Drilling Data Viewer")
        self.setGeometry(100, 100, 800, 500)

        # Widget principal
        central_widget = QWidget()

        self.setCentralWidget(central_widget)

        # Layout principal (horizontal)
        main_layout = QHBoxLayout()

        central_widget.setLayout(main_layout)

        # . Menu lateral
        sidebar = QVBoxLayout()

        title = QLabel("Menu")
        sidebar.addWidget(title)

        btn_load = QPushButton("Abrir CSV")

        btn_load.clicked.connect(self.load_and_plot)
        sidebar.addWidget(btn_load)

        btn_3d = QPushButton("Visualizar 3D")
        btn_3d.clicked.connect(self.safe_3d)
        sidebar.addWidget(btn_3d)

        sidebar.addStretch()

        # . Área principal
        content = QVBoxLayout()

        self.label = QLabel("Pronto para carregar dados")
        content.addWidget(self.label)

        # Adicionando no layout principal
        main_layout.addLayout(sidebar, 1)
        main_layout.addLayout(content, 3)

    def load_and_plot(self):
        file, _ =  QFileDialog.getOpenFileName(self, "Abrir CSV", "", "CSV Files (*.csv)")

        if file:
            df = load_data(file)
            plot_pressure(df)
            self.label.setText(f"Arquivo carregado:\n{file}")

    def safe_3d(self):
        try:
            self.label.setText("Tentando abrir visualização 3D...")
            create_3d_plot()
        except Exception as e:
            self.label.setText("Erro ao abrir 3D.\nProblema com OpenGL")
            print(e)