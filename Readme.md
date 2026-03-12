🚖 Urban Routes – Proyecto de Automatización QA

"Python" (https://img.shields.io/badge/Python-3.x-blue)
"Selenium" (https://img.shields.io/badge/Selenium-WebDriver-green)
"Pytest" (https://img.shields.io/badge/Pytest-Automatización-orange)
"QA Automation" (https://img.shields.io/badge/QA-Automation-purple)

✨ Sobre el proyecto

Este proyecto forma parte de mi proceso de aprendizaje en Automatización de Pruebas (QA Automation).
El objetivo fue automatizar el flujo completo de solicitud de un taxi en la aplicación web Urban Routes, utilizando Python, Selenium WebDriver y Pytest.

Durante el desarrollo del proyecto practiqué la simulación de acciones reales de un usuario dentro de la aplicación, verificando que cada paso del proceso funcione correctamente.

Me siento muy feliz con el resultado de este proyecto porque me permitió fortalecer mis conocimientos en automatización de pruebas, localizadores estables y organización del código. 😊

---

🧪 Escenario de prueba automatizado

La prueba automatizada simula el siguiente flujo de usuario dentro de la aplicación:

1️⃣ Ingresar dirección de origen y destino.
2️⃣ Escribir un mensaje para el conductor.
3️⃣ Activar la opción “Manta y pañuelos”.
4️⃣ Solicitar 2 helados utilizando el botón de incremento. 🍦🍦
5️⃣ Presionar el botón “Pedir un taxi”.
6️⃣ Verificar que el proceso de solicitud del viaje se complete correctamente.

Este flujo permite validar que la funcionalidad principal de solicitud de taxi funciona correctamente de principio a fin.

---

🧱 Estructura del proyecto

El proyecto está organizado utilizando el patrón de diseño Page Object Model (POM), lo que permite mantener el código limpio, organizado y fácil de mantener.

UrbanRoutesAutomation
│
├── UrbanRoutesPage.py      # Métodos que representan acciones del usuario
├── UrbanRoutesLocators.py  # Localizadores de los elementos de la página
├── TestUrbanRoutes.py      # Escenario de prueba automatizado
└── README.md               # Documentación del proyecto

📌 Ventajas de utilizar Page Object Model

- Separación entre lógica de pruebas y localizadores
- Código más legible
- Pruebas más fáciles de mantener
- Reutilización de métodos

---

🛠️ Tecnologías utilizadas

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Esperas explícitas (WebDriverWait)

---

▶️ Cómo ejecutar las pruebas

1️⃣ Clonar el repositorio

git clone <URL-del-repositorio>

2️⃣ Instalar dependencias

pip install selenium
pip install pytest

3️⃣ Ejecutar las pruebas

pytest

Pytest ejecutará automáticamente el escenario de prueba y mostrará los resultados en la terminal.

---

💡 Nota sobre el nombre del repositorio

Es posible que el nombre de este repositorio sea diferente al del repositorio original que se clonó inicialmente.

Durante el desarrollo del proyecto trabajé en dos computadoras diferentes, lo que ocasionó algunos conflictos relacionados con el entorno y la configuración del proyecto. Después de consultar con los instructores, la mejor solución fue crear nuevamente el proyecto desde cero y continuar el desarrollo en un entorno limpio.

Por esta razón, el nombre de este repositorio es diferente al del repositorio original.



🌱 Aprendizajes obtenidos

Este proyecto me permitió desarrollar y practicar habilidades importantes dentro del área de QA Automation, como:

✔ Automatización de pruebas de interfaz con Selenium
✔ Creación de XPath estables
✔ Uso de esperas explícitas para manejar elementos dinámicos
✔ Organización del código utilizando Page Object Model
✔ Análisis y solución de errores durante la ejecución de pruebas

Completar este proyecto ha sido un paso muy importante en mi camino dentro del mundo de la automatización de pruebas, y estoy muy emocionada de seguir aprendiendo y creciendo en esta área. 🚀



🙌 Reflexión final

Este proyecto representa un avance importante en mi formación como futura QA Automation Engineer.

Cada reto que surgió durante el desarrollo fue una oportunidad para aprender más sobre herramientas de automatización y buenas prácticas en pruebas de software.

¡Gracias por tomarte el tiempo de revisar este proyecto! 😊