from fastapi import FastAPI
import uvicorn
from queries.routes import queries_actions

app = FastAPI()
app.include_router(queries_actions, prefix="/api")



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)