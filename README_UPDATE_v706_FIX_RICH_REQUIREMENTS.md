# v7.06 — Fix rich requirements

## Problema

El log muestra que Streamlit intenta instalar `rich 15.0.0` y después devuelve error de dependencias.

## Solución

Se fija una versión estable de `rich` y su pila:

```txt
rich==13.9.4
markdown-it-py==3.0.0
mdurl==0.1.2
pygments==2.19.2
```

## Subir a GitHub

Sube solo:

- requirements.txt
- README_UPDATE_v706_FIX_RICH_REQUIREMENTS.md

Después:

- Commit changes
- Streamlit → Reboot app
- Ctrl + F5

## Importante

En GitHub abre `requirements.txt` y comprueba que NO contiene:

- streamlit
- protobuf
- rich==15.0.0
