from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/flashcards")
def get_flashcards():
	return {"flashcards": [
		{"id": 1, "question": "What is the capital of France?", "answer": "Paris"},
		{"id": 2, "question": "What is 2 + 2?", "answer": "4"},
		{"id": 3, "question": "What is the largest planet in our solar system?", "answer": "Jupiter"}
	]}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)