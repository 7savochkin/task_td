import starlette.status
import uvicorn
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

from base.exceptions import ServerError
from telegram_app import routers as tg_routers

app = FastAPI()

# include telegram endpoints
app.include_router(tg_routers.telegram_router)


# handle Server Error Exception
@app.exception_handler(ServerError)
def server_error_handler(request: Request, error) -> JSONResponse: # noqa
    return JSONResponse({'detail': str(error)},
                        status_code=starlette.status.HTTP_400_BAD_REQUEST)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
