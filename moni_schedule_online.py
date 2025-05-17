import streamlit as st
import calendar
from datetime import datetime
import base64

def get_base64_img(img_path):
    with open(img_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

side_image_base64 = get_base64_img("cat.jpg")

st.markdown(
    f"""
    <style>
    @keyframes scroll-up {{
        0% {{ background-position-y: 1000px; }}
        100% {{ background-position-y: 0px; }}
    }}

    @keyframes scroll-down {{
        0% {{ background-position-y: 0px; }}
        100% {{ background-position-y: 1000px; }}
    }}

    .stApp {{
        background-color: black;
        background-image:
            url("data:image/png;base64,{side_image_base64}"),
            url("data:image/png;base64,{side_image_base64}");
        background-repeat: repeat-y, repeat-y;
        background-position: left top, right top;
        background-size: 100px auto, 100px auto;
        animation: scroll-up 20s linear infinite, scroll-down 20s linear infinite;
        background-attachment: scroll, scroll;
    }}

    .stApp, .stMarkdown, .stTextInput, .stNumberInput, .stCode {{
        color: white !important;
    }}

    button div[data-testid="baseButton-body"] span {{
        color: black !important;
    }}

    button:focus div[data-testid="baseButton-body"] span,
    button:active div[data-testid="baseButton-body"] span {{
        color: black !important;
    }}

    @media (max-width: 768px) {{
        .stApp img {{
            width: 80px !important;
            height: 80px !important;
        }}
        .logo-container {{
            margin-bottom: 5px;
        }}
        .stTitle {{
            font-size: 1.5rem !important;
            text-align: center;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True
)




logo_base64 = get_base64_img("moni_nail.jpg")

st.markdown(
    f"""
    <div class='logo-container' style='text-align:center; margin-bottom:10px;'>
        <img src='data:image/jpeg;base64,{logo_base64}'
             style='width:120px; height:120px; border-radius:50%; object-fit:cover;
                    box-shadow: 0 0 10px rgba(255,255,255,0.4);' />
    </div>
    """,
    unsafe_allow_html=True
)

st.title("MoniGlow._Nail Schedule")
st.write("Enter the year, month and time of day")

year = st.number_input("Years", min_value=2020, max_value=2100, value=datetime.now().year)
month = st.number_input("Month", min_value=1, max_value=12, value=datetime.now().month)
time_input = st.text_input("Enter the daily time (default: 10:30, 14:00, 17:30)", "10:30,14:00,17:30")

schedule_times = [t.strip() for t in time_input.split(",") if t.strip()]

def generate_schedule(year, month, schedule_times):
    days_in_month = calendar.monthrange(year, month)[1]
    max_time_length = max(len(time) for time in schedule_times)
    time_format = f"{{:<{max_time_length}}}"

    output_lines = []
    for day in range(1, days_in_month + 1):
        weekday = calendar.weekday(year, month, day)
        day_name = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][weekday]
        day_str = f"{day:02d}"
        formatted_times = " ".join([time_format.format(time) for time in schedule_times])
        line = f"{month}/{day_str}({day_name}) {formatted_times}"
        output_lines.append(line)

    return "\n".join(output_lines)

if st.button("Generate"):
    if not schedule_times:
        st.error("Enter at least one time")
    else:
        schedule_text = generate_schedule(year, month, schedule_times)

        st.subheader("Schedule preview (copy in the upper right corner)")
        st.code(schedule_text, language="text")
