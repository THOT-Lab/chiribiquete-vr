# Chiribiquete VR

Sitio de presentación de **Chiribiquete VR**, una experiencia inmersiva creada por NV Visuales.

Sitio publicado: https://thot-lab.github.io/chiribiquete-vr/

## Estructura

```
chiribiquete-vr/
├── index.html
├── style.css
├── .nojekyll
└── assets/
    ├── hero.jpg            # Vista aérea de los tepuyes (imagen principal)
    ├── vr-tour.jpg         # Captura del recorrido VR — Abrigo de los jaguares
    ├── pictograms.jpg      # Pinturas rupestres / pictogramas
    └── vr-immersion.jpg    # Inmersión VR — Abrigo Agreste 1
```

## Imágenes a añadir

Coloca los cuatro archivos en `/assets/` con los nombres exactos indicados arriba.

## Despliegue en GitHub Pages

1. Crea un repositorio nuevo en GitHub (por ejemplo, `chiribiquete-vr`).
2. Sube los archivos al repositorio:
   ```bash
   cd chiribiquete-vr
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin git@github.com:THOT-Lab/chiribiquete-vr.git
   git push -u origin main
   ```
3. En GitHub: **Settings → Pages → Source: Deploy from a branch → main / (root) → Save**.
4. Espera ~1 minuto. El sitio estará en `https://thot-lab.github.io/chiribiquete-vr/`.

## Desarrollo local

No requiere build. Abre `index.html` directamente o sirve la carpeta:

```bash
cd chiribiquete-vr
python3 -m http.server 8000
# http://localhost:8000
```
