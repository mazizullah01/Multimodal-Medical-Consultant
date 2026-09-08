from app.pipeline import clear_consultation, process_inputs
from app.ui import build_app

app = build_app(
    process_inputs=process_inputs,
    clear_consultation=clear_consultation,
)

if __name__ == "__main__":
    app.queue().launch()
