# Smart AI Image Describer

Smart AI Image Describer is a lightweight image-understanding application that generates natural-language descriptions of uploaded images. Upload an image and the vision-language model analyzes its visible content, producing a clear description of the main subjects, their actions, important objects, and surroundings.

The application is built with **Python, Gradio, PyTorch, and the Moondream2 vision-language model**.

## Features

- **Image upload:** Upload an image through a simple Gradio interface.
- **AI-generated descriptions:** Generate a description of the image in approximately 5–6 clear sentences.
- **Visual context:** Describe visible subjects, actions, objects, and surroundings.
- **Vision-language model:** Uses Moondream2 for image understanding and text generation.
- **GPU inference:** Uses Hugging Face Spaces GPU integration to run inference on a GPU when available through the configured environment.
- **Simple interface:** Displays the generated description in an easy-to-read text box.

## Tech stack

- Python
- Gradio
- PyTorch
- Hugging Face Transformers
- Moondream2 (`vikhyatk/moondream2`)
- PIL / Pillow
- Hugging Face Spaces (`spaces` GPU decorator)

## How it works

1. The user uploads an image in the Gradio interface.
2. The image is converted to RGB and resized to a maximum dimension of 768 pixels.
3. Moondream2 encodes the image into visual embeddings.
4. A prompt instructs the model to describe only what is visibly present.
5. The model generates a description, which is displayed in the interface.

## Project structure

```text
Smart-AI-Image-Describer/
├── app.py       # Gradio user interface and prediction function
└── model.py     # Moondream2 loading and image-description inference
```

## Model details

- **Model:** `vikhyatk/moondream2`
- **Revision:** `2024-08-26` (pinned in the code)
- **Image handling:** RGB conversion and resizing to fit within 768 × 768 pixels
- **Generation:** Up to 150 new tokens
- **Inference:** PyTorch inference mode with half-precision model weights

The model is loaded with Hugging Face Transformers using `trust_remote_code=True`, as required by its custom model implementation.

## Run locally

The current `model.py` is configured for a CUDA GPU and uses the Hugging Face Spaces `spaces.GPU` decorator. A compatible GPU environment and the required dependencies are therefore needed to run this exact implementation.

### 1. Clone the repository

```bash
git clone https://github.com/hamadalikhan723/Smart-AI-Image-Describer.git
cd Smart-AI-Image-Describer
```

### 2. Install dependencies

Install the packages used by the application:

```bash
pip install gradio spaces torch transformers pillow
```

You may need to install a CUDA-compatible PyTorch build that matches your GPU and system. Refer to the official [PyTorch installation guide](https://pytorch.org/get-started/locally/).

### 3. Launch the application

```bash
python app.py
```

The first run may take time because the model and tokenizer are downloaded from Hugging Face.

> **Note:** The repository code loads the model onto `cuda` at startup and wraps inference with `spaces.GPU`. Running it outside Hugging Face Spaces may require adapting the GPU decorator and model device configuration for your local environment.

## Responsible use and limitations

- The model can misunderstand image content or produce inaccurate descriptions.
- Descriptions are based on visible image content and should not be treated as verified facts.
- Avoid using generated descriptions as the sole basis for important decisions.
- Performance depends on the available GPU, image complexity, and model-loading time.

## License

No license has been specified for this repository yet.