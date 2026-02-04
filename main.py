from fastapi import FastAPI, HTTPException

app = FastAPI()

#in-memory, not a db
notes=[]
#note_id_counter is used to assign a unique ID to each note, and its value is manually incremented every time a new note is created.
note_id_counter =1

@app.get('/health')
#This function receives data from the client,creates a new note
def health_check():
    return {"status":"ok"}


#POST-create new data
@app.post("/notes")
def create_note(content: str):
    global note_id_counter

    note = {
        "id": note_id_counter,
        "content": content #Stores the text sent by the user
    }

    notes.append(note)
    note_id_counter += 1

    return note
