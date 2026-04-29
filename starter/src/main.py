from fastapi import FastAPI

GREETINGS: dict[str, str] = {
    "es": "¡Hola, {name}!",
    "en": "Hello, {name}!",
    "fr": "Bonjour, {name}!",
    "de": "Hallo, {name}!",
    "it": "Ciao, {name}!",
    "pt": "Olá, {name}!",
}

SUPPORTED_LANGUAGES = list(GREETINGS.keys())

app = FastAPI(
    title="Bike Store API",
    description="API básica para tienda de bicicletas",
    version="1.0.0"
)


@app.get("/")
async def root() -> dict[str, str]:
    """Información de la API."""

    return {
        "name": "Bike Store API",
        "version": "1.0.0",
        "domain": "bike-store"
    }


@app.get("/customer/{name}")
async def greet(
    name: str,
    language: str = "es",
) -> dict[str, str]:
    """
    Bienvenida a clientes de la tienda.
    """

    messages = {
        "es": f"¡Bienvenido a la tienda de bicicletas, {name}!",
        "en": f"Welcome to the bike store, {name}!",
        "fr": f"Bienvenue au magasin de vélos, {name}!"
    }

    return {
    "message": messages.get(language, messages["es"]),
    "language": language,
    "name": name
}


@app.get("/bike/{identifier}/info")
async def bike_info(
    identifier: str,
    detail_level: str = "basic",
) -> dict:
    """
    Información de una bicicleta.
    """

    if detail_level == "full":
        return {
            "id": identifier,
            "model": "Mountain Bike",
            "brand": "Trek",
            "price": 1200000,
            "stock": 8
        }

    return {
        "id": identifier,
        "model": "Mountain Bike",
        "price": 1200000    
    }

def get_day_period(hour: int) -> tuple[str, str]:

    if 6 <= hour < 12:
        return ("Taller y reparaciones disponibles", "morning")

    elif 12 <= hour < 18:
        return ("Ventas y repuestos disponibles", "afternoon")

    else:
        return ("Servicio nocturno limitado", "night")
    
@app.get("/service/schedule")
async def greet_time_based(
    hour: int,
) -> dict[str, str | int]:

    if hour < 0 or hour > 23:
        return {"error":"Hora inválida"}

    message, period = get_day_period(hour)

    return {
        "message": message,
        "hour": hour,
        "period": period
    }


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Verifica el estado de la API."""

    return {
        "status": "healthy",
        "domain": "bike-store"
    }

# ============================================
# VERIFICACIÓN
# ============================================
# Una vez completados todos los TODOs:
#
# 1. Ejecutar:
#    docker compose up --build(fue con venv)
#
# 2. Probar en el navegador:(hecho)
#    http://localhost:8000/docs
#
# 3. Verificar cada endpoint:
# - GET /
# - GET /customer/Carlos
# - GET /customer/Carlos?language=en
# - GET /bike/bike001/info
# - GET /bike/bike001/info?detail_level=full
# - GET /service/schedule?hour=10
# - GET /health
#      (hechos)
# ============================================