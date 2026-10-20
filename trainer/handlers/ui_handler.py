from __future__ import annotations

import sys

from trainer.bootstrap import TrainerContext
from trainer.services import cheat_service


def run(ctx: TrainerContext) -> int:
    try:
        from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
    except ImportError:
        print("PySide6 missing; install requirements.txt", file=sys.stderr)
        return 1

    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setWindowTitle("Fart Togethe Trainer")

    central = QWidget()
    layout = QVBoxLayout(central)

    svc = cheat_service.CheatService(ctx)

    btn_inf = QPushButton("Infinite Fart Meter")
    btn_inf.clicked.connect(svc.toggle_infinite_fart)
    layout.addWidget(btn_inf)

    btn_speed = QPushButton("Fart Speed x3")
    btn_speed.clicked.connect(svc.toggle_fart_speed)
    layout.addWidget(btn_speed)

    btn_ghost = QPushButton("Ghost Fart (no sound)")
    btn_ghost.clicked.connect(svc.toggle_ghost_fart)
    layout.addWidget(btn_ghost)

    win.setCentralWidget(central)
    win.resize(320, 240)
    win.show()
    return app.exec()