# App generadora de chistes y procesamiento de datos de la Api open meteo para hyo
además de la aplicación genera 10 chistes aleatorios en inglés 
# Instalación
python -m venv .venv 
source venv/bin/activate (o venv\Scripts\activate en windows )
pip install -e .
#  Uso básico
para los chistes: 
```python
from tecemer_lab import app
```
para la extracción de un json("pronostico_huancayo.json") y  un csv (pronostico_huancayo.csv)de la api open meteo
```python
from tecemer_lab import clima.py
```
para el procesamiento del csv en un csv procesado("pronostico_huancayo_procesado.csv") y un resumen del analisis(resumen_por_categoria.csv)
```python
from tecemer_lab import analisis.py
```
# Estructura del proyecto

```
tecemer-lab
├─ pronostico_huancayo.csv
├─ pronostico_huancayo.json
├─ pronostico_huancayo_procesado.csv
├─ pyproject.toml
├─ README.md
├─ requirements.txt
├─ resumen_por_categoria.csv
└─ src
   └─ tecemer_lab
      ├─ analisis.py
      ├─ app.py
      ├─ clima.py
      ├─ numpy_demo.py
      └─ __init__.py

```
# autor
Grijalva Martinez Italo Osmar
facultad : Ingeniería de sistemas
semana #2