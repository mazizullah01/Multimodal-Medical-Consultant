import gradio as gr

from voice_of_the_patient import transcribe_patient_voice
from brain_of_doc_groq  import brain_of_the_doctor
from voice_of_the_doc import convert_text_to_doctor_audio, play_audio

# Logic + UI

def process_inputs(audio_filepath, image_filepath, video_filepath):

    # User  will ask question in audio and this audio will be convertes to text
    patient_text = transcribe_patient_voice(audio_filepath)

    # This text + users image/vedio will be sent to brain of the doctor and brain of the doctor  will respond in text
    doctor_text = brain_of_the_doctor(
        patient_text=patient_text,
        image_filepath=image_filepath,
        vedio_filepath=video_filepath,
    )
    # We will convert this text responce from the doctor to audio responce
    doctor_audio = convert_text_to_doctor_audio(doctor_text)

    # play audio for the Patient
    play_audio(doctor_audio)
    return patient_text, doctor_text, str(doctor_audio)

