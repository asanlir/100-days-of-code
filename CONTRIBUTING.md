# Normas de Contribución - 100 Days of Code

Gracias por contribuir a este repositorio de aprendizaje. Estas normas aseguran consistencia y claridad en el proyecto.

## 📋 Principios Generales

- **Propósito**: Documentar el aprendizaje progresivo en Python, no construir productos finales
- **Estructura**: Mantener una carpeta por proyecto complejo; scripts simples en la raíz
- **Calidad**: Código legible, modular y con convenciones consistentes
- **Licencia**: MIT - Todos los aportes están bajo esta licencia

## 🐍 Convenciones de Código

### Nombrado

- **Funciones y variables**: `snake_case` (p.ej. `is_resource_sufficient()`, `total_cost`)
- **Constantes**: `UPPER_CASE` (p.ej. `STARTING_POSITIONS`, `GRID_WIDTH`)
- **Clases**: `PascalCase` (p.ej. `CoffeeMaker`, `QuizBrain`, `Snake`)
- **Módulos**: `snake_case` (p.ej. `question_model.py`, `money_machine.py`)

### Código Python

- **Indentación**: 4 espacios (configurado en `.editorconfig`)
- **Línea máxima**: 88 caracteres (como Black)
- **Imports**: Estándar → Terceros → Locales

  ```python
  import os
  import datetime as dt

  import pandas as pd
  import requests

  from question_model import Question
  from art.cards import logo
  ```

- **Docstrings**: Presentes en clases y métodos públicos
  ```python
  class CoffeeMaker:
      """Modela la máquina que prepara el café."""

      def is_resource_sufficient(self, drink):
          """Retorna True si hay ingredientes suficientes, False en caso contrario."""
  ```

### Organización de Proyectos

- Proyectos complejos en carpetas dedicadas con `main.py` como entrada
- Módulos separados por responsabilidad (`menu.py`, `coffee_maker.py`, `money_machine.py`)
- Datos externos en subdirectorios (`data/`, `images/`, `letter_templates/`)
- Módulos compartidos en `/art/`

## 📝 Commits

Usar **Conventional Commits** en español:

```
<tipo>(scope): <descripción>

<cuerpo (opcional)>

<pie (opcional)>
```

### Tipos válidos

- `feat`: Nuevo ejercicio, feature o funcionalidad
- `fix`: Corrección de error
- `docs`: Actualización de documentación o README
- `style`: Cambios de formato (no afectan lógica)
- `refactor`: Reorganización de código sin cambiar comportamiento
- `chore`: Configuración, dependencias, archivos base
- `test`: Adición o mejora de tests

### Reglas

- Usa verbo imperativo en presente: "agrega autenticación" (no "agregada")
- Sin punto final en la descripción
- Scope es opcional pero recomendado: `feat(snake): agrega detección de colisiones`
- Mantén mensajes concisos (<50 caracteres en la primera línea)

**Ejemplos válidos:**

```
feat(pong): agrega lógica de colisión de pelota
fix(habit-tracker): corrige petición a API
docs: actualiza guía de instalación
style: normaliza espaciado en coffee_machine.py
refactor(quiz-game): separa lógica de UI en clase QuizBrain
```

## 🧪 Calidad del Código

- **Legibilidad**: Usa nombres descriptivos; el código es tu pensamiento
- **Modularidad**: Cada clase y función tiene una única responsabilidad
- **Sin repetición**: Extrae código repetido a funciones reutilizables
- **Variables locales**: Evita variables globales; pasa parámetros entre funciones

## 📂 Estructura de Carpetas

```
proyecto/
├── main.py              # Entrada principal
├── modulo_1.py          # Lógica específica
├── modulo_2.py
├── data/                # Datos externos
│   └── config.csv
├── images/              # Recursos visuales
└── templates/           # Plantillas (si aplica)
```

## 🔄 Flujo de Trabajo

1. **Fork/Branch**: Crea una rama para tu aporte (`feat/nuevo-proyecto`, `fix/error`)
2. **Código**: Escribe el código siguiendo estas normas
3. **Commit**: Haz commits pequeños y significativos con mensajes claros
4. **PR**: Describe qué aprendiste y qué resuelve tu aporte
5. **Review**: Sé abierto a sugerencias y mejoras

## 🛠️ Herramientas Recomendadas

- **Editor**: VS Code con Python Extension
- **Formatter**: Black o Autopep8
- **Linter**: Pylint o Flake8
- **Version Control**: Git Conventional Commits

## ❓ Preguntas Frecuentes

**¿Debo escribir tests?**
No es obligatorio para este proyecto de aprendizaje, pero es buena práctica. Si incluyes tests, usa `pytest`.

**¿Puedo modificar ejercicios existentes?**
Sí, si es para mejorar la legibilidad, corregir errores o agregar funcionalidad educativa. Explica el cambio en el commit.

**¿Qué pasa con las dependencias?**
Añade nuevas dependencias solo si son educativas. Actualiza cualquier `requirements.txt` o documentación.

**¿Debo comentar mi código?**
Prefiere código legible a comentarios. Usa docstrings para explicar _por qué_, no _qué_.

---

**Última actualización:** Abril 2026  
**Licencia:** MIT
