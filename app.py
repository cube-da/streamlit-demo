import streamlit as st

st.set_page_config(page_title="Ondři, díky!", page_icon="🍺", layout="wide")

# Matrix rain + styling
st.markdown("""
<style>
/* Matrix canvas na pozadi */
canvas#matrix {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
}

/* Ztmavit Streamlit pozadi */
.stApp {
    background-color: rgba(0, 0, 0, 0.85);
}
header, [data-testid="stHeader"] {
    background-color: transparent !important;
}

/* Texty */
.matrix-title {
    font-family: 'Courier New', monospace;
    font-size: 5rem;
    font-weight: bold;
    text-align: center;
    color: #00ff41;
    text-shadow: 0 0 20px #00ff41, 0 0 40px #00ff41, 0 0 80px #008f11;
    margin-top: 10vh;
    animation: flicker 3s infinite;
}
.matrix-subtitle {
    font-family: 'Courier New', monospace;
    font-size: 1.5rem;
    text-align: center;
    color: #00ff41;
    opacity: 0.9;
    text-shadow: 0 0 10px #00ff41;
    margin-top: 1rem;
    line-height: 2;
}
.matrix-footer {
    font-family: 'Courier New', monospace;
    font-size: 0.9rem;
    text-align: center;
    color: #00ff41;
    opacity: 0.5;
    margin-top: 5rem;
}
.matrix-beer {
    font-size: 8rem;
    text-align: center;
    margin: 2rem 0;
    animation: pulse 2s ease-in-out infinite;
}

@keyframes flicker {
    0%, 100% { opacity: 1; }
    92% { opacity: 1; }
    93% { opacity: 0.8; }
    94% { opacity: 1; }
    96% { opacity: 0.6; }
    97% { opacity: 1; }
}
@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.1); }
}

/* Schovat Streamlit default elementy */
#MainMenu, footer, [data-testid="stDecoration"] { display: none; }
</style>

<!-- Matrix Rain Canvas -->
<canvas id="matrix"></canvas>
<script>
const canvas = document.getElementById('matrix');
const ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const chars = 'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン0123456789ABCDEF';
const fontSize = 14;
const columns = canvas.width / fontSize;
const drops = Array(Math.floor(columns)).fill(1);

function draw() {
    ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = '#00ff41';
    ctx.font = fontSize + 'px monospace';

    for (let i = 0; i < drops.length; i++) {
        const text = chars[Math.floor(Math.random() * chars.length)];
        ctx.fillStyle = Math.random() > 0.98 ? '#fff' : '#00ff41';
        ctx.fillText(text, i * fontSize, drops[i] * fontSize);
        if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
            drops[i] = 0;
        }
        drops[i]++;
    }
}

setInterval(draw, 35);
window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});
</script>
""", unsafe_allow_html=True)

# Obsah
st.markdown('<div class="matrix-beer">🍺</div>', unsafe_allow_html=True)
st.markdown('<div class="matrix-title">Ondři, díky!</div>', unsafe_allow_html=True)
st.markdown("""
<div class="matrix-subtitle">
> Za nasměrování na Streamlit.<br>
> Tvoje konzultace funguje — tahle appka je důkaz.<br>
> Běží z GitHubu. Za 0 Kč. Na pár řádků Pythonu.<br>
<br>
> Wake up, Ondra... The Matrix has you.<br>
> Follow the white rabbit. 🐇
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="matrix-footer">
[ SYSTEM ] Deployed from GitHub → Streamlit Community Cloud<br>
[ STATUS ] Online | Built with 🍺 and Python | © 2026 cube-da
</div>
""", unsafe_allow_html=True)
