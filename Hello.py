# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
LOGGER = get_logger(__name__)

import requests


def gen_illusion(prompt):
    
  url = "https://54285744-illusion-diffusion.gateway.alpha.fal.ai/"

  API_KEY = "key " + st.secrets["API_KEY"]

  PROMPT = f"(masterpiece:1.4), (best quality), (detailed), BREAK {prompt}."

  LOGGER.info(PROMPT)

  payload = {
      "image_url": "https://storage.googleapis.com/llm-sandbox/Charte_Graphique_TheField_white.jpg",
      "prompt": PROMPT,
      "negative_prompt" : "(worst quality, poor details:1.4), lowres, (artist name, signature, watermark:1.4), bad-artist-anime, bad_prompt_version2, bad-hands-5, ng_deepnegative_v1_75t",
      "guidance_scale": 7.5,
      "controlnet_conditioning_scale": 1,
      "control_guidance_start": 0,
      "control_guidance_end": 1,
      "seed": 65423178,
      "scheduler": "Euler",
      "num_inference_steps": 40
  }
  headers = {
      "Authorization": API_KEY,
      "Content-Type": "application/json"
  }

  response = requests.post(url, json=payload, headers=headers)
  image = response.json()
  LOGGER.info(image)
  return image["image"]["url"]


def run():
    st.set_page_config(
        page_title="Illusion Diffusion - The field",
        page_icon="👋",
    )

    st.write("# Illusion Diffusion - The field")

    prompt_input = st.text_input('Prompt', placeholder='A New York city scene with buildings in the distance')
    result = gen_illusion(prompt_input)

    if prompt_input:
      st.image(result)


if __name__ == "__main__":
    run()
