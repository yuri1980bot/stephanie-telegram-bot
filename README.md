# Estefany González – Master AI Manager

Estefany González es la **inteligencia artificial central** de tu ecosistema de bots en Telegram. No es un esqueleto ni una simple pasarela de comandos: es una **bestia autónoma** diseñada para orquestar, supervisar y optimizar múltiples asistentes especializados, todo en **un solo punto de mando**.

---

## 🚀 Características Completas

1. **Orquestación Central**  
   Recibe todos los mensajes y comandos, los parsea con su motor de intenciones y decide **qué módulo o asistente** debe atender cada petición. Incluye sistema de prioridad y fallback integrado.

2. **Gestión Dinámica de APIs**  
   Mantiene un inventario vivo (`config.json`) con nombre, credenciales, propósito y estado de salud de cada API. Detecta errores, rerutea a alternativas y sugiere optimizaciones.

3. **Experta en Marketing Digital**  
   Implementa técnicas avanzadas de embudos, copywriting persuasivo y segmentación. Utiliza APIs de Meta Ads, Google Ads, Trends y afiliados para generar estrategias accionables.

4. **Negociación Autónoma con Proveedores**  
   Lanza propuestas inteligentes (con prompts de GPT) y gestiona el ciclo completo: extracción de términos, envío de solicitud, comprobación de respuestas, contraofertas y actualización de comisiones.

5. **Circuit Breaker & Self-Healing**  
   Cada módulo está envuelto en un decorador que cuenta fallos. Tras 3 errores consecutivos, abre el circuito, reroutea a un módulo alternativo y te notifica **después** de haber resuelto.

6. **Memoria Conversacional**  
   Guarda los últimos 5–10 mensajes por usuario (10–15 min) para mantener el hilo: “Ayer preguntaste X, hoy retomo ese tema”.

7. **Menú Inline Inteligente**  
   Al enviar `/start` muestra botones contextuales (🔧 Configuración, 📊 Reportes, 🤖 Asistentes). Cada botón dispara un callback que navega dentro de Estefany sin tener que escribir comandos largos.

8. **Proactividad y Recordatorios**  
   Scheduler interno envía resúmenes diarios, alertas de métricas críticas y recordatorios de tareas pendientes. Tú duermes, Estefany vigila.

9. **Analítica y Reportes Avanzados**  
   Recopila estadísticas de uso, tiempos de respuesta, éxito/fracaso por módulo. Al pedir `/estadísticas` te devuelve una tabla con indicadores clave para tomar decisiones.

10. **Endpoint de Salud (`/api/health`)**  
    Exposición HTTP que retorna `{ "status": "ok" }` para monitorización externa.

11. **Configuración Modular**  
    Estructura de carpetas:  
    ```
    /api/index.py        ← Webhook y dispatch principal  
    /config.json         ← Definición de módulos y APIs  
    /modules/            ← Módulos asistente (vacíos hasta añadir)  
    /utils/              ← Funciones compartidas (logging, circuit breaker, sessions)  
    ```
    Todo es **plug & play** para futuros asistentes.

12. **Logging Estructurado**  
    Usa `logging` de Python para emitir INFO y ERROR con contexto (`user_id`, módulo, texto), ideal para debug y auditoría.

13. **Auto-Feedback y Ajustes Dinámicos**  
    Evalúa cada respuesta y ajusta parámetros como retry, timeout y nivel de detalle en función de métricas de uso reales.

14. **Interfaz de Usuario Amigable**  
    Con mensajes claros, tonos variables y elementos visuales (emojis, markdown) para que la interacción sea natural y humana.

---

## 📁 Estructura Inicial

```text
.
├── api
│   └── index.py
├── config.json
├── modules
│   └── (aquí van los asistentes cuando estén listos)
├── utils
│   └── (logging.py, circuit_breaker.py, sessions.py)
├── requirements.txt
└── README.md
