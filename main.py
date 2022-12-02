from zipfile import ZipFile
import pandas

import gradio as gr
import pandas as pd


def zip_to_json(file_obj):
    df = pd.read_csv(file_obj.name, sep=';')
    print(df.head())
    return "Il nome del file: " + file_obj.name


demo = gr.Interface(fn=zip_to_json,
                    inputs="file",
                    outputs="text")

if __name__ == "__main__":
    demo.launch()