import streamlit as st


def footer_home():
    st.markdown("""
        <style>
        .footer-container {
            margin-top: 3rem;
            text-align: center;
        }

        .gradient-text {
            font-weight: 700;
            font-size: 20px;
            letter-spacing: 0.6px;
            background: linear-gradient(90deg, #00C9FF, #92FE9D, #ff4b4b);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: shine 4s linear infinite;
        }

        @keyframes shine {
            to {
                background-position: 200% center;
            }
        }

        .tagline {
            font-size: 12px;
            color: #bbb;
            margin-top: 6px;
            letter-spacing: 0.3px;
        }
        </style>

        <div class="footer-container">
            <div class="gradient-text">
                ✨ Created with ❤️ by Anuj Patil ✨
            </div>
            <div class="tagline">
                AI Powered Attendance System 🚀
            </div>
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown("""
        <style>
        .footer-container {
            margin-top: 3rem;
            text-align: center;
        }

        .text {
            font-size: 16px;
            color: #666;
            letter-spacing: 0.4px;
        }

        .anuj-highlight {
            font-weight: 700;
            color: #ff4b4b;
            text-shadow: 0 0 8px rgba(255,75,75,0.7);
        }

        .badge {
            display: inline-block;
            margin-top: 10px;
            padding: 6px 14px;
            font-size: 12px;
            border-radius: 999px;
            background: linear-gradient(90deg, rgba(255,75,75,0.1), rgba(0,201,255,0.1));
            color: #333;
            border: 1px solid rgba(255, 75, 75, 0.3);
        }
        </style>

        <div class="footer-container">
            <div class="text">
                🚀 Built by <span class="anuj-highlight">Anuj Patil</span>
            </div>

        </div>
    """, unsafe_allow_html=True)
