from flask import Flask, render_template_string, jsonify
from datetime import datetime
import random

app = Flask(__name__)

TEMPLATE = """<!DOCTYPE html> <!-- El HTML va aquí (omitido para brevedad) --> """
# Reemplaza TEMPLATE por el completo en la práctica

# Datos simulados
inventario = [
    {"Producto": "A", "Stock": 10, "Precio": 5.0, "Ultima Actualización": "2025-07-21"},
    {"Producto": "B", "Stock": 20, "Precio": 8.5, "Ultima Actualización": "2025-07-21"}
]
ventas_diarias = [{"fecha": f"2025-07-{i+1:02}", "total": random.randint(5, 20)} for i in range(15)]
detalle_ventas = {
    f"2025-07-{i+1:02}": [{"producto": "A", "cantidad": random.randint(1, 10)},
                          {"producto": "B", "cantidad": random.randint(1, 10)}]
    for i in range(15)
}

@app.route("/")
def home():
    return render_template_string(TEMPLATE, inventario=inventario)

@app.route("/data")
def data():
    return jsonify({
        "inventario": inventario,
        "ventas_diarias": ventas_diarias
    })

@app.route("/detalle/<fecha>")
def detalle(fecha):
    return jsonify(detalle_ventas.get(fecha, []))

if __name__ == "__main__":
    app.run(debug=True)
