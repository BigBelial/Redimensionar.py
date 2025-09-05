# 🖼️ Redimensionador de Imágenes

Script en Python que redimensiona imágenes automáticamente usando PIL (Python Imaging Library). Convierte cualquier imagen a resolución Full HD (1920x1080) manteniendo la calidad.

## 📝 Descripción

Script Python con PIL para redimensionar imágenes automáticamente. Toma cualquier imagen JPG y la convierte a resolución Full HD (1920x1080 píxeles). Fácil de usar, rápido y eficiente. Ideal para estandarizar imágenes, crear fondos de pantalla o preparar contenido multimedia. Preserva formato JPG.

## 🚀 Uso Rápido

1. **Instalar PIL**:
   ```bash
   pip install Pillow
   ```

2. **Colocar imagen**: Asegúrate de tener `imagen.jpg` en el mismo directorio

3. **Ejecutar**:
   ```bash
   python redimensionar.py
   ```

4. **Resultado**: Se genera `imagen_redimensionada.jpg` en 1920x1080

## 📋 Código

```python
from PIL import Image

# Abrir la imagen
imagen = Image.open("imagen.jpg")

# Redimensionar la imagen
ancho_deseado = 1920
alto_deseado = 1080
imagen_redimensionada = imagen.resize((ancho_deseado, alto_deseado))

# Guardar la imagen redimensionada
imagen_redimensionada.save("imagen_redimensionada.jpg")
```

## 📦 Requisitos

- Python 3.x
- Pillow (PIL)
- Imagen fuente: `imagen.jpg`

## ✨ Características

- ✅ Redimensionamiento a Full HD
- ✅ Preserva formato JPG
- ✅ Código simple y claro
- ✅ Procesamiento rápido

---

💡 **Tip**: Modifica `ancho_deseado` y `alto_deseado` para otras resoluciones
