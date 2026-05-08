import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent
DATOS_DIR = BASE_DIR / "datos"
RESULTADOS_DIR = BASE_DIR / "resultados"


class SimuladorPuertas:
    """
    Simulador basico de puertas logicas.
    Se trabajan las operaciones AND, OR y XOR porque permiten mostrar
    de forma simple como cambia una salida segun dos entradas binarias.
    """

    def and_logico(self, a, b):
        return a & b

    def or_logico(self, a, b):
        return a | b

    def xor_logico(self, a, b):
        return a ^ b

    def generar_tabla_verdad(self):
        tabla = []

        # Se recorren las cuatro combinaciones posibles para dos entradas binarias.
        for a in [0, 1]:
            for b in [0, 1]:
                tabla.append({
                    "A": a,
                    "B": b,
                    "AND": self.and_logico(a, b),
                    "OR": self.or_logico(a, b),
                    "XOR": self.xor_logico(a, b)
                })

        return pd.DataFrame(tabla)

    def exportar_tabla(self):
        RESULTADOS_DIR.mkdir(exist_ok=True)
        tabla = self.generar_tabla_verdad()
        tabla.to_csv(RESULTADOS_DIR / "tabla_verdad.csv", index=False)
        print("Tabla de verdad exportada correctamente.")

    def procesar_archivo(self):
        RESULTADOS_DIR.mkdir(exist_ok=True)
        ruta = DATOS_DIR / "entradas.csv"

        try:
            datos = pd.read_csv(ruta)
        except FileNotFoundError:
            print("No se encontro el archivo datos/entradas.csv")
            return

        columnas_necesarias = {"A", "B"}
        if not columnas_necesarias.issubset(datos.columns):
            print("El archivo debe tener las columnas A y B.")
            return

        resultados = []

        for _, fila in datos.iterrows():
            a = int(fila["A"])
            b = int(fila["B"])

            resultados.append({
                "A": a,
                "B": b,
                "AND": self.and_logico(a, b),
                "OR": self.or_logico(a, b),
                "XOR": self.xor_logico(a, b)
            })

        resultados_df = pd.DataFrame(resultados)
        resultados_df.to_csv(RESULTADOS_DIR / "resultados_lote.csv", index=False)

        totales = {
            "AND": int(resultados_df["AND"].sum()),
            "OR": int(resultados_df["OR"].sum()),
            "XOR": int(resultados_df["XOR"].sum())
        }

        self.generar_reporte(resultados_df, totales)
        self.generar_grafico(totales)

        print("Procesamiento finalizado correctamente.")

    def generar_reporte(self, resultados_df, totales):
        # El reporte se deja en texto simple para que pueda revisarse sin abrir programas adicionales.
        with open(RESULTADOS_DIR / "reporte.txt", "w", encoding="utf-8") as archivo:
            archivo.write("REPORTE DEL ANALISIS\n")
            archivo.write("----------------------------\n")
            archivo.write(f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
            archivo.write(f"Total de registros procesados: {len(resultados_df)}\n")
            archivo.write(f"Cantidad de AND = 1: {totales['AND']}\n")
            archivo.write(f"Cantidad de OR = 1: {totales['OR']}\n")
            archivo.write(f"Cantidad de XOR = 1: {totales['XOR']}\n")

    def generar_grafico(self, totales):
        operaciones = list(totales.keys())
        cantidades = list(totales.values())

        plt.figure(figsize=(6, 4))
        plt.bar(operaciones, cantidades)
        plt.title("Cantidad de resultados positivos")
        plt.xlabel("Puertas logicas")
        plt.ylabel("Cantidad")
        plt.tight_layout()
        plt.savefig(RESULTADOS_DIR / "grafico_resultados.png")
        plt.close()


def menu():
    simulador = SimuladorPuertas()

    while True:
        print("\n===== SIMULADOR DE PUERTAS LOGICAS =====")
        print("1 - Mostrar tabla de verdad")
        print("2 - Exportar tabla CSV")
        print("3 - Procesar archivo CSV")
        print("4 - Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            print(simulador.generar_tabla_verdad())
        elif opcion == "2":
            simulador.exportar_tabla()
        elif opcion == "3":
            simulador.procesar_archivo()
        elif opcion == "4":
            print("Programa finalizado.")
            break
        else:
            print("Opcion invalida.")


if __name__ == "__main__":
    menu()
