from PIL import Image

# Abrir la imagen
imagen = Image.open("imagen.jpg")

# Redimensionar la imagen
ancho_deseado = 1920
alto_deseado = 1080
imagen_redimensionada = imagen.resize((ancho_deseado, alto_deseado))

# Guardar la imagen redimensionada
imagen_redimensionada.save("imagen_redimensionada.jpg")