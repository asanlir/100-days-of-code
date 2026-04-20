# 100 Days of Code | Python

Repositorio de practica personal para registrar el progreso del curso **100 Days of Code** (Python).

## Descripción

Este repositorio centraliza ejercicios, retos y mini proyectos desarrollados durante el proceso de aprendizaje.

El objetivo no es construir un producto final, sino documentar una evolución técnica constante mediante entregas pequeñas y frecuentes.

## Objetivos del repositorio

- Mantener un historial claro de avances diarios.
- Consolidar en un único lugar todos los proyectos del curso.
- Practicar buenas bases de trabajo con Git y control de versiones.

## Alcance actual

- Scripts y juegos de consola.
- Proyectos gráficos con Turtle.
- Ejercicios organizados por carpetas temáticas.

## Requisitos

- Python 3.10 o superior.

## Como ejecutar proyectos

Desde la raíz del repositorio:

```bash
python "ruta/al/archivo.py"
```

Ejemplos:

```bash
python auction.py
python "Turtle Crossing/main.py"
python "Quiz Game/main.py"
```

## Flujo de actualización

- Se agregaran nuevos proyectos a medida que avance el curso.
- Cada avance se versionara mediante commits pequeños y descriptivos.

## Convenciones

- Archivo .gitignore configurado para excluir cache, entornos virtuales y artefactos temporales.
- Estructura de carpetas orientada a separar proyectos por tema o modulo.

## Guía de commits

Para mantener un historial limpio, consistente y fácil de entender, este repositorio sigue el estándar Conventional Commits con las siguientes reglas:

### 1. Estructura del mensaje

Cada commit debe seguir el siguiente formato:

```text
<type>(scope): <description>

<body>

<footer>
```

- `type`: tipo de cambio realizado.
- `scope` (opcional): modulo, componente o area afectada.
- `description`: resumen breve del cambio.
- `body` (opcional): explicación detallada.
- `footer` (opcional): referencias a issues o tareas.

### 2. Usa verbo en imperativo

El mensaje debe comenzar con un verbo en presente e imperativo.

Correcto:

- `feat: agrega autenticación con JWT`
- `fix: corrige error en calculo de totales`

Incorrecto:

- `feat: agregado autenticación`
- `fix: se corrigió un bug`

### 3. No uses punto final

El mensaje de commit es un titulo, no una frase completa.

Correcto:

- `docs: actualiza guía de instalación`

Incorrecto:

- `docs: actualiza guía de instalación.`

### 4. Limita el resumen a 50 caracteres

- Se claro, directo y especifico.
- Evita descripciones largas en la primera linea.

Correcto:

- `refactor: simplifica lógica de validación`

Incorrecto:

- `refactor: realiza una simplificación extensa de toda la lógica de validación del sistema`

### 5. Usa el cuerpo para añadir contexto

Si necesitas explicar el cambio, hazlo en el cuerpo:

```text
feat: agrega sistema de autenticación

Se implementa autenticación con JWT incluyendo
middleware de validación y expiración de tokens
```

### 6. Usa prefijos semánticos

Utiliza los siguientes tipos de commit:

- `feat`: nueva funcionalidad.
- `fix`: corrección de errores.
- `perf`: mejora de rendimiento.
- `refactor`: cambios internos sin alterar funcionalidad.
- `docs`: cambios en documentación.
- `style`: formato, espacios o estilo.
- `test`: tests añadidos o modificados.
- `build`: cambios en build o dependencias.
- `ci`: cambios en integración continua.

### 7. Usa scope cuando sea necesario

Especialmente util en proyectos grandes o monorepos:

- `feat(auth): agrega login con Google`
- `fix(api): corrige error en endpoint de usuarios`

### 8. Un commit, un cambio lógico

Cada commit debe representar un cambio claro y aislado.

Correcto:

- `feat: agrega validación de formulario`

Incorrecto:

- `feat: agrega validación y cambia estilos y corrige bug`

### 9. Evita mensajes genéricos

No aportan valor al historial.

Evitar:

- `update`
- `cambios`
- `arreglos varios`

Usar:

- `fix: corrige error en renderizado de lista`

### 10. Usa el footer para referencias

```text
fix: corrige error en login

Fixes #42
```

Ejemplos completos:

```text
feat(game): agrega detección de colisiones

Se implementa lógica de colisiones entre jugador
y obstáculos para mejorar la jugabilidad
```

```text
docs: actualiza README con instrucciones

Añade sección de instalación y uso básico
```

```text
refactor(api): reorganiza estructura de rutas

Simplifica la gestión de endpoints y mejora
la mantenibilidad del código
```

## Estado

En progreso. Repositorio activo de aprendizaje.

## Autor

Alejandro Sánchez
