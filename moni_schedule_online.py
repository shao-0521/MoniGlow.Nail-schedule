import streamlit as st
import calendar
from datetime import datetime, date
import base64

def get_base64_img(img_path):
    with open(img_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

side_image_base64 = get_base64_img("cat.jpg")

st.markdown(
    f"""
    <style>
    @keyframes scroll-vertical {{
        0%   {{ background-position-y: 0px; }}
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
        animation: scroll-vertical 10s linear infinite alternate;
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

    /* 🔍 Make number input fields and step buttons larger */
    input[type="number"] {{
        font-size: 1.3rem !important;
        padding: 0.5rem 1rem !important;
    }}

    button[aria-label="Increment"] > svg,
    button[aria-label="Decrement"] > svg {{
        width: 20px !important;
        height: 20px !important;
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
st.write("Enter the year, month, and daily time")

today = datetime.now()
next_month = today.month % 12 + 1
next_year = today.year + (1 if today.month == 12 else 0)

year = st.number_input("Year", min_value=2020, max_value=2100, value=next_year)
month = st.number_input("Month", min_value=1, max_value=12, value=next_month)

time_input = st.text_input("Daily time slots (e.g., 10:30, 14:00, 17:30)", "10:30,14:00,17:30")
schedule_times = [t.strip() for t in time_input.split(",") if t.strip()]

def generate_schedule(year, month, schedule_times):
    days_in_month = calendar.monthrange(year, month)[1]
    max_time_length = max(len(time) for time in schedule_times)
    time_format = f"{{:<{max_time_length}}}"

    output_lines = []
    for day in range(1, days_in_month + 1):
        current_date = date(year, month, day)
        weekday = calendar.weekday(year, month, day)
        day_name = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][weekday]
        day_str = f"{day:02d}"
        formatted_times = " ".join([time_format.format(time) for time in schedule_times])
        line = f"{month}/{day_str} ({day_name}) {formatted_times}"
        output_lines.append(line)

        if weekday == 6:
            output_lines.append("")

    return "\n".join(output_lines)


if st.button("Generate Schedule"):
    if not schedule_times:
        st.error("Please enter at least one time")
    else:
        schedule_text = generate_schedule(year, month, schedule_times)
        st.subheader("Preview (you can copy by touch the schedule and the copy buttn on the upper right)")
        st.code(schedule_text, language="text")
