# AI-SkinExpert

Voice + image skin consultation demo (Gradio).

## Layout

- `app/` — pipeline + doctor services
- `app/ui/` — Gradio layout, markup, soft-clinical CSS
- `samples/` — demo media
- `main.py` — entrypoint

## Run

```bash
uv run python main.py
```

Requires `GROQ_API_KEY` and `DEEPGRAM_API_KEY` in `.env`.
