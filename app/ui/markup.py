"""HTML fragments for the consultation UI."""

SIDEBAR_HTML = """
<div class="side-brand">
  <div class="brand-logo" aria-label="AI Skin Specialist logo">
    <svg viewBox="0 0 32 32" fill="none" aria-hidden="true">
      <path d="M16 3.5 26 7v8.2c0 6.4-4 11.1-10 13.3-6-2.2-10-6.9-10-13.3V7l10-3.5Z" stroke="currentColor" stroke-width="2.4"/>
      <path d="M16 10v11M10.5 15.5h11" stroke="currentColor" stroke-width="2.8" stroke-linecap="round"/>
    </svg>
  </div>
  <div class="brand-copy"><strong>AI Skin</strong><span>SPECIALIST</span></div>
</div>
<div class="nav-item active" aria-current="page"><span class="nav-icon">▦</span>Consultation Hub</div>
<div class="support-box"><b>SUPPORT</b>Clinical assistance available<br>24/7 for specialists.</div>
"""

HEADER_HTML = """
<header class="top-header">
  <div class="page-title">
    <strong>Consultation Assistant</strong>
    <span>Voice, Image, and Video Based Analysis</span>
  </div>
  <div class="privacy-pill">♢ &nbsp; Privacy-first consultation</div>
  <div class="doctor">
    <div><strong>Dr. Specialist</strong><span>Dermatologist</span></div>
    <div class="doctor-avatar" role="img" aria-label="Dr. Specialist profile image">
      <svg viewBox="0 0 54 54" fill="none" aria-hidden="true">
        <rect width="54" height="54" fill="#dceef9"/>
        <circle cx="27" cy="20" r="9" fill="#f2c9ad"/>
        <path d="M17.5 18.5c.8-8.4 18-10 19.3.7-4.1-1.1-8.8-3.5-12.8-1.3-2.2 1.2-3.2 2-6.5.6Z" fill="#425b6b"/>
        <path d="M11 54c.8-12 6.6-18 16-18s15.2 6 16 18H11Z" fill="#fff"/>
        <path d="m22 36 5 8 5-8M27 44v10" stroke="#1494e8" stroke-width="2"/>
      </svg>
    </div>
  </div>
</header>
"""

STEPS_IDLE_HTML = """
<ol class="steps-strip" aria-label="Consultation steps">
  <li class="step-chip active"><span class="n">1</span>Record voice</li>
  <li class="step-chip"><span class="n">2</span>Add photo</li>
  <li class="step-chip"><span class="n">3</span>Analyze</li>
  <li class="step-chip"><span class="n">4</span>Results</li>
</ol>
"""

STEPS_DONE_HTML = """
<ol class="steps-strip" aria-label="Consultation steps">
  <li class="step-chip done"><span class="n">✓</span>Record voice</li>
  <li class="step-chip done"><span class="n">✓</span>Add photo</li>
  <li class="step-chip done"><span class="n">✓</span>Analyze</li>
  <li class="step-chip done active"><span class="n">4</span>Results</li>
</ol>
"""

PATIENT_CARD_HEAD_HTML = """
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
"""

RESPONSE_CARD_HEAD_HTML = """
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
"""

EMPTY_STATUS_HTML = """
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
"""

SUCCESS_STATUS_HTML = """
<div class="success-banner">
  <span class="success-icon">✓</span>
  <div>
    <strong>Analysis complete</strong>
    <span>Your private consultation is ready below.</span>
  </div>
</div>
"""

DISCLAIMER_HTML = (
    '<div class="disclaimer">AI-generated educational guidance is not a medical diagnosis. '
    "Seek urgent care for rapidly worsening, painful, bleeding, or otherwise concerning symptoms.</div>"
)

VOICE_FIELD_HTML = (
    '<div class="field-heading">Describe your skin concern <span>♩ &nbsp; Patient Voice</span></div>'
)

IMAGE_FIELD_HTML = (
    '<div class="field-heading">Skin Image <em>RECOMMENDED</em></div>'
)

VIDEO_FIELD_HTML = '<div class="field-heading">Skin Video</div>'
