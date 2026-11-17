import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import json
import os

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AgriWise AI — Futuristic Crop Intelligence",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- FUTURISTIC SAAS DESIGN SYSTEM ----------------

st.markdown("""
<style>
/* ── Color Palette & Base Variables ── */
:root {
    --bg-main: #07140F;
    --sidebar-bg: #0D2118;
    --card-bg: #112B1E;
    --elevated-bg: #183927;
    --primary-emerald: #22C55E;
    --bright-lime: #A3E635;
    --mint-accent: #86EFAC;
    --text-primary: #F8FAFC;
    --text-secondary: #B8C9BD;
    --border-color: #28543A;
}

/* ── Global Styles ── */
.stApp {
    background-color: var(--bg-main);
    color: var(--text-primary);
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* ── Sidebar Styling ── */
section[data-testid="stSidebar"] {
    background-color: var(--sidebar-bg);
    border-right: 1px solid var(--border-color);
}
section[data-testid="stSidebar"] .stMarkdown,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] p {
    color: var(--text-primary) !important;
}

/* Radio navigation styling */
div[data-testid="stRadio"] label {
    background: transparent;
    border-radius: 10px;
    padding: 8px 12px;
    margin-bottom: 4px;
    transition: background 0.2s, border-color 0.2s;
    border: 1px solid transparent;
}
div[data-testid="stRadio"] label:hover {
    background: rgba(34, 197, 94, 0.08);
    border-color: var(--border-color);
}

/* ── Container Layout ── */
.block-container {
    padding-top: 2rem;
    padding-bottom: 4rem;
    max-width: 1240px;
}

/* ── Hero Banner ── */
.hero-banner {
    position: relative;
    border-radius: 24px;
    overflow: hidden;
    margin-bottom: 30px;
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.5), inset 0 0 0 1px var(--border-color);
    min-height: 300px;
    display: flex;
    align-items: center;
    background: var(--card-bg);
}
.hero-banner img {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    object-fit: cover;
    filter: brightness(0.35) contrast(1.1);
}
.hero-overlay {
    position: relative;
    z-index: 2;
    padding: 3.5rem 4rem;
    max-width: 800px;
}
.hero-badge {
    display: inline-block;
    background: rgba(34, 197, 94, 0.15);
    border: 1px solid var(--primary-emerald);
    color: var(--mint-accent) !important;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 6px 16px;
    border-radius: 30px;
    margin-bottom: 14px;
    box-shadow: 0 0 15px rgba(34, 197, 94, 0.2);
}
.hero-title {
    color: var(--text-primary) !important;
    font-size: 2.8rem;
    font-weight: 800;
    line-height: 1.15;
    margin: 0 0 0.8rem 0;
    letter-spacing: -0.5px;
}
.hero-sub {
    color: var(--text-secondary) !important;
    font-size: 1.1rem;
    font-weight: 400;
    margin: 0;
    line-height: 1.6;
}

/* ── Metric Cards ── */
.metric-card {
    background: var(--card-bg);
    border: 1px solid var(--border-color);
    border-radius: 18px;
    padding: 24px;
    display: flex;
    align-items: center;
    gap: 20px;
    height: 100%;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
    transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
}
.metric-card:hover {
    border-color: var(--primary-emerald);
    transform: translateY(-3px);
    box-shadow: 0 12px 30px rgba(34, 197, 94, 0.15);
}
.metric-icon {
    font-size: 2.2rem;
    width: 58px;
    height: 58px;
    background: var(--elevated-bg);
    border: 1px solid var(--border-color);
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}
.metric-label {
    color: var(--text-secondary) !important;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    margin-bottom: 6px;
}
.metric-value {
    color: var(--text-primary) !important;
    font-size: 1.7rem;
    font-weight: 800;
    line-height: 1.1;
}
.metric-sub {
    color: var(--mint-accent) !important;
    font-size: 11px;
    margin-top: 4px;
    font-weight: 500;
}

/* ── Step Cards ── */
.step-card {
    background: var(--card-bg);
    border: 1px solid var(--border-color);
    border-radius: 18px;
    padding: 28px 24px;
    height: 100%;
    position: relative;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
    overflow: hidden;
}
.step-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, var(--primary-emerald), var(--bright-lime));
}
.step-num {
    color: var(--bright-lime) !important;
    font-size: 2.2rem;
    font-weight: 800;
    line-height: 1;
}
.step-title {
    color: var(--text-primary) !important;
    font-size: 1.15rem;
    font-weight: 700;
    margin: 12px 0 8px;
}
.step-desc {
    color: var(--text-secondary) !important;
    font-size: 0.92rem;
    line-height: 1.6;
}

/* ── Result Card ── */
.result-card {
    background: linear-gradient(135deg, #0D2118 0%, #163827 50%, #112B1E 100%);
    border: 1px solid var(--primary-emerald);
    border-radius: 24px;
    padding: 40px;
    text-align: center;
    box-shadow: 0 16px 40px rgba(34, 197, 94, 0.25), inset 0 0 20px rgba(34, 197, 94, 0.1);
    color: var(--text-primary);
    position: relative;
    overflow: hidden;
}
.result-badge {
    color: var(--bright-lime) !important;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 12px;
}
.result-crop {
    color: var(--text-primary) !important;
    font-size: 3.5rem;
    font-weight: 800;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin: 10px 0;
    text-shadow: 0 0 20px rgba(34, 197, 94, 0.4);
}
.result-prob {
    color: var(--mint-accent) !important;
    font-size: 1.15rem;
    margin: 0;
    font-weight: 600;
}
.result-disclaimer {
    color: var(--text-secondary) !important;
    font-size: 0.82rem;
    margin-top: 16px;
    font-style: italic;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}

/* ── Section Headers ── */
.section-header {
    display: flex;
    align-items: center;
    gap: 14px;
    margin: 2.5rem 0 1.5rem;
}
.section-title {
    color: var(--text-primary) !important;
    font-size: 1.45rem;
    font-weight: 700;
    margin: 0;
    letter-spacing: -0.3px;
}
.section-line {
    flex: 1;
    height: 1px;
    background: var(--border-color);
}

/* ── Info Boxes & Cards ── */
.info-box {
    background: var(--elevated-bg);
    border: 1px solid var(--border-color);
    border-left: 4px solid var(--primary-emerald);
    border-radius: 14px;
    padding: 18px 22px;
    color: var(--text-primary) !important;
    font-size: 0.94rem;
    line-height: 1.6;
    margin-bottom: 20px;
    box-shadow: 0 4px 16px rgba(0,0,0,0.2);
}
.content-card {
    background: var(--card-bg);
    border: 1px solid var(--border-color);
    border-radius: 18px;
    padding: 26px;
    margin-bottom: 18px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.3);
    transition: border-color 0.2s;
}
.content-card:hover {
    border-color: #356e4c;
}
.content-card h3 {
    color: var(--text-primary) !important;
    font-size: 1.15rem;
    font-weight: 700;
    margin-top: 0;
    margin-bottom: 12px;
}
.content-card p, .content-card li {
    color: var(--text-secondary) !important;
    font-size: 0.94rem;
    line-height: 1.6;
}

/* ── Form Inputs & Buttons ── */
div[data-testid="stForm"] {
    background: var(--card-bg) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: 20px !important;
    padding: 32px !important;
    box-shadow: 0 12px 36px rgba(0, 0, 0, 0.4) !important;
}

/* Input labels and text visibility fix */
label, .stTextInput label, .stNumberInput label, .stSelectbox label {
    color: var(--text-primary) !important;
    font-weight: 600 !important;
}
input, .stNumberInput input {
    background-color: var(--bg-main) !important;
    color: var(--text-primary) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: 10px !important;
}
input:focus, .stNumberInput input:focus {
    border-color: var(--primary-emerald) !important;
    box-shadow: 0 0 10px rgba(34, 197, 94, 0.2) !important;
}

/* Buttons */
.stButton > button, .stDownloadButton > button {
    background: linear-gradient(135deg, #16A34A, #22C55E) !important;
    color: #07140F !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
    font-size: 0.98rem !important;
    padding: 12px 26px !important;
    box-shadow: 0 6px 20px rgba(34, 197, 94, 0.35) !important;
    transition: transform 0.15s ease, opacity 0.2s ease, box-shadow 0.2s ease !important;
}
.stButton > button:hover, .stDownloadButton > button:hover {
    opacity: 0.95 !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(34, 197, 94, 0.5) !important;
}

/* Dividers & tables */
hr {
    border-color: var(--border-color) !important;
    margin: 2.5rem 0 !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL & METRICS ----------------

@st.cache_resource
def load_model():
    model = joblib.load("crop_model.pkl")
    features = joblib.load("feature_names.pkl")
    return model, features

@st.cache_data
def load_evaluation_metrics():
    if os.path.exists("evaluation_metrics.json"):
        try:
            with open("evaluation_metrics.json", "r") as f:
                return json.load(f)
        except Exception:
            return None
    return None

model, features = load_model()
eval_metrics = load_evaluation_metrics()

# ---------------- CROP DATABASE & METADATA ----------------

CROP_DATABASE = {
    "rice": {
        "name": "Rice",
        "category": "Cereal / Grain",
        "emoji": "🌾",
        "image": "https://images.unsplash.com/photo-1536256263959-770b48d82b08?w=600&q=80&auto=format&fit=crop",
        "ideal_temp": "20°C – 35°C",
        "ideal_rainfall": "150mm – 300mm",
        "soil_ph": "6.0 – 7.0",
        "description": "Rice is a staple food crop thriving in warm, humid climates with abundant water supply and clayey, water-retentive soils."
    },
    "maize": {
        "name": "Maize",
        "category": "Cereal / Grain",
        "emoji": "🌽",
        "image": "https://images.unsplash.com/photo-1551754655-cd97e68d206c?w=600&q=80&auto=format&fit=crop",
        "ideal_temp": "18°C – 27°C",
        "ideal_rainfall": "60mm – 110mm",
        "soil_ph": "5.5 – 7.5",
        "description": "Maize (corn) is a versatile cereal grain requiring well-drained fertile soils and moderate rainfall with ample sunlight."
    },
    "chickpea": {
        "name": "Chickpea",
        "category": "Pulse / Legume",
        "emoji": "🫘",
        "image": "https://images.unsplash.com/photo-1515543904379-3d757af72e44?w=600&q=80&auto=format&fit=crop",
        "ideal_temp": "15°C – 25°C",
        "ideal_rainfall": "60mm – 90mm",
        "soil_ph": "6.0 – 8.0",
        "description": "Chickpea is an important pulse crop grown in cooler, drier climates in loamy to sandy soils with good aeration."
    },
    "kidneybeans": {
        "name": "Kidney Beans",
        "category": "Pulse / Legume",
        "emoji": "🫘",
        "image": "https://images.unsplash.com/photo-1551462145-378290636712?w=600&q=80&auto=format&fit=crop",
        "ideal_temp": "16°C – 26°C",
        "ideal_rainfall": "90mm – 140mm",
        "soil_ph": "6.0 – 7.5",
        "description": "Kidney beans require temperate conditions, moderate moisture, and rich, well-draining loamy soil."
    },
    "pigeonpeas": {
        "name": "Pigeon Peas",
        "category": "Pulse / Legume",
        "emoji": "🫘",
        "image": "https://images.unsplash.com/photo-1515543904379-3d757af72e44?w=600&q=80&auto=format&fit=crop",
        "ideal_temp": "20°C – 30°C",
        "ideal_rainfall": "70mm – 130mm",
        "soil_ph": "5.5 – 7.5",
        "description": "Pigeon peas are hardy legume crops adapted to semi-arid regions with deep root systems."
    },
    "mothbeans": {
        "name": "Moth Beans",
        "category": "Pulse / Legume",
        "emoji": "🫘",
        "image": "https://images.unsplash.com/photo-1515543904379-3d757af72e44?w=600&q=80&auto=format&fit=crop",
        "ideal_temp": "24°C – 38°C",
        "ideal_rainfall": "40mm – 80mm",
        "soil_ph": "5.5 – 8.0",
        "description": "Moth bean is an extremely drought-resistant pulse crop well suited to arid sandy soils."
    },
    "mungbean": {
        "name": "Mung Bean",
        "category": "Pulse / Legume",
        "emoji": "🫘",
        "image": "https://images.unsplash.com/photo-1515543904379-3d757af72e44?w=600&q=80&auto=format&fit=crop",
        "ideal_temp": "25°C – 35°C",
        "ideal_rainfall": "60mm – 100mm",
        "soil_ph": "6.2 – 7.2",
        "description": "Mung bean is a short-duration warm-season legume requiring well-drained loam soils."
    },
    "blackgram": {
        "name": "Black Gram",
        "category": "Pulse / Legume",
        "emoji": "🫘",
        "image": "https://images.unsplash.com/photo-1585849834908-3488fb2ed38b?w=600&q=80&auto=format&fit=crop",
        "ideal_temp": "25°C – 35°C",
        "ideal_rainfall": "80mm – 150mm",
        "soil_ph": "6.5 – 7.8",
        "description": "Black gram (urad dal) thrives in humid tropical and subtropical areas with heavy clay-loam soils."
    },
    "lentil": {
        "name": "Lentil",
        "category": "Pulse / Legume",
        "emoji": "🌿",
        "image": "https://images.unsplash.com/photo-1584735935682-2f2b69dff9d2?w=600&q=80&auto=format&fit=crop",
        "ideal_temp": "18°C – 30°C",
        "ideal_rainfall": "40mm – 80mm",
        "soil_ph": "6.0 – 8.0",
        "description": "Lentils are cool-season annual pulse crops tolerant of moderate drought and winter temperatures."
    },
    "pomegranate": {
        "name": "Pomegranate",
        "category": "Fruit Crop",
        "emoji": "🍎",
        "image": "https://images.unsplash.com/photo-1541345304915-d4fc43cf496d?w=600&q=80&auto=format&fit=crop",
        "ideal_temp": "25°C – 38°C",
        "ideal_rainfall": "50mm – 80mm",
        "soil_ph": "5.5 – 7.2",
        "description": "Pomegranate is a drought-tolerant fruit tree thriving in semi-arid climates with sunny conditions."
    },
    "banana": {
        "name": "Banana",
        "category": "Fruit Crop",
        "emoji": "🍌",
        "image": "https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?w=600&q=80&auto=format&fit=crop",
        "ideal_temp": "25°C – 32°C",
        "ideal_rainfall": "150mm – 250mm",
        "soil_ph": "6.0 – 7.5",
        "description": "Bananas require tropical humidity, warm temperatures, consistent moisture, and rich, deep loam soils."
    },
    "mango": {
        "name": "Mango",
        "category": "Fruit Crop",
        "emoji": "🥭",
        "image": "https://images.unsplash.com/photo-1553279768-865429fa0078?w=600&q=80&auto=format&fit=crop",
        "ideal_temp": "24°C – 35°C",
        "ideal_rainfall": "90mm – 150mm",
        "soil_ph": "5.5 – 7.5",
        "description": "Mango trees flourish in tropical to subtropical climates with distinct dry seasons during flowering."
    },
    "grapes": {
        "name": "Grapes",
        "category": "Fruit Crop",
        "emoji": "🍇",
        "image": "https://images.unsplash.com/photo-1537640538966-79f369143f8f?w=600&q=80&auto=format&fit=crop",
        "ideal_temp": "15°C – 30°C",
        "ideal_rainfall": "60mm – 100mm",
        "soil_ph": "6.0 – 7.5",
        "description": "Grapevines prefer Mediterranean climates with warm sunny summers and well-drained soils."
    },
    "watermelon": {
        "name": "Watermelon",
        "category": "Fruit / Melon",
        "emoji": "🍉",
        "image": "https://images.unsplash.com/photo-1587049352847-4a222e784d38?w=600&q=80&auto=format&fit=crop",
        "ideal_temp": "24°C – 32°C",
        "ideal_rainfall": "40mm – 90mm",
        "soil_ph": "6.0 – 7.0",
        "description": "Watermelon is a warm-weather vining crop thriving in sandy loam soils with good drainage."
    },
    "muskmelon": {
        "name": "Muskmelon",
        "category": "Fruit / Melon",
        "emoji": "🍈",
        "image": "https://images.unsplash.com/photo-1571575183759-b1c4c1753966?w=600&q=80&auto=format&fit=crop",
        "ideal_temp": "24°C – 30°C",
        "ideal_rainfall": "40mm – 80mm",
        "soil_ph": "6.0 – 7.0",
        "description": "Muskmelons prefer warm, dry sunny conditions and fertile sandy loam soils."
    },
    "apple": {
        "name": "Apple",
        "category": "Fruit Crop",
        "emoji": "🍏",
        "image": "https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?w=600&q=80&auto=format&fit=crop",
        "ideal_temp": "15°C – 24°C",
        "ideal_rainfall": "100mm – 180mm",
        "soil_ph": "6.0 – 7.0",
        "description": "Apples are temperate fruit trees requiring cold winter chilling hours and well-draining loam soils."
    },
    "orange": {
        "name": "Orange",
        "category": "Fruit Crop",
        "emoji": "🍊",
        "image": "https://images.unsplash.com/photo-1611080626919-7cf5a9dbab5b?w=600&q=80&auto=format&fit=crop",
        "ideal_temp": "15°C – 30°C",
        "ideal_rainfall": "90mm – 150mm",
        "soil_ph": "6.0 – 7.5",
        "description": "Citrus fruits like oranges prefer subtropical climates with moderate rainfall and well-aerated soils."
    },
    "papaya": {
        "name": "Papaya",
        "category": "Fruit Crop",
        "emoji": "🍈",
        "image": "https://images.unsplash.com/photo-1617093727343-374698b1b08d?w=600&q=80&auto=format&fit=crop",
        "ideal_temp": "22°C – 32°C",
        "ideal_rainfall": "100mm – 200mm",
        "soil_ph": "6.0 – 7.0",
        "description": "Papaya is a fast-growing tropical fruit tree requiring warm temperatures and high drainage capacity."
    },
    "coconut": {
        "name": "Coconut",
        "category": "Tree / Plantation",
        "emoji": "🥥",
        "image": "https://images.unsplash.com/photo-1526947425960-945c6e72858f?w=600&q=80&auto=format&fit=crop",
        "ideal_temp": "27°C – 35°C",
        "ideal_rainfall": "150mm – 250mm",
        "soil_ph": "5.5 – 8.0",
        "description": "Coconut palms thrive in tropical coastal regions with high humidity, abundant sunshine, and sandy soils."
    },
    "cotton": {
        "name": "Cotton",
        "category": "Fiber Crop",
        "emoji": "🌸",
        "image": "https://images.unsplash.com/photo-1599940824399-b87987ceb72a?w=600&q=80&auto=format&fit=crop",
        "ideal_temp": "21°C – 35°C",
        "ideal_rainfall": "60mm – 110mm",
        "soil_ph": "5.8 – 8.0",
        "description": "Cotton is a major fiber crop requiring warm sunny weather, moderate rainfall, and deep alluvial soils."
    },
    "jute": {
        "name": "Jute",
        "category": "Fiber Crop",
        "emoji": "🌱",
        "image": "https://images.unsplash.com/photo-1586771107445-d3ca888129ff?w=600&q=80&auto=format&fit=crop",
        "ideal_temp": "24°C – 38°C",
        "ideal_rainfall": "150mm – 250mm",
        "soil_ph": "6.0 – 7.5",
        "description": "Jute is a rain-fed fiber crop requiring high humidity, warm temperatures, and alluvial soil."
    },
    "coffee": {
        "name": "Coffee",
        "category": "Plantation Crop",
        "emoji": "☕",
        "image": "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=600&q=80&auto=format&fit=crop",
        "ideal_temp": "15°C – 28°C",
        "ideal_rainfall": "150mm – 250mm",
        "soil_ph": "6.0 – 6.5",
        "description": "Coffee plants thrive in tropical highlands with shaded conditions, rich acidic soils, and high rainfall."
    }
}

def get_crop_info(name: str):
    return CROP_DATABASE.get(name.lower(), {
        "name": name.capitalize(),
        "category": "Agricultural Crop",
        "emoji": "🌱",
        "image": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=600&q=80&auto=format&fit=crop",
        "ideal_temp": "20°C – 30°C",
        "ideal_rainfall": "80mm – 150mm",
        "soil_ph": "6.0 – 7.0",
        "description": f"Agricultural crop: {name.capitalize()}."
    })

# ---------------- SIDEBAR NAVIGATION ----------------

with st.sidebar:
    st.markdown("""
    <div style="padding: 14px 0 10px;">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:6px;">
        <span style="font-size:2rem;">🌱</span>
        <div>
          <div style="color:#F8FAFC;font-size:1.2rem;font-weight:800;line-height:1.1;letter-spacing:-0.3px;">
            AgriWise AI
          </div>
          <div style="color:#22C55E;font-size:0.75rem;letter-spacing:1.5px;
              text-transform:uppercase;margin-top:3px;font-weight:700;">
            Crop Intelligence
          </div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="height:1px;background:var(--border-color);margin:12px 0 20px;"></div>', unsafe_allow_html=True)

    page = st.radio(
        "Navigation",
        [
            "Home",
            "Crop Recommendation",
            "Crop Library",
            "Soil Insights",
            "Prediction History",
            "Analytics & Performance",
            "About & Help"
        ],
        label_visibility="collapsed"
    )

    st.markdown('<div style="height:1px;background:var(--border-color);margin:20px 0 16px;"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div style="background:var(--card-bg);border:1px solid var(--border-color);border-radius:14px;padding:16px;">
      <div style="color:#22C55E;font-size:11px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:8px;">
        Neural Engine Status
      </div>
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:6px;">
        <span style="width:9px;height:9px;background:#22C55E;border-radius:50%;box-shadow:0 0 8px #22C55E;display:inline-block;"></span>
        <span style="color:#F8FAFC;font-size:0.86rem;font-weight:600;">Random Forest Active</span>
      </div>
      <div style="color:#B8C9BD;font-size:0.78rem;">100 estimators · 22 crop classes</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="height:16px;"></div>', unsafe_allow_html=True)
    st.caption("AgriWise AI © 2026 · Futuristic SaaS")

# =============================================
# PAGE 1: HOME
# =============================================

if page == "Home":
    st.markdown("""
    <div class="hero-banner">
      <img src="https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=1400&q=80&auto=format&fit=crop" alt="Futuristic agricultural farm field">
      <div class="hero-overlay">
        <div class="hero-badge">⚡ Futuristic Agricultural Intelligence</div>
        <h1 class="hero-title">Smarter Farming.<br>Better Decisions.</h1>
        <p class="hero-sub">Empowering agronomic precision with high-performance machine learning. Predict optimal crop yields instantly based on soil chemistry and environmental telemetry.</p>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Metric summary row
    c1, c2, c3, c4 = st.columns(4)
    metrics_home = [
        (c1, "🌾", str(len(model.classes_)), "Crop Categories", "Supported cultivars"),
        (c2, "📊", str(len(features)), "Input Features", "Soil & weather vectors"),
        (c3, "🎯", "99.55%", "Test Accuracy", "Held-out test split"),
        (c4, "🌲", "100", "Decision Trees", "Ensemble estimators"),
    ]
    for col, icon, val, label, sub in metrics_home:
        with col:
            st.markdown(f"""
            <div class="metric-card">
              <div class="metric-icon">{icon}</div>
              <div>
                <div class="metric-label">{label}</div>
                <div class="metric-value">{val}</div>
                <div class="metric-sub">{sub}</div>
              </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section-header" style="margin-top:2.8rem;">
      <h2 class="section-title">Operational Workflow</h2>
      <div class="section-line"></div>
    </div>
    """, unsafe_allow_html=True)

    s1, s2, s3 = st.columns(3)
    steps = [
        (s1, "01", "Telemetry & Soil Input", "Provide accurate Nitrogen (N), Phosphorus (P), Potassium (K), soil pH, temperature, humidity, and rainfall."),
        (s2, "02", "Ensemble Classification", "Our optimized Random Forest model analyzes your vectors across 100 decision trees to compute suitability scores."),
        (s3, "03", "Actionable Intelligence", "Receive top cultivar matches, probabilistic confidence metrics, and exportable professional reports."),
    ]
    for col, num, title, desc in steps:
        with col:
            st.markdown(f"""
            <div class="step-card">
              <div class="step-num">{num}</div>
              <div class="step-title">{title}</div>
              <div class="step-desc">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section-header" style="margin-top:2.8rem;">
      <h2 class="section-title">Core Platform Capabilities</h2>
      <div class="section-line"></div>
    </div>
    """, unsafe_allow_html=True)

    h1, h2, h3 = st.columns(3)
    with h1:
        st.markdown("""
        <div class="content-card">
          <h3>🔬 High-Precision ML</h3>
          <p>Trained on rigorous agricultural telemetry datasets to ensure maximum classification accuracy and robust generalization.</p>
        </div>
        """, unsafe_allow_html=True)
    with h2:
        st.markdown("""
        <div class="content-card">
          <h3>⚡ Real-Time Analytics</h3>
          <p>Instantaneous inference with interactive Plotly visualizations, radar distributions, and downloadable CSV audit reports.</p>
        </div>
        """, unsafe_allow_html=True)
    with h3:
        st.markdown("""
        <div class="content-card">
          <h3>🛡️ Transparent Decision Support</h3>
          <p>Clear probabilistic confidence metrics and feature importance breakdowns without black-box ambiguity.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box" style="margin-top:2rem;">
      <strong>⚠️ Decision Support Disclaimer:</strong> AgriWise AI delivers computational suggestions based on historical statistical patterns. Always integrate these insights with regional agronomic expertise and comprehensive laboratory soil testing.
    </div>
    """, unsafe_allow_html=True)

# =============================================
# PAGE 2: CROP RECOMMENDATION
# =============================================

elif page == "Crop Recommendation":
    st.markdown("""
    <div class="section-header">
      <h2 class="section-title">Crop Recommendation Engine</h2>
      <div class="section-line"></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
      <strong>Telemetry Input Instructions:</strong> Enter your soil nutrient laboratory report values and local climatic parameters.
      Nitrogen, Phosphorus, and Potassium (NPK) should be entered in mg/kg. Use preset profiles below for rapid simulation.
    </div>
    """, unsafe_allow_html=True)

    # Quick preset profiles
    st.markdown("**Quick Preset Profiles:**")
    preset_cols = st.columns(4)
    preset_values = None

    if preset_cols[0].button("🌾 Tropical Rice", width="stretch"):
        preset_values = {"N": 90.0, "P": 42.0, "K": 43.0, "temperature": 20.8, "humidity": 82.0, "ph": 6.5, "rainfall": 202.9}
    if preset_cols[1].button("🌽 Maize / Corn", width="stretch"):
        preset_values = {"N": 70.0, "P": 54.0, "K": 20.0, "temperature": 22.5, "humidity": 65.0, "ph": 6.8, "rainfall": 85.0}
    if preset_cols[2].button("🫘 Chickpea", width="stretch"):
        preset_values = {"N": 40.0, "P": 72.0, "K": 80.0, "temperature": 18.5, "humidity": 16.5, "ph": 7.2, "rainfall": 80.0}
    if preset_cols[3].button("🌸 Cotton", width="stretch"):
        preset_values = {"N": 120.0, "P": 40.0, "K": 20.0, "temperature": 23.5, "humidity": 79.5, "ph": 6.7, "rainfall": 80.3}

    if preset_values:
        for k, v in preset_values.items():
            st.session_state[f"input_{k}"] = v

    with st.form("crop_recommendation_form"):
        st.markdown("### 🌱 Soil Nutrient Profile (mg/kg)")
        c1, c2, c3 = st.columns(3)
        with c1:
            nitrogen = st.number_input(
                "Nitrogen (N)", min_value=0.0, max_value=200.0,
                value=st.session_state.get("input_N", 90.0), step=0.5,
                help="Available Nitrogen in soil (mg/kg). Typical range: 0–140."
            )
        with c2:
            phosphorus = st.number_input(
                "Phosphorus (P)", min_value=0.0, max_value=200.0,
                value=st.session_state.get("input_P", 42.0), step=0.5,
                help="Available Phosphorus in soil (mg/kg). Typical range: 5–145."
            )
        with c3:
            potassium = st.number_input(
                "Potassium (K)", min_value=0.0, max_value=250.0,
                value=st.session_state.get("input_K", 43.0), step=0.5,
                help="Available Potassium in soil (mg/kg). Typical range: 5–205."
            )

        st.markdown('<div style="height:1px;background:var(--border-color);margin:24px 0;"></div>', unsafe_allow_html=True)
        st.markdown("### 🌤️ Environmental & Climatic Conditions")

        c4, c5, c6, c7 = st.columns(4)
        with c4:
            temperature = st.number_input(
                "Temperature (°C)", min_value=0.0, max_value=60.0,
                value=st.session_state.get("input_temperature", 25.0), step=0.5,
                help="Average temperature in °C. Typical range: 8–44°C."
            )
        with c5:
            humidity = st.number_input(
                "Humidity (%)", min_value=0.0, max_value=100.0,
                value=st.session_state.get("input_humidity", 80.0), step=0.5,
                help="Relative humidity percentage. Typical range: 14–100%."
            )
        with c6:
            ph = st.number_input(
                "Soil pH", min_value=0.0, max_value=14.0,
                value=st.session_state.get("input_ph", 6.5), step=0.1,
                help="Soil acidity/alkalinity. Typical range: 3.5–10.0."
            )
        with c7:
            rainfall = st.number_input(
                "Rainfall (mm)", min_value=0.0, max_value=500.0,
                value=st.session_state.get("input_rainfall", 200.0), step=1.0,
                help="Rainfall in millimeters. Typical range: 20–300 mm."
            )

        st.markdown('<div style="height:12px;"></div>', unsafe_allow_html=True)

        col_btn1, col_btn2 = st.columns([3, 1])
        with col_btn1:
            submitted = st.form_submit_button("⚡ Run AI Cultivar Inference", width="stretch")
        with col_btn2:
            reset_clicked = st.form_submit_button("🔄 Reset Inputs", width="stretch")

    if reset_clicked:
        for k in ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]:
            st.session_state.pop(f"input_{k}", None)
        st.session_state.pop("prediction", None)
        st.rerun()

    if submitted:
        errors = []
        if not (0 <= ph <= 14): errors.append("Soil pH must be between 0 and 14.")
        if not (0 <= humidity <= 100): errors.append("Humidity must be between 0 and 100%.")
        if not (0 <= temperature <= 60): errors.append("Temperature must be between 0 and 60°C.")
        if rainfall < 0 or rainfall > 500: errors.append("Rainfall must be between 0 and 500 mm.")

        if errors:
            for err in errors:
                st.error(err, icon="⚠️")
        else:
            input_values = {
                "N": nitrogen, "P": phosphorus, "K": potassium,
                "temperature": temperature, "humidity": humidity,
                "ph": ph, "rainfall": rainfall
            }
            input_df = pd.DataFrame([[input_values[f] for f in features]], columns=features)
            prediction = model.predict(input_df)[0]
            probabilities = model.predict_proba(input_df)[0]
            confidence = float(max(probabilities)) * 100

            st.session_state["prediction"] = prediction
            st.session_state["probabilities"] = probabilities
            st.session_state["inputs"] = input_values
            st.session_state["confidence"] = confidence

            history_item = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "prediction": prediction,
                "confidence": confidence,
                "inputs": input_values.copy()
            }
            if "history" not in st.session_state:
                st.session_state["history"] = []
            if not st.session_state["history"] or st.session_state["history"][0]["inputs"] != input_values:
                st.session_state["history"].insert(0, history_item)

    if "prediction" in st.session_state:
        prediction = st.session_state["prediction"]
        probabilities = st.session_state["probabilities"]
        input_values = st.session_state["inputs"]
        confidence = st.session_state["confidence"]
        crop_meta = get_crop_info(prediction)

        st.markdown("""
        <div class="section-header" style="margin-top:2.8rem;">
          <h2 class="section-title">Inference Results</h2>
          <div class="section-line"></div>
        </div>
        """, unsafe_allow_html=True)

        col_res1, col_res2 = st.columns([2, 3])
        with col_res1:
            st.markdown(f"""
            <div class="result-card" style="height:100%;display:flex;flex-direction:column;justify-content:center;">
              <div class="result-badge">✨ Optimal Cultivar Match</div>
              <div style="font-size:3.5rem;margin:8px 0;">{crop_meta['emoji']}</div>
              <div class="result-crop">{prediction}</div>
              <div class="result-prob">Model Confidence: <strong>{confidence:.1f}%</strong></div>
              <div class="result-disclaimer">
                Derived from Random Forest ensemble classification. Represents training data probability distribution, not a cultivation guarantee.
              </div>
            </div>
            """, unsafe_allow_html=True)

        with col_res2:
            st.markdown(f"""
            <div class="content-card" style="height:100%;display:flex;flex-direction:column;justify-content:center;">
              <h3>📖 Cultivar Profile: {crop_meta['name']}</h3>
              <p><strong>Category:</strong> {crop_meta['category']}</p>
              <p>{crop_meta['description']}</p>
              <hr style="margin:14px 0;">
              <p style="margin:0;font-size:0.88rem;color:var(--mint-accent);">
                <strong>Ideal Climate:</strong> {crop_meta['ideal_temp']} &nbsp;|&nbsp;
                <strong>Rainfall:</strong> {crop_meta['ideal_rainfall']} &nbsp;|&nbsp;
                <strong>pH:</strong> {crop_meta['soil_ph']}
              </p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<div style="height:1.5rem;"></div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="section-header">
          <h2 class="section-title">Top 5 Cultivar Probabilities</h2>
          <div class="section-line"></div>
        </div>
        """, unsafe_allow_html=True)

        prob_df = (
            pd.DataFrame({"Crop": model.classes_, "Probability (%)": probabilities * 100})
            .sort_values("Probability (%)", ascending=False)
            .head(5)
            .sort_values("Probability (%)", ascending=True)
        )
        prob_df["Label"] = prob_df["Crop"].apply(
            lambda c: f"{get_crop_info(c)['emoji']} {c.capitalize()}"
        )

        fig_top5 = go.Figure(go.Bar(
            x=prob_df["Probability (%)"],
            y=prob_df["Label"],
            orientation="h",
            marker=dict(
                color=prob_df["Probability (%)"],
                colorscale=[[0, "#16A34A"], [1, "#22C55E"]],
            ),
            text=[f"{v:.1f}%" for v in prob_df["Probability (%)"]],
            textposition="outside",
            textfont=dict(color="#F8FAFC", size=12, weight="bold"),
        ))
        fig_top5.update_layout(
            template="plotly_dark",
            paper_bgcolor="#07140F",
            plot_bgcolor="#112B1E",
            height=320,
            margin=dict(l=10, r=60, t=20, b=20),
            xaxis=dict(title="Probability (%)", range=[0, 105], gridcolor="#28543A", color="#B8C9BD"),
            yaxis=dict(tickfont=dict(size=12, color="#F8FAFC")),
        )
        st.plotly_chart(fig_top5, width="stretch", alt="Top 5 cultivar probabilities chart")

        report_df = pd.DataFrame([{
            **input_values,
            "Recommended Crop": prediction,
            "Confidence (%)": round(confidence, 2),
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
        }])
        st.download_button(
            "📥 Download Professional Audit Report (CSV)",
            data=report_df.to_csv(index=False),
            file_name=f"AgriWise_Audit_{prediction}_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
            mime="text/csv",
            width="stretch"
        )

# =============================================
# PAGE 3: CROP LIBRARY
# =============================================

elif page == "Crop Library":
    st.markdown("""
    <div class="section-header">
      <h2 class="section-title">Cultivar Reference Library</h2>
      <div class="section-line"></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
      Browse reference profiles for all 22 supported agricultural crop classes. Inspect ideal environmental telemetry,
      soil pH requirements, and botanical categorizations.
    </div>
    """, unsafe_allow_html=True)

    search_query = st.text_input("🔍 Search cultivars by name or category...", "").lower()

    st.markdown('<div style="height:12px;"></div>', unsafe_allow_html=True)

    crops_to_show = [
        c for c in sorted(model.classes_)
        if search_query in c.lower() or search_query in get_crop_info(c)["category"].lower()
    ]

    cols = st.columns(3)
    for i, crop_key in enumerate(crops_to_show):
        info = get_crop_info(crop_key)
        with cols[i % 3]:
            st.markdown(f"""
            <div class="content-card" style="height:100%;display:flex;flex-direction:column;justify-content:space-between;">
              <div>
                <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;">
                  <span style="font-size:2.2rem;">{info['emoji']}</span>
                  <div>
                    <h3 style="margin:0;font-size:1.2rem;color:var(--text-primary);">{info['name']}</h3>
                    <span style="color:var(--bright-lime);font-size:0.75rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;">{info['category']}</span>
                  </div>
                </div>
                <p style="font-size:0.9rem;color:var(--text-secondary);margin-bottom:16px;line-height:1.5;">{info['description']}</p>
              </div>
              <div style="border-top:1px solid var(--border-color);padding-top:12px;font-size:0.82rem;color:var(--mint-accent);">
                <div>🌡️ Temp: <strong>{info['ideal_temp']}</strong></div>
                <div>💧 Rainfall: <strong>{info['ideal_rainfall']}</strong></div>
                <div>🧪 Soil pH: <strong>{info['soil_ph']}</strong></div>
              </div>
            </div>
            """, unsafe_allow_html=True)

# =============================================
# PAGE 4: SOIL INSIGHTS
# =============================================

elif page == "Soil Insights":
    st.markdown("""
    <div class="section-header">
      <h2 class="section-title">Soil Telemetry & Environmental Analytics</h2>
      <div class="section-line"></div>
    </div>
    """, unsafe_allow_html=True)

    if "prediction" not in st.session_state:
        st.markdown("""
        <div class="info-box">
          ℹ️ No active telemetry vector found. Please run an inference in <strong>Crop Recommendation</strong>
          to visualize detailed soil nutrient breakdowns and environmental charts.
        </div>
        """, unsafe_allow_html=True)
    else:
        input_values = st.session_state["inputs"]

        sm1, sm2, sm3, sm4 = st.columns(4)
        smaps = [
            (sm1, "🧪", f"{input_values['ph']}", "Soil pH Level", "Acidity / Alkalinity"),
            (sm2, "🌱", f"{input_values['N']} mg/kg", "Nitrogen (N)", "Macronutrient"),
            (sm3, "🌾", f"{input_values['P']} mg/kg", "Phosphorus (P)", "Macronutrient"),
            (sm4, "🥔", f"{input_values['K']} mg/kg", "Potassium (K)", "Macronutrient"),
        ]
        for col, icon, val, label, sub in smaps:
            with col:
                st.markdown(f"""
                <div class="metric-card">
                  <div class="metric-icon">{icon}</div>
                  <div>
                    <div class="metric-label">{label}</div>
                    <div class="metric-value" style="font-size:1.3rem;">{val}</div>
                    <div class="metric-sub">{sub}</div>
                  </div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown('<div style="height:1.8rem;"></div>', unsafe_allow_html=True)

        npk_df = pd.DataFrame({
            "Nutrient": ["Nitrogen (N)", "Phosphorus (P)", "Potassium (K)"],
            "Value (mg/kg)": [input_values["N"], input_values["P"], input_values["K"]]
        })
        fig_npk = px.bar(
            npk_df, x="Nutrient", y="Value (mg/kg)",
            color="Nutrient",
            color_discrete_sequence=["#16A34A", "#22C55E", "#86EFAC"],
            text="Value (mg/kg)"
        )
        fig_npk.update_layout(
            template="plotly_dark",
            paper_bgcolor="#07140F",
            plot_bgcolor="#112B1E",
            height=340,
            showlegend=False,
            margin=dict(l=10, r=10, t=30, b=20),
            yaxis=dict(gridcolor="#28543A", color="#B8C9BD"),
            xaxis=dict(color="#F8FAFC"),
            title=dict(text="<b>Soil Macronutrient Levels (NPK)</b>", font=dict(color="#F8FAFC", size=15))
        )
        st.plotly_chart(fig_npk, width="stretch", alt="NPK macronutrient chart")

        weather_df = pd.DataFrame({
            "Parameter": ["Temperature (°C)", "Humidity (%)", "Soil pH", "Rainfall (mm)"],
            "Entered Value": [input_values["temperature"], input_values["humidity"], input_values["ph"], input_values["rainfall"]]
        })
        st.markdown("""
        <div class="section-header">
          <h2 class="section-title">Climatic Telemetry Summary</h2>
          <div class="section-line"></div>
        </div>
        """, unsafe_allow_html=True)

        st.dataframe(weather_df, width="stretch", hide_index=True)

        st.markdown("""
        <div class="info-box" style="margin-top:1.2rem;">
          <strong>Agronomic Notice:</strong> Nutrient thresholds vary by cultivar and soil composition. Consult local agricultural
          extension offices for custom fertilization schedules.
        </div>
        """, unsafe_allow_html=True)

# =============================================
# PAGE 5: PREDICTION HISTORY
# =============================================

elif page == "Prediction History":
    st.markdown("""
    <div class="section-header">
      <h2 class="section-title">Session Inference History</h2>
      <div class="section-line"></div>
    </div>
    """, unsafe_allow_html=True)

    if "history" not in st.session_state or not st.session_state["history"]:
        st.markdown("""
        <div class="info-box">
          ℹ️ No inference history recorded in this session. Run an evaluation from <strong>Crop Recommendation</strong> to populate this log.
        </div>
        """, unsafe_allow_html=True)
    else:
        col_clear, col_space = st.columns([1, 4])
        with col_clear:
            if st.button("🗑️ Clear History", width="stretch"):
                st.session_state["history"] = []
                st.rerun()

        st.markdown('<div style="height:12px;"></div>', unsafe_allow_html=True)

        history_rows = []
        for idx, item in enumerate(st.session_state["history"]):
            inp = item["inputs"]
            history_rows.append({
                "Timestamp": item["timestamp"],
                "Recommended Cultivar": item["prediction"].capitalize(),
                "Confidence": f"{item['confidence']:.1f}%",
                "N": inp["N"], "P": inp["P"], "K": inp["K"],
                "Temp (°C)": inp["temperature"], "Humidity (%)": inp["humidity"],
                "pH": inp["ph"], "Rainfall (mm)": inp["rainfall"]
            })

        history_df = pd.DataFrame(history_rows)
        st.dataframe(history_df, width="stretch", hide_index=True)

        st.markdown("""
        <div class="info-box" style="margin-top:1.2rem;">
          <strong>Privacy Guarantee:</strong> History is maintained exclusively in local browser session memory and is never transmitted or persisted externally.
        </div>
        """, unsafe_allow_html=True)

# =============================================
# PAGE 6: ANALYTICS & PERFORMANCE
# =============================================

elif page == "Analytics & Performance":
    st.markdown("""
    <div class="section-header">
      <h2 class="section-title">Model Performance & Evaluation Metrics</h2>
      <div class="section-line"></div>
    </div>
    """, unsafe_allow_html=True)

    if eval_metrics:
        acc = eval_metrics.get("accuracy", 0.0) * 100
        prec = eval_metrics.get("precision", 0.0) * 100
        rec = eval_metrics.get("recall", 0.0) * 100
        f1 = eval_metrics.get("f1_score", 0.0) * 100

        em1, em2, em3, em4 = st.columns(4)
        eval_cards = [
            (em1, "🎯", f"{acc:.2f}%", "Test Accuracy", "Held-out test split"),
            (em2, "📈", f"{prec:.2f}%", "Macro Precision", "Average class precision"),
            (em3, "📉", f"{rec:.2f}%", "Macro Recall", "Average class recall"),
            (em4, "⚖️", f"{f1:.2f}%", "Macro F1-Score", "Harmonic mean"),
        ]
        for col, icon, val, label, sub in eval_cards:
            with col:
                st.markdown(f"""
                <div class="metric-card">
                  <div class="metric-icon">{icon}</div>
                  <div>
                    <div class="metric-label">{label}</div>
                    <div class="metric-value" style="font-size:1.35rem;">{val}</div>
                    <div class="metric-sub">{sub}</div>
                  </div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown('<div style="height:1.8rem;"></div>', unsafe_allow_html=True)

        perf_df = pd.DataFrame({
            "Evaluation Metric": ["Accuracy", "Precision", "Recall", "F1-Score"],
            "Score (%)": [acc, prec, rec, f1]
        })
        fig_perf = px.bar(
            perf_df, x="Evaluation Metric", y="Score (%)",
            color="Evaluation Metric",
            color_discrete_sequence=["#16A34A", "#22C55E", "#86EFAC", "#A3E635"],
            text="Score (%)"
        )
        fig_perf.update_layout(
            template="plotly_dark",
            paper_bgcolor="#07140F",
            plot_bgcolor="#112B1E",
            height=340,
            showlegend=False,
            margin=dict(l=10, r=10, t=30, b=20),
            yaxis=dict(range=[0, 105], gridcolor="#28543A", color="#B8C9BD"),
            xaxis=dict(color="#F8FAFC"),
            title=dict(text="<b>Model Evaluation Metrics (Test Dataset)</b>", font=dict(color="#F8FAFC", size=15))
        )
        st.plotly_chart(fig_perf, width="stretch", alt="Evaluation metrics bar chart")
    else:
        st.warning("Evaluation metrics data file (evaluation_metrics.json) not found.")

    st.markdown("""
    <div class="section-header" style="margin-top:2.8rem;">
      <h2 class="section-title">Random Forest Feature Importance</h2>
      <div class="section-line"></div>
    </div>
    """, unsafe_allow_html=True)

    feat_labels = {
        "N": "Nitrogen (N)", "P": "Phosphorus (P)", "K": "Potassium (K)",
        "temperature": "Temperature (°C)", "humidity": "Humidity (%)",
        "ph": "Soil pH", "rainfall": "Rainfall (mm)"
    }
    importance_df = pd.DataFrame({
        "Feature": [feat_labels.get(f, f) for f in features],
        "Importance": model.feature_importances_
    }).sort_values("Importance", ascending=True)

    fig_imp = px.bar(
        importance_df, x="Importance", y="Feature",
        orientation="h",
        color="Importance",
        color_continuous_scale="Greens"
    )
    fig_imp.update_layout(
        template="plotly_dark",
        paper_bgcolor="#07140F",
        plot_bgcolor="#112B1E",
        height=340,
        coloraxis_showscale=False,
        margin=dict(l=10, r=20, t=20, b=20),
        xaxis=dict(title="Gini Importance Score", gridcolor="#28543A", color="#B8C9BD"),
        yaxis=dict(title="", color="#F8FAFC")
    )
    st.plotly_chart(fig_imp, width="stretch", alt="Feature importance bar chart")

    st.markdown("""
    <div class="info-box">
      <strong>Note:</strong> Feature importance measures the mean decrease in Gini impurity across all 100 decision trees.
      It illustrates which telemetry vectors carry the strongest statistical weight in classification.
    </div>
    """, unsafe_allow_html=True)

# =============================================
# PAGE 7: ABOUT & HELP
# =============================================

elif page == "About & Help":
    st.markdown("""
    <div class="section-header">
      <h2 class="section-title">About AgriWise AI & Support</h2>
      <div class="section-line"></div>
    </div>
    """, unsafe_allow_html=True)

    col_ab1, col_ab2 = st.columns([3, 2])

    with col_ab1:
        st.markdown("""
        <div class="content-card">
          <h3>🎯 Platform Architecture</h3>
          <p>AgriWise AI is an enterprise-grade agricultural intelligence platform merging advanced soil telemetry with ensemble machine learning. By evaluating chemical and climatic vectors, the platform delivers optimal cultivar recommendations.</p>
        </div>

        <div class="content-card">
          <h3>🌲 Model Specifications</h3>
          <p>Powered by a <strong>Random Forest Classifier</strong> trained on 2,200 validated soil and climate samples across 22 distinct crop categories. The ensemble aggregates decisions from 100 individual decision trees using Gini impurity criteria.</p>
        </div>

        <div class="content-card">
          <h3>⚠️ Platform Limitations</h3>
          <p>AgriWise AI serves as a computational decision-support tool and should be paired with professional agronomic consultation. Predictions reflect statistical training patterns and do not account for unmeasured factors such as pest pressures, soil microbial health, or local market economics.</p>
        </div>
        """, unsafe_allow_html=True)

    with col_ab2:
        st.markdown("""
        <div class="content-card">
          <h3>❓ Frequently Asked Questions</h3>
          <p><strong>Q: Where do I obtain NPK values?</strong><br>From a certified local soil testing laboratory report.</p>
          <hr style="margin:12px 0;">
          <p><strong>Q: Are predictions guaranteed?</strong><br>No. They represent model confidence probabilities based on historical data.</p>
          <hr style="margin:12px 0;">
          <p><strong>Q: Is session data saved?</strong><br>No. All data processing occurs locally in browser memory.</p>
        </div>

        <div class="content-card">
          <h3>🛠️ Technology Stack</h3>
          <ul>
            <li><strong>Frontend:</strong> Streamlit</li>
            <li><strong>Machine Learning:</strong> scikit-learn (Random Forest)</li>
            <li><strong>Visualizations:</strong> Plotly (Dark SaaS Theme)</li>
            <li><strong>Data Processing:</strong> Pandas & NumPy</li>
          </ul>
        </div>
        """, unsafe_allow_html=True)

# ---------------- FOOTER ----------------

st.markdown("""
<div style="text-align:center;color:var(--text-secondary);font-size:0.82rem;padding:28px 0 12px;border-top:1px solid var(--border-color);margin-top:3.5rem;">
  AgriWise AI &nbsp;·&nbsp; Smarter Farming. Better Decisions. &nbsp;·&nbsp; Futuristic SaaS Edition 2026
</div>
""", unsafe_allow_html=True)
