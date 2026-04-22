# app.py
# Streamlit web UI — the only file the user directly runs.
# It handles upload, input, display, and delegates all logic to the agent.

import json
import streamlit as st
from agent.agent import run_from_bytes

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Multimodal Agent",
    page_icon="🧠",
    layout="wide",
)

# ── Custom CSS for a clean dark look ───────────────────────────────────────────
st.markdown("""
<style>
    /* Dark background */
    .stApp { background-color: #0e1117; }

    /* Section headers */
    h1 { color: #ffffff; font-size: 1.8rem !important; }
    h3 { color: #a0aec0; font-size: 1rem !important; font-weight: 500; }

    /* JSON output block */
    .json-box {
        background: #1a1f2e;
        border: 1px solid #2d3748;
        border-radius: 8px;
        padding: 1.2rem 1.5rem;
        font-family: 'Courier New', monospace;
        font-size: 0.85rem;
        color: #68d391;
        white-space: pre-wrap;
        overflow-x: auto;
    }

    /* Status badge */
    .badge-done {
        background: #276749;
        color: #c6f6d5;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 0.8rem;
    }
    .badge-error {
        background: #742a2a;
        color: #fed7d7;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

# ── Header ─────────────────────────────────────────────────────────────────────
st.title("🧠 Multimodal Agent")
st.caption("Upload any image. Ask anything. Get structured output.")

# ── Two-column layout ──────────────────────────────────────────────────────────
col_input, col_output = st.columns(2, gap="large")

with col_input:
    st.subheader("Input")

    uploaded_file = st.file_uploader(
        "Upload an image",
        type=["jpg", "jpeg", "png", "webp", "gif"],
        label_visibility="collapsed",
    )

    if uploaded_file:
        st.image(uploaded_file, use_container_width=True)

    instruction = st.text_area(
        "What do you want to know?",
        placeholder='e.g. "am I overspending on food?" or "summarize this meeting"',
        height=100,
    )

    context = st.text_area(
        "Additional context (optional)",
        placeholder='e.g. "my monthly budget is ₹5000" or "this is a sprint planning board"',
        height=80,
    )

    run_btn = st.button("▶ Analyze", type="primary", use_container_width=True)

# ── Output column ──────────────────────────────────────────────────────────────
with col_output:
    st.subheader("Output")

    if run_btn:
        # Validation
        if not uploaded_file:
            st.warning("Please upload an image first.")
        elif not instruction.strip():
            st.warning("Please enter a question or instruction.")
        else:
            with st.spinner("Analyzing…"):
                try:
                    result = run_from_bytes(
                        image_bytes=uploaded_file.getvalue(),
                        filename=uploaded_file.name,
                        instruction=instruction.strip(),
                        context=context.strip(),
                    )

                    # Check if the agent returned an error dict
                    if "error" in result:
                        st.markdown('<div class="badge-error">Error</div>', unsafe_allow_html=True)
                        st.error(result.get("error"))
                        if "raw_output" in result:
                            st.text(result["raw_output"])
                    else:
                        st.markdown('<div class="badge-done">Done!</div>', unsafe_allow_html=True)

                        # Pretty-printed JSON display
                        pretty = json.dumps(result, indent=2, ensure_ascii=False)
                        st.markdown(
                            f'<div class="json-box">{pretty}</div>',
                            unsafe_allow_html=True,
                        )

                        # Raw JSON expander for copy-paste
                        with st.expander("▶ Raw JSON (copy-paste ready)"):
                            st.code(pretty, language="json")

                except ValueError as e:
                    st.error(f"Image error: {e}")
                except Exception as e:
                    st.error(f"Unexpected error: {e}")
    else:
        # Placeholder state
        st.markdown("""
        <div style="color:#4a5568; text-align:center; margin-top:4rem; font-size:0.95rem;">
            Upload an image and ask a question<br>to see structured output here.
        </div>
        """, unsafe_allow_html=True)