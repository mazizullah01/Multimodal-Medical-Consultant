"""Gradio dashboard for the AI Skin Specialist."""

import gradio as gr

from app.doctor_brain import brain_of_the_doctor
from app.doctor_voice import convert_text_to_doctor_audio
from app.patient_voice import transcribe_patient_voice


def process_inputs(audio_filepath, image_filepath, video_filepath, progress=gr.Progress()):
    """Transcribe the concern, review the image, and create the voice response."""
    if not audio_filepath:
        raise gr.Error("Please record or upload a short voice note describing your concern.")
    if not image_filepath:
        raise gr.Error("Please upload a clear photo of the affected skin area.")

    try:
        progress(0.15, desc="Transcribing your voice note")
        patient_text = transcribe_patient_voice(audio_filepath)

        progress(0.5, desc="Reviewing your skin photo")
        doctor_text = brain_of_the_doctor(
            patient_text=patient_text,
            image_filepath=image_filepath,
            video_filepath=video_filepath,
        )

        progress(0.82, desc="Preparing your audio response")
        doctor_audio = convert_text_to_doctor_audio(doctor_text)
        progress(1, desc="Consultation ready")
    except Exception as exc:
        raise gr.Error(f"We couldn't complete the consultation: {exc}") from exc

    status = """
    <div class="success-banner">
        <span class="success-icon">✓</span>
        <div><strong>Analysis complete</strong><span>Your private consultation is ready below.</span></div>
    </div>
    """
    return patient_text, doctor_text, str(doctor_audio), status


def clear_consultation():
    """Reset all consultation fields."""
    return None, None, None, "", "", None, ""


CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
:root { color-scheme: light; --app-blue:#1494e8; --app-blue-dark:#0878bd; --app-ink:#17202b; --app-muted:#63717e; --app-line:#e2e8ee; --app-wash:#f5f8fb; }
* { box-sizing:border-box; }
body, .gradio-container { margin:0 !important; background:#fff !important; color:var(--app-ink) !important; }
.gradio-container, .dark .gradio-container {
  color-scheme:light !important; max-width:none !important; padding:0 !important; font-family:'Inter',sans-serif !important;
  --body-background-fill:#fff; --body-text-color:var(--app-ink); --block-background-fill:#fff;
  --block-border-color:var(--app-line); --block-label-background-fill:#fff; --block-label-text-color:#536470;
  --input-background-fill:#f8fafc; --input-border-color:var(--app-line); --input-placeholder-color:#9aa6af;
}
.app-layout { display:grid !important; grid-template-columns:304px minmax(0,1fr); gap:0 !important; min-height:100vh; align-items:stretch !important; }
.sidebar { background:#fff !important; border:0 !important; border-right:1px solid var(--app-line) !important; min-width:304px !important; padding:26px 16px 22px !important; }
.side-brand { display:flex; align-items:center; gap:14px; padding:0 10px 54px; }
.brand-logo { width:54px;height:54px;background:#e8f4fc;border-radius:12px;display:grid;place-items:center;color:#0878bd; }.brand-logo svg{width:32px;height:32px}
.brand-copy strong { display:block;color:#086fb2;font-size:16px;font-weight:600; }.brand-copy span { color:#5d6871;font-size:11px;font-weight:700;letter-spacing:.11em; }
.nav-item { height:59px;display:flex;align-items:center;gap:21px;padding:0 26px;border-radius:12px;color:#46515d;font-size:16px;margin:3px 0; }
.nav-icon { width:25px;text-align:center;font-size:22px;color:#657783; }.nav-item.active { background:#2899e9;color:#102b3c;font-weight:600; }.nav-item.active .nav-icon { color:#006ea9; }
.support-box { margin:calc(100vh - 560px) 9px 0;background:#f3f7fb;border:1px solid #dde6ee;border-radius:12px;padding:25px 26px;color:#71808c;font-size:13px;line-height:1.5; }
.support-box b { display:block;font-size:11px;color:#5e6c78;margin-bottom:7px; }
.main-area { min-width:0 !important; background:var(--app-wash) !important; padding:0 !important; gap:0 !important; }
.top-header { height:84px;background:#fff;display:grid;grid-template-columns:1fr auto auto;align-items:center;padding:0 55px;border-bottom:1px solid #edf1f4;gap:33px; }
.page-title strong { display:block;font-size:16px;font-weight:500; }.page-title span { font-size:13px;color:#4f5b67; }
.privacy-pill { background:#eef5ff;border:1px solid #c8ddfa;border-radius:22px;color:#1d467d;font-size:12px;font-weight:600;padding:12px 23px; }
.doctor { border-left:1px solid #d8e0e7;padding-left:30px;display:flex;align-items:center;gap:15px;text-align:right; }.doctor strong{display:block;font-size:13px}.doctor span{font-size:11px;color:#687580}.doctor-avatar{width:54px;height:54px;background:#dceef9;border-radius:50%;display:grid;place-items:center;overflow:hidden}.doctor-avatar svg{width:54px;height:54px}
.workspace { padding:68px 55px 52px !important; max-width:1010px; width:100%; margin:0 auto; }
.consult-grid { display:grid !important;grid-template-columns:minmax(390px,1fr) minmax(390px,1fr);gap:24px !important;align-items:stretch !important; }
.consult-card { background:#fff !important;border:1px solid var(--app-line) !important;border-radius:12px !important;overflow:hidden;min-height:850px;box-shadow:none !important;gap:0 !important; }
.card-head { background:#f7f9fb;border-bottom:1px solid var(--app-line);padding:42px 43px 38px;min-height:174px; }.response-head{background:#f1f3ff}.card-title{display:flex;align-items:center;gap:24px;font-size:17px;font-weight:500}.title-icon{width:43px;height:43px;flex:0 0 43px;border-radius:10px;background:#e4f0fa;color:#0878bd;display:grid;place-items:center;font-size:22px}.title-icon svg{width:25px;height:25px;display:block}.response-head .title-icon{background:#e1e8fc;color:#316fd1}.card-head p{margin:10px 0 0;color:#495765;font-size:13px;line-height:1.45}.ready-dot{display:block;margin:10px 0 0;color:#4b5965;font-size:13px}.ready-dot:before{content:'●';color:#4878d5;margin-right:11px}
.input-body { padding:38px 43px 28px !important; gap:0 !important; }.field-heading{font-size:15px;font-weight:500;margin:0 0 16px}.field-heading span{float:right;color:#657680;font-size:11px;font-weight:600}.field-heading em{font-style:normal;background:#e5f2ff;color:#0879be;font-size:9px;font-weight:700;border-radius:10px;padding:4px 8px;margin-left:7px}
.voice-recorder { min-height:112px !important;border:1px solid #e2e8ee !important;border-radius:10px !important;background:#f6f8fa !important;margin-bottom:42px !important;overflow:hidden; }
.voice-recorder .label-wrap,.voice-recorder .block-info { display:none !important; }
.voice-recorder button { box-shadow:none !important; }
.voice-recorder wave { min-height:92px !important; }
.upload-media { position:relative !important;height:190px !important;border:2px dashed #acd5f2 !important;border-radius:11px !important;background:#fbfcfd !important;margin-bottom:39px !important;overflow:hidden}
.video-media{height:152px !important;border-color:#e1e8ee !important;margin-bottom:12px !important}
.upload-media .label-wrap,.upload-media .block-info{display:none !important}
.upload-media button{cursor:pointer !important}
.gradio-container .block,.gradio-container .form{color:var(--app-ink) !important}.gradio-container label,.gradio-container textarea{color:var(--app-ink) !important}
.actions { padding:22px 43px 30px !important;background:#f8fafc;border-top:1px solid var(--app-line);gap:10px !important;margin-top:auto !important}.analyze-btn{background:#087dbf !important;color:#fff !important;border:0 !important;border-radius:10px !important;min-height:50px;font-weight:600 !important}.clear-btn{background:#fff !important;color:#647480 !important;border:1px solid #dbe3e9 !important;border-radius:10px !important;min-height:44px}
.result-body{padding:0 43px 32px !important;gap:13px !important}.result-empty{height:900px;display:flex;align-items:center;justify-content:center;text-align:center;color:#404c58}.result-icon{position:relative;width:156px;height:156px;border:2px solid #c2def1;border-radius:50%;display:grid;place-items:center;margin:0 auto 34px;color:#087cbc;box-shadow:inset 0 0 0 19px #fff;background:#e9edf0}.result-icon:after{content:'';position:absolute;inset:-3px;border-radius:50%;border:3px solid transparent;border-top-color:#69add7;border-right-color:#69add7;transform:rotate(-32deg)}.result-icon svg{width:54px;height:54px;display:block}.result-empty strong{display:block;font-size:15px;margin-bottom:23px}.result-empty span{display:block;max-width:285px;font-size:17px;line-height:1.45;color:#4e5966}.output-box{margin:0 0 4px !important}.output-box textarea{line-height:1.5 !important;font-size:13px !important}.output-box label span{font-size:12px !important;font-weight:600 !important;color:#52616d !important}.audio-output{margin-top:2px !important}.disclaimer{font-size:10px;line-height:1.45;color:#78858f;margin-top:8px}.success-banner{background:#edf8f4;border:1px solid #cce9dd;border-radius:9px;color:#24634e;padding:11px 13px;font-size:12px}.success-banner .success-icon{margin-right:7px}.success-banner div,.success-banner span{display:inline}.success-banner div span{margin-left:7px}
.result-body:has(.result-empty) .output-box,.result-body:has(.result-empty) .disclaimer{display:none !important}
footer{display:none !important}
@media(max-width:900px){.app-layout{grid-template-columns:1fr}.sidebar{display:none !important}.top-header{padding:0 20px;grid-template-columns:1fr auto}.doctor{display:none}.workspace{padding:25px 16px !important}.consult-grid{grid-template-columns:1fr}.consult-card{min-height:auto}}
"""


with gr.Blocks(css=CSS, title="AI Skin Specialist") as app:
    with gr.Row(elem_classes="app-layout"):
        with gr.Column(elem_classes="sidebar", scale=0):
            gr.HTML("""
            <div class="side-brand">
              <div class="brand-logo" aria-label="AI Skin Specialist logo">
                <svg viewBox="0 0 32 32" fill="none" aria-hidden="true"><path d="M16 3.5 26 7v8.2c0 6.4-4 11.1-10 13.3-6-2.2-10-6.9-10-13.3V7l10-3.5Z" stroke="currentColor" stroke-width="2.4"/><path d="M16 10v11M10.5 15.5h11" stroke="currentColor" stroke-width="2.8" stroke-linecap="round"/></svg>
              </div>
              <div class="brand-copy"><strong>AI Skin</strong><span>SPECIALIST</span></div>
            </div>
            <div class="nav-item active" aria-current="page"><span class="nav-icon">▦</span>Consultation Hub</div>
            <div class="support-box"><b>SUPPORT</b>Clinical assistance available<br>24/7 for specialists.</div>
            """)
        with gr.Column(elem_classes="main-area"):
            gr.HTML("""
            <header class="top-header">
              <div class="page-title"><strong>Consultation Assistant</strong><span>Voice, Image, and Video Based Analysis</span></div>
              <div class="privacy-pill">♢ &nbsp; Privacy-first consultation</div>
              <div class="doctor">
                <div><strong>Dr. Specialist</strong><span>Dermatologist</span></div>
                <div class="doctor-avatar" role="img" aria-label="Dr. Specialist profile image">
                  <svg viewBox="0 0 54 54" fill="none" aria-hidden="true"><rect width="54" height="54" fill="#dceef9"/><circle cx="27" cy="20" r="9" fill="#f2c9ad"/><path d="M17.5 18.5c.8-8.4 18-10 19.3.7-4.1-1.1-8.8-3.5-12.8-1.3-2.2 1.2-3.2 2-6.5.6Z" fill="#425b6b"/><path d="M11 54c.8-12 6.6-18 16-18s15.2 6 16 18H11Z" fill="#fff"/><path d="m22 36 5 8 5-8M27 44v10" stroke="#1494e8" stroke-width="2"/></svg>
                </div>
              </div>
            </header>
            """)
            with gr.Column(elem_classes="workspace"):
                with gr.Row(elem_classes="consult-grid"):
                    with gr.Column(elem_classes="consult-card"):
                        gr.HTML("""
                        <div class="card-head">
                          <div class="card-title">
                            <span class="title-icon">
                              <svg viewBox="0 0 32 32" fill="none" aria-hidden="true">
                                <rect x="4" y="3" width="20" height="25" rx="2" stroke="currentColor" stroke-width="2.6"/>
                                <path d="M9 9h10M9 14h7" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>
                                <circle cx="23" cy="20" r="4" fill="#e4f0fa" stroke="currentColor" stroke-width="2.4"/>
                                <path d="M16.5 29c.5-3.5 3-5.5 6.5-5.5s6 2 6.5 5.5" fill="#e4f0fa" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>
                              </svg>
                            </span>
                            Patient Input
                          </div>
                          <p>Provide voice, image, or video for comprehensive<br>analysis.</p>
                        </div>
                        """)
                        with gr.Column(elem_classes="input-body"):
                            gr.HTML('<div class="field-heading">Describe your skin concern <span>♩ &nbsp; Patient Voice</span></div>')
                            patient_audio = gr.Audio(
                                sources=["microphone"],
                                type="filepath",
                                label="Patient Voice",
                                waveform_options=gr.WaveformOptions(
                                    waveform_color="#a9d7f1",
                                    waveform_progress_color="#087dbf",
                                    show_recording_waveform=True,
                                    show_controls=False,
                                ),
                                elem_classes="voice-recorder",
                            )
                            gr.HTML('<div class="field-heading">Skin Image <em>RECOMMENDED</em></div>')
                            patient_image = gr.Image(type="filepath", label="Skin Image", elem_classes="upload-media")
                            gr.HTML('<div class="field-heading">Skin Video</div>')
                            patient_video = gr.Video(label="Skin Video", elem_classes=["upload-media", "video-media"])
                        with gr.Column(elem_classes="actions"):
                            analyze_btn = gr.Button("Analyze Consultation", variant="primary", elem_classes="analyze-btn")
                            clear_btn = gr.Button("Clear", elem_classes="clear-btn")
                    with gr.Column(elem_classes="consult-card"):
                        gr.HTML("""
                        <div class="card-head response-head">
                          <div class="card-title">
                            <span class="title-icon">
                              <svg viewBox="0 0 32 32" fill="none" aria-hidden="true">
                                <path d="M16 3.5 26 7v8.2c0 6.4-4 11.1-10 13.3-6-2.2-10-6.9-10-13.3V7l10-3.5Z" stroke="currentColor" stroke-width="2.7" stroke-linejoin="round"/>
                                <path d="M16 10v11M10.5 15.5h11" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>
                              </svg>
                            </span>
                            Doctor Response
                          </div>
                          <span class="ready-dot">AI Assistant Ready</span>
                        </div>
                        """)
                        with gr.Column(elem_classes="result-body"):
                            status = gr.HTML("""
                            <div class="result-empty"><div>
                              <div class="result-icon">
                                <svg viewBox="0 0 64 64" fill="none" aria-hidden="true">
                                  <path d="M23 18v-5c0-3 2-5 5-5h8c3 0 5 2 5 5v5" stroke="currentColor" stroke-width="4"/>
                                  <rect x="9" y="18" width="46" height="36" rx="4" stroke="currentColor" stroke-width="4"/>
                                  <path d="M32 26v20M22 36h20" stroke="currentColor" stroke-width="5" stroke-linecap="round"/>
                                </svg>
                              </div>
                              <strong>Ready for Analysis</strong>
                              <span>Your consultation summary,<br>transcript, and guidance will<br>appear below after analysis.</span>
                            </div></div>
                            """)
                            transcript = gr.Textbox(label="Patient transcript", lines=2, interactive=False, elem_classes="output-box")
                            response = gr.Textbox(label="Specialist guidance", lines=6, interactive=False, elem_classes="output-box")
                            doctor_audio = gr.Audio(label="Doctor voice response", interactive=False, elem_classes=["output-box", "audio-output"])
                            gr.HTML('<div class="disclaimer">AI-generated educational guidance is not a medical diagnosis. Seek urgent care for rapidly worsening, painful, bleeding, or otherwise concerning symptoms.</div>')

    analyze_btn.click(
        fn=process_inputs,
        inputs=[patient_audio, patient_image, patient_video],
        outputs=[transcript, response, doctor_audio, status],
    )
    clear_btn.click(
        fn=clear_consultation,
        inputs=[],
        outputs=[patient_audio, patient_image, patient_video, transcript, response, doctor_audio, status],
        queue=False,
    )


if __name__ == "__main__":
    app.queue().launch()
