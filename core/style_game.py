# --- Light theme ---
LIGHT_THEME = """
QWidget {
    background-color: #f8fafc;
    color: #000000;
    font-family: 'Segoe UI', system-ui, sans-serif;
}
QLabel#title { font-size: 20px; font-weight: 700; color: #1e293b; }
QLabel#undercores { font-size: 28px; font-weight: 800; color: #0d9488; letter-spacing: 6px; }
QLabel#incorrect { font-size: 13px; color: #64748b; }
QLabel#lives { font-size: 15px; color: #e11d48; font-weight: 600; }

QLineEdit#input {
    border: 2px solid #cbd5e1;
    border-radius: 8px;
    padding: 4px 10px;
    background-color: #ffffff;
    color: #0f172a;
}
QLineEdit#input:focus { border-color: #0d9488; }

QPushButton {
    background-color: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    color: #334155;
    font-weight: 600;
}
QPushButton:hover { background-color: #f1f5f9; }

QPushButton#toggle_button {
    padding: 4px 12px;
    font-size: 11px;
    background-color: #e2e8f0;
    border: none;
    color: #475569;
}

"""

# ---Dark theme ---
DARK_THEME = """
QWidget {
    background-color: #0f172a;
    color: #f8fafc;
    font-family: 'Segoe UI', system-ui, sans-serif;
}
QLabel#title { font-size: 20px; font-weight: 700; color: #f8fafc; }
QLabel#undercores { font-size: 28px; font-weight: 800; color: #2dd4bf; letter-spacing: 6px; }
QLabel#incorrect { font-size: 13px; color: #94a3b8; }
QLabel#lives { font-size: 15px; color: #fb7185; font-weight: 600; }

QLineEdit#input {
    border: 2px solid #334155;
    border-radius: 8px;
    padding: 4px 10px;
    background-color: #1e293b;
    color: #f8fafc;
}
QLineEdit#input:focus { border-color: #2dd4bf; }

QPushButton {
    background-color: #1e293b;
    border: 1px solid #334155;
    border-radius: 6px;
    color: #f8fafc;
    font-weight: 600;
}
QPushButton:hover { background-color: #334155; }

QPushButton#toggle_button {
    padding: 4px 12px;
    font-size: 11px;
    background-color: #334155;
    border: none;
    color: #f8fafc;
}
"""