# Chiribiquete VR

Sitio de presentación de **Chiribiquete VR**, una experiencia inmersiva creada por NV Visuales y THOT.

Sitio publicado: https://thot-lab.github.io/chiribiquete-vr/ (ES) · [en.html](https://thot-lab.github.io/chiribiquete-vr/en.html) (EN) · [fr.html](https://thot-lab.github.io/chiribiquete-vr/fr.html) (FR)

## Estructura

```
├── index.html        # Versión en español (referencia)
├── en.html           # Generado por tools/i18n.py — no editar a mano
├── fr.html           # Generado por tools/i18n.py — no editar a mano
├── style.css
├── script.js
├── tools/i18n.py     # Traducciones EN/FR y generación de en.html / fr.html
└── assets/
    ├── hero-tepuy*.jpg      # Imagen de portada
    ├── pictos/              # Pictogramas rupestres (máscaras PNG)
    ├── partners/            # Logos de socios (blancos)
    ├── zurich-panel-*.jpg   # Muros de la instalación del Museo Rietberg
    └── meta/                # Favicon (jaguar), iconos e imagen para redes
```

## Idiomas

`index.html` (español) es la versión de referencia. Después de modificarla:

1. actualizar la traducción correspondiente en `tools/i18n.py` (tuplas español / inglés / francés);
2. ejecutar `python3 tools/i18n.py`, que regenera `en.html` y `fr.html`.

El script se detiene si un texto español ya no se encuentra en `index.html`.

## Medios

Los archivos originales pesados (RAW, vídeo completo) se mantienen fuera de Git (`.gitignore`). El sitio usa versiones web optimizadas.

## Despliegue

GitHub Pages: **Settings → Pages → Deploy from a branch → main / (root)**. Cada push a `main` actualiza el sitio en ~1 minuto.

## Desarrollo local

No requiere build:

```bash
python3 -m http.server 8000
# http://localhost:8000
```
