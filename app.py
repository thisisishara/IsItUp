# # app.py
# from sanic import Sanic, response
#
# from shared.constants import APP_NAME, APP_VERSION
#
# app = Sanic(name=f"{APP_NAME}")
# app.static(uri="/static", file_or_directory="./static", name="static")
#
#
# @app.route("/")
# async def root(request):
#     return response.text(f"Hello from {APP_NAME} {APP_VERSION}")
#
#
# @app.websocket('/feed')
# async def feed(request, ws):
#     data = "hello"
#     print("sending: " + data)
#     await ws.send(data)
#     data_r = await ws.recv()
#     print("Received: " + data_r)
#
#
# @app.route("/health")
# async def health(request):
#     return response.json({"status": "ok"})
#
#
# if __name__ == '__main__':
#     app.run(host='localhost', port=8000, debug=True)
import subprocess

if __name__ == '__main__':
    subprocess.run(["waitress-serve", "--host=localhost", "--port=8001", "run:app"])
