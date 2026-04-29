# Flight Deals

## Objetivo

Buscar vuelos baratos para varios destinos, comparar precios con un umbral guardado en una hoja de calculo y enviar alertas cuando aparece una mejor oferta.

## Requisitos

- Python 3.10+
- requests
- requests-cache
- python-dotenv
- twilio

## Modulos

- `main.py`
- `data_manager.py`
- `flight_search.py`
- `flight_data.py`
- `notification_manager.py`

## Variables de entorno (.env)

- `SHEETY_PRICES_ENDPOINT`
- `SHEETY_USERS_ENDPOINT`
- `SHEETY_USERNAME`
- `SHEETY_PASSWORD`
- `SERPAPI_API_KEY`
- `TWILIO_SID`
- `TWILIO_AUTH_TOKEN`
- `TWILIO_VIRTUAL_NUMBER`
- `TWILIO_VERIFIED_NUMBER`
- `TWILIO_WHATSAPP_NUMBER`
- `EMAIL_PROVIDER_SMTP_ADDRESS`
- `MY_EMAIL`
- `MY_EMAIL_PASSWORD`

## Ejecucion

```bash
python main.py
```
