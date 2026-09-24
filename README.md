# Desarrollo de Predicados en Python

## ¿Qué es este proyecto?

Este es un pequeño programa en Python que muestra cómo trabajar con **predicados lógicos** (como "Sofía asiste a practicaLab3") usando solo funciones y datos básicos. Es útil para entender cómo se representa el conocimiento en sistemas de razonamiento automático.

## ¿Cómo ejecutarlo?

1. Asegúrate de tener **Python 3** instalado en tu computadora.
2. Descarga o clona este repositorio.
3. Abre una terminal (símbolo de sistema) y navega a la carpeta del proyecto.
4. Ejecuta el siguiente comando:

```bash
python "desarrollo de predicados python.py"
```

> **Nota**: Si el nombre del archivo con espacios te causa problemas, puedes renombrarlo a algo como `predicados.py` y luego ejecutar `python predicados.py`.

Verás una salida como esta:

```
--- EVALUACIÓN DE CONSULTAS ---

1. Predicado: AsisteA(alumno, actividad)
Consulta Positiva: ¿Sofía asiste a practicaLab3?
R: True
Consulta Negativa: ¿Carlos asiste a practicaLab3?
R: False

2. Predicado: EsTutorDe(alumno, grupo)
Consulta Positiva: ¿Diego es tutor del grupoC?
R: True
Consulta Negativa: ¿Ana es tutora del grupoC?
R: False

... (y así sucesivamente para los otros predicados)
```

## Explicación rápida del código

El programa está dividido en tres partes claras:

### 1. Base de conocimientos (los hechos)
Al inicio, definimos listas de estudiantes, actividades, etc., y luego creamos diccionarios que guardan quién hace qué. Por ejemplo:

```python
asiste_a_hechos = {
    "sofia": ["practicaLab3"]
}
```
Esto significa: *Sofía asiste a practicaLab3*.

### 2. Las funciones de predicado
Cada predicado es una función que recibe dos argumentos y consulta la base de conocimientos. Por ejemplo:

```python
def AsisteA(alumno, actividad):
    return actividad in asiste_a_hechos.get(alumno, [])
```
Esta función pregunta: ¿Está `actividad` en la lista de actividades de `alumno`? Si el alumno no está en el diccionario, se asume que no asiste a nada (lista vacía) y devuelve `False`.

### 3. Las consultas de prueba
Al final, imprimimos preguntas positivas (que esperamos que sean `True`) y negativas (que esperamos que sean `False`) para cada predicado, mostrando el resultado.

## ¿Cómo puedo modificarlo?

- **Agregar nuevos hechos**: Edita los diccionarios al inicio (como `asiste_a_hechos`, `es_tutor_de_hechos`, etc.).
- **Agregar nuevos predicados**: Copia una de las funciones existentes, cambia su nombre y lógica según necesites.
- **Probar otras consultas**: Modifica la sección de "Consultas" al final para hacer tus propias preguntas.

## Ideas para extender el proyecto (si te interesa)

- Permitir que el usuario ingrese consultas desde el teclado.
- Guardar la base de conocimientos en un archivo externo (JSON o CSV).
- Añadir más tipos de relaciones (por ejemplo, "es amigo de", "tiene edad mayor que").
- Usar conjuntos (`set`) en lugar de listas para búsquedas más rápidas.

---

¡Diviértete experimentando con la lógica! Si tienes dudas, puedes mirar el código comentado o preguntar a un compañero o profesor.