# Simulador de Puertas Logicas

Proyecto desarrollado para la materia **Organizacion Empresarial** de la Tecnicatura Universitaria en Programacion - UTN.

La idea del trabajo fue armar un proyecto chico pero ordenado, donde se pueda ver el uso de Git, GitHub, Jira y una implementacion tecnica en Python. Para no hacerlo innecesariamente complejo, se eligio trabajar con puertas logicas basicas, ya que permiten mostrar entradas, procesamiento y resultados de forma clara.

## Funcionalidades

El programa permite:

- generar una tabla de verdad con operaciones AND, OR y XOR;
- procesar un archivo CSV con entradas binarias;
- guardar los resultados en la carpeta `resultados`;
- generar un reporte textual;
- crear un grafico comparativo con la cantidad de salidas positivas.

## Tecnologias utilizadas

- Python 3
- Pandas
- Matplotlib
- Git
- GitHub
- Jira

## Estructura del repositorio

```txt
repo-proyecto/
├── datos/
│   └── entradas.csv
├── scripts/
│   └── simulador_puertas.py
├── resultados/
│   ├── resultados_lote.csv
│   ├── reporte.txt
│   └── grafico_resultados.png
├── documentacion/
├── README.md
├── requirements.txt
└── .gitignore
```

## Ejecucion

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar el programa:

```bash
python scripts/simulador_puertas.py
```

Al ejecutar el programa se muestra un menu con opciones para generar la tabla de verdad, exportar resultados o procesar el archivo de datos.

## Flujo de trabajo propuesto

El trabajo se organizo en tareas vinculadas a Jira. Cada commit debe comenzar con el codigo del issue correspondiente, por ejemplo:

```txt
OE-01: Crear estructura inicial del proyecto
OE-02: Implementar simulacion de puertas logicas
OE-03: Agregar generacion de resultados y grafico
```

## Observaciones

El proyecto usa rutas relativas, por lo que puede ejecutarse desde distintas computadoras sin depender de rutas locales especificas. Los resultados generados quedan dentro de la carpeta `resultados`.
