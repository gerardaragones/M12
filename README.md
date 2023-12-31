# 2daw-m12-projecte1

Codi d'exemple que serveix de suport per la part backend pel projecte 1 del M12 de 2n de DAW.

## Setup

### Python Virtual Environment

Crea l'entorn:

    python3 -m venv .venv

L'activa:

    source .venv/bin/activate

Instal·la el requisits:

    pip install -r requirements.txt

Alternativament, els requisits es poden instal·lar manualment:

    pip install -U pip
    pip install -U flask python-dotenv Flask-SQLAlchemy flask-wtf flask-login email_validator

Per a generar el fitxer de requiriments:

    pip freeze > requirements.txt

Per desactivar l'entorn:

    deactivate

### Fitxer .env

Crea el fitxer `.env` a partir del `.env.exemple`

### Base de dades

Crea la base de dades sqlite (un fitxer amb extensió .db) amb la comanda:

    python init_database.py

### Inicia l'aplicació

Executa:

    flask run

I obre un navegador a l'adreça: [http://127.0.0.1:5000](http://127.0.0.1:5000)

Autenticat amb l'usuari `mortadelo@insjoaquimmir.cat` amb contrasenya `patata`.

### DEBUG

Des de l'opció de `Run and Debug`, crea un fitxer animenat `launch.json` amb el contingut següent:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "MY APP",
            "type": "python",
            "request": "launch",
            "module": "flask",
            "env": {
                "FLASK_APP": "wsgi.py",
                "FLASK_DEBUG": "1"
            },
            "args": [
                "run",
                "--no-debugger",
                "--no-reload"
            ],
            "jinja": true,
            "justMyCode": true
        }
    ]
}
```

## Enllaços de referència

* Flask login: https://j2logo.com/tutorial-flask-leccion-4-login/
* Per visualitzar les cookies he fet servir [Check my cookies](https://chrome.google.com/webstore/detail/check-my-cookies/idmefaajmbkeajdiafefcleiaihkahnm)

## TODO

* logs: https://j2logo.com/tutorial-flask-leccion-9-logs-en-flask/