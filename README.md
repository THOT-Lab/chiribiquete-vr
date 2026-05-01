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
    ├── expo-lima-20s.mp4   # Extracto video web de la instalación
    ├── vr-test-nv-visuales.mp4
    ├── IMG_0724.JPG
    ├── IMG_0728_NV_VISUALES.JPG
    └── CHIRIBIQUETTE_Vector-Logo.pdf
```

## Medios

Los archivos originales pesados se mantienen fuera de Git cuando no son necesarios para la publicación. El sitio usa versiones web optimizadas para GitHub Pages.

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
