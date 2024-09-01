from src.services.predict.tf_predict import tf_predict
from typing import Any

from src.services.predict.torch_predic import torch_preprocess, torch_predict
from src.utils import load_image


def torch_run_classifier(image: str) -> Any:
    img = load_image(image)
    if img is None:
        return None
    input_batch = torch_preprocess(img)
    top_labels = torch_predict(input_batch, model=None)
    return top_labels[0]


def tf_run_classifier(image: str) -> Any:
    img = load_image(image)
    if img is None:
        return None
    pred_results = tf_predict(img)

    return pred_results
