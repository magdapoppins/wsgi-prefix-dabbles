Start w uvicorn asgi server `uvicorn main:app --reload`

gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker