"""Genera relevamiento.html a partir de datos/gestiones.json y herramientas/plantilla.html."""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
datos = json.loads((RAIZ / "datos" / "gestiones.json").read_text(encoding="utf-8"))
plantilla = (RAIZ / "herramientas" / "plantilla.html").read_text(encoding="utf-8")
js = json.dumps(datos, ensure_ascii=False).replace("</", "<\\/")
(RAIZ / "relevamiento.html").write_text(plantilla.replace("/*DATA*/", js), encoding="utf-8")
print("relevamiento.html generado")
