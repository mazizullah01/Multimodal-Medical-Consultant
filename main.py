
# play audio for the Patient

iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone", "upload"], type="filepath", label="Patient Voice"),
        gr.Image(type="filepath", label="Patient Image"),
        gr.Video(label="Patient Video"),         
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio(label="Doctor Voice"),
    ],
    title="AI Skin Specialist with Vision and voice",
)
