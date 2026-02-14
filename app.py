import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Ondro, díky!", page_icon="🍺", layout="wide")

# Schovat Streamlit UI elementy
st.markdown("""
<style>
.stApp { background-color: #000 !important; }
header, footer, #MainMenu, [data-testid="stDecoration"],
[data-testid="stHeader"] { display: none !important; }
[data-testid="stMainBlockContainer"] { padding-top: 0 !important; }
iframe { border: none !important; }
</style>
""", unsafe_allow_html=True)

# Cela stranka jako HTML component (JS funguje uvnitr)
components.html("""
<!DOCTYPE html>
<html>
<head>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { background: #000; overflow: hidden; font-family: 'Courier New', monospace; }

canvas {
    position: fixed;
    top: 0;
    left: 0;
    z-index: 0;
}

.content {
    position: relative;
    z-index: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    padding: 2rem;
}

.content-box {
    background: rgba(0, 0, 0, 0.85);
    border: 1px solid rgba(0, 255, 65, 0.3);
    border-radius: 12px;
    padding: 3rem 4rem;
    box-shadow: 0 0 40px rgba(0, 255, 65, 0.1);
}

.beer {
    font-size: 6rem;
    animation: pulse 2s ease-in-out infinite;
    filter: drop-shadow(0 0 20px rgba(255, 200, 0, 0.5));
}

.title {
    font-size: 4.5rem;
    font-weight: bold;
    color: #00ff41;
    text-shadow: 0 0 20px #00ff41, 0 0 40px #00ff41, 0 0 80px #008f11;
    margin: 1rem 0;
    animation: flicker 4s infinite;
}

.message {
    font-size: 1.3rem;
    color: #00ff41;
    text-shadow: 0 0 10px #00ff41;
    text-align: center;
    line-height: 2.2;
    opacity: 0.9;
    max-width: 700px;
}

.quote {
    font-size: 1.1rem;
    color: #00ff41;
    opacity: 0.7;
    margin-top: 2rem;
    font-style: italic;
    text-shadow: 0 0 8px #00ff41;
}

.footer {
    font-size: 0.8rem;
    color: #00ff41;
    opacity: 0.35;
    margin-top: 3rem;
    text-align: center;
    line-height: 1.8;
}

@keyframes flicker {
    0%, 100% { opacity: 1; }
    92% { opacity: 1; }
    93% { opacity: 0.7; }
    94% { opacity: 1; }
    96% { opacity: 0.5; }
    97% { opacity: 1; }
}

@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.15); }
}
</style>
</head>
<body>

<canvas id="matrix"></canvas>

<div class="content">
    <div class="content-box">
    <div class="beer">🍺</div>
    <div class="title">Ondro, díky!</div>
    <div class="message">
        Za nasměrování na Streamlit + Community Cloud.<br>
        Tvoje konzultace funguje — tahle appka je důkaz.<br>
        Běží z GitHubu. Za 0 Kč. Na pár řádků Pythonu.
    </div>
    <div class="quote">Wake up, Ondra... The Matrix has you. 🐇</div>
    <div class="footer">
        [ SYSTEM ] Deployed from GitHub &rarr; Streamlit Community Cloud<br>
        [ STATUS ] Online &bull; Built with 🍺 and Python &bull; 2026 cube-da
    </div>
    </div>
</div>

<script>
const canvas = document.getElementById('matrix');
const ctx = canvas.getContext('2d');

function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}
resize();
window.addEventListener('resize', resize);

const chars = 'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン0123456789ABCDEF<>/{}=+';
const fontSize = 14;
let columns, drops;

function initDrops() {
    columns = Math.floor(canvas.width / fontSize);
    drops = Array(columns).fill(0).map(() => Math.random() * -100);
}
initDrops();
window.addEventListener('resize', initDrops);

function draw() {
    ctx.fillStyle = 'rgba(0, 0, 0, 0.04)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.font = fontSize + 'px monospace';

    for (let i = 0; i < drops.length; i++) {
        const char = chars[Math.floor(Math.random() * chars.length)];
        const x = i * fontSize;
        const y = drops[i] * fontSize;

        // Hlava sloupce je jasnejsi
        if (Math.random() > 0.98) {
            ctx.fillStyle = '#ffffff';
        } else if (Math.random() > 0.9) {
            ctx.fillStyle = '#80ff80';
        } else {
            ctx.fillStyle = '#00ff41';
        }

        ctx.fillText(char, x, y);

        if (y > canvas.height && Math.random() > 0.98) {
            drops[i] = 0;
        }
        drops[i] += 0.5 + Math.random() * 0.5;
    }
}

setInterval(draw, 33);
</script>

</body>
</html>
""", height=800, scrolling=False)
