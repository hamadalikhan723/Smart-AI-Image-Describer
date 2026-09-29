import spaces
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image

MODEL_ID = "vikhyatk/moondream2"
REVISION = "2024-08-26"  # pinned so encode_image/answer_question keep working

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_ID, revision=REVISION, trust_remote_code=True
)

# On ZeroGPU, loading onto "cuda" at startup is the expected pattern
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    revision=REVISION,
    trust_remote_code=True,
    torch_dtype=torch.float16,
).to("cuda").eval()

PROMPT = (
    "Describe this image in 5 to 6 clear sentences: the main subjects, "
    "their actions, important objects, and surroundings. "
    "Only describe what is visibly present."
)


@spaces.GPU(duration=20)  # GPU is attached only while this function runs
def generate_caption(image: Image.Image):
    image = image.convert("RGB")
    image.thumbnail((768, 768))  # smaller image = faster encoding

    with torch.inference_mode():
        embeds = model.encode_image(image)
        text = model.answer_question(
            embeds, PROMPT, tokenizer, max_new_tokens=150
        )
    return text.strip()