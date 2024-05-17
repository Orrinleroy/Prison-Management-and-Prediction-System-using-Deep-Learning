import gradio as gr
from pymongo import MongoClient

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client['prison_management']
collection = db['prisoners']

# Function to add prisoner record
def add_prisoner(name, age, crime, sentence):
    record = {
        "name": name,
        "age": age,
        "crime": crime,
        "sentence": sentence
    }
    collection.insert_one(record)
    return f"Prisoner {name} added successfully."

# Function to view all prisoner records
def view_prisoners():
    prisoners = collection.find()
    prisoner_list = []
    for prisoner in prisoners:
        prisoner_list.append([prisoner['name'], prisoner['age'], prisoner['crime'], prisoner['sentence']])
    return prisoner_list

# Function to delete prisoner record by name
def delete_prisoner(name):
    result = collection.delete_one({"name": name})
    if result.deleted_count > 0:
        return f"Prisoner {name} deleted successfully."
    else:
        return f"Prisoner {name} not found."

# Gradio UI setup
def interface():
    with gr.Blocks() as demo:
        with gr.Tab("Add Prisoner"):
            with gr.Row():
                name = gr.Textbox(label="Name")
                age = gr.Number(label="Age")
                crime = gr.Textbox(label="Crime")
                sentence = gr.Textbox(label="Sentence")
                submit_btn = gr.Button("Add Prisoner")
                result = gr.Textbox(label="Result", interactive=False)

            submit_btn.click(fn=add_prisoner, inputs=[name, age, crime, sentence], outputs=result)

        with gr.Tab("View Prisoners"):
            view_btn = gr.Button("View Prisoners")
            prisoner_list = gr.Dataframe(headers=["Name", "Age", "Crime", "Sentence"])

            view_btn.click(fn=view_prisoners, outputs=prisoner_list)

        with gr.Tab("Delete Prisoner"):
            delete_name = gr.Textbox(label="Name of Prisoner to Delete")
            delete_btn = gr.Button("Delete Prisoner")
            delete_result = gr.Textbox(label="Result", interactive=False)

            delete_btn.click(fn=delete_prisoner, inputs=delete_name, outputs=delete_result)

    demo.launch()

if __name__ == "__main__":
    interface()
