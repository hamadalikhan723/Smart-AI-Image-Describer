import gradio as gr
from model import generate_caption


def predict(image):
    if image is None:
        return "Please upload an image first."

    return generate_caption(image)


interface = gr.Interface(
    fn=predict,
    inputs=gr.Image(
        type="pil",
        label="Upload Image"
    ),
    outputs=gr.Textbox(
        label="AI Image Description",
        lines=8,
        placeholder="Your detailed image description will appear here..."
    ),
    title="Smart AI Image Describer 🤖",
    description=(
        "Upload an image and get an AI-generated detailed description "
        "in 5–8 sentences."
    ),
    examples=None,
    flagging_mode="never"
)


interface.launch()