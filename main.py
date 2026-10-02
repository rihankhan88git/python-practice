from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def get_message():
    return {"message": "Welcome to carrier craft technologies its a tech  World"}

@app.get("/details")
def get_details():
    return {"sty_id":101,
            "sty_name":"jack",
            "sty_course":"AIML",
            "sty_fee":12000,
            "sty_gender":"male",
            "sty_language":"english",
            "sty_country":"USA",
            "sty_project":"Fast API",

            }
