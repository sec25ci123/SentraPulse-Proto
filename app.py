import streamlit as st
from ultralytics import YOLO
from PIL import Image
import tempfile
import os

st.set_page_config(
    page_title="SentraPulse",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ SentraPulse")
st.subheader("AI-Based Crowd Density & Risk Monitoring")
st.caption("Prototype | Camera-image analysis")

@st.cache_resource
def load_model():
    return YOLO("yolo26n.pt")

uploaded_file = st.file_uploader(
    "Upload a crowd image",
    type=["jpg", "jpeg", "png"]
)

st.info("Upload an image to analyze the people visible in it.")

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded camera image",
             use_container_width=True)

    if st.button("Analyze Crowd", type="primary"):
        with st.spinner("Detecting people..."):
            model = load_model()
            with tempfile.NamedTemporaryFile(
                suffix=".jpg", delete=False
            ) as temp:
                image.save(temp.name)
                image_path = temp.name

            try:
                result = model(
		  image_path,
		  conf=0.10,
		  iou=0.45,
		  imgsz=1280,
		  verbose=False
		)[0]
                boxes = result.boxes
                person_count = sum(
                    int(c) == 0 for c in boxes.cls.tolist()
                )

                annotated = result.plot()
                annotated = Image.fromarray(
                    annotated[:, :, ::-1]
                )

                # Illustrative thresholds for this demo
                if person_count < 5:
                    level = "LOW"
                    message = "Normal monitoring"
                elif person_count < 15:
                    level = "MODERATE"
                    message = "Monitor crowd movement"
                else:
                    level = "HIGH"
                    message = "Review area and assess safety"

                st.divider()
                col1, col2, col3 = st.columns(3)
                col1.metric("People Detected", person_count)
                col2.metric("Density Category", level)
                col3.metric("System Status", "Analyzed")

                st.subheader("Monitoring Alert")
                if level == "HIGH":
                    st.error("⚠️ " + message)
                elif level == "MODERATE":
                    st.warning("🟡 " + message)
                else:
                    st.success("🟢 " + message)

                st.subheader("AI Detection Results")
                st.image(
                    annotated,
                    caption="Detected people highlighted by AI",
                    use_container_width=True
                )

                st.caption(
                    "Demo thresholds only. A single image does not "
                    "measure actual area-based crowd density or predict "
                    "future risks. Detection may miss people."
                )
            finally:
                os.remove(image_path)
