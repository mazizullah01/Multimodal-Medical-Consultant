import gradio as gr

from voice_of_the_patient import transcribe_patient_voice
from brain_of_doc_groq  import brain_of_the_doctor
from voice_of_the_doc import convert_text_to_doctor_audio, play_audio

# Logic + UI

def process_inputs(audio_filepath, image_filepath, video_filepath):

    # User  will ask question in audio and this audio will be convertes to text
    patient_text = transcribe_patient_voice(audio_filepath)

