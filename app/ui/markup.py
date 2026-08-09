"""HTML fragments for the consultation UI."""

HEADER_HTML = """
<header class="top-header">
  <div class="header-brand">
    <div class="brand-logo" aria-label="AI Skin Specialist logo">
      <svg viewBox="0 0 32 32" fill="none" aria-hidden="true">
        <path d="M16 3.5 26 7v8.2c0 6.4-4 11.1-10 13.3-6-2.2-10-6.9-10-13.3V7l10-3.5Z" stroke="currentColor" stroke-width="2.4"/>
        <path d="M16 10v11M10.5 15.5h11" stroke="currentColor" stroke-width="2.8" stroke-linecap="round"/>
      </svg>
    </div>
    <div class="brand-copy"><strong>AI Skin</strong><span>SPECIALIST</span></div>
  </div>
  <div class="page-title">
    <strong>Consultation Assistant</strong>
    <span>Voice, Image, and Video Based Analysis</span>
  </div>
  <div class="privacy-pill">♢ &nbsp; Privacy-first consultation</div>
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

INPUTS_INTRO_HTML = """
<div class="inputs-intro">
  <div class="inputs-intro-copy">
    <strong>Your consultation inputs</strong>
    <span>Record your concern, add a clear skin photo, and optionally attach a short video.</span>
  </div>
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
  <p class="response-sub">Specialist guidance appears here after you analyze your inputs.</p>
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
  <span>Your consultation summary, transcript, and guidance will appear here after analysis.</span>
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

VOICE_FIELD_HTML = """
<div class="tile-heading">
  <span class="tile-title">Voice</span>
  <em class="tile-badge required">Required</em>
</div>
<p class="tile-hint">Describe your skin concern in a short voice note.</p>
"""

IMAGE_FIELD_HTML = """
<div class="tile-heading">
  <span class="tile-title">Photo</span>
  <em class="tile-badge recommended">Recommended</em>
</div>
<p class="tile-hint">Upload a clear photo of the affected skin area.</p>
"""

VIDEO_FIELD_HTML = """
<div class="tile-heading">
  <span class="tile-title">Video</span>
  <em class="tile-badge optional">Optional</em>
</div>
<p class="tile-hint">Add a short clip if it helps show the concern.</p>
"""
