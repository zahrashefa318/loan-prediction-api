from fastapi import FastAPI
from routes.predict import router as  predict_router
from routes.token_route import route as token_router
from fastapi.middleware.cors import CORSMiddleware
import db.db_init


app=FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_methods=["*"],
                   allow_headers=["*"],
                   allow_credentials=True)

app.include_router(predict_router)
app.include_router(token_router)
if __name__=="__main__": # It prevents only the server (uvicorn.run) from executing when imported.
    import uvicorn
    uvicorn.run("main:app",reload=True) # reload = true means Automatically restart the server whenever I change my code
