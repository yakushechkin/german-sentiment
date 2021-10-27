from germansentiment import SentimentModel
from fastapi import FastAPI, HTTPException

from app.schemas import SentimentRequest, SentimentResponse
from app.log import logger


app = FastAPI()


@app.get("/")
async def read_root():
    logger.info("The get method.")
    return {"About": "German Sentiment Classification with Bert"}


@app.post("/predict", response_model=SentimentResponse)
async def create_item(request: SentimentRequest):

    logger.info("The received texts for classification: %s", request.texts)
    try:
        model = SentimentModel()
        prediction = model.predict_sentiment(request.texts)
    except Exception as e:
        logger.error("Exception: %s", e)
        raise HTTPException(status_code=400, detail="Model cannot be found.") from None

    logger.info("Sentiments: %s", prediction)
    return SentimentResponse(sentiments=prediction)
