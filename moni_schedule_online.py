import streamlit as st
import calendar
from datetime import datetime
import base64
from datetime import timedelta

def get_base64_img(img_path):
    with open(img_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

left_side_image_base64 = get_base64_img("cat.jpg")
right_side_image_base64 = get_base64_img("shao.jpg")

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
            url("data:image/png;base64,{left_side_image_base64}"),
            url("data:image/png;base64,{right_side_image_base64}");
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
st.write("Select month and assign daily time")

today = datetime.now()
next_month = today.month % 12 + 1
next_year = today.year + (1 if today.month == 12 else 0)

# year = st.number_input("Year", min_value=2020, max_value=2100, value=next_year)
# month = st.number_input("Month", min_value=1, max_value=12, value=next_month)


def generate_month_options():
    today = datetime.now().replace(day=1)
    start_month = today + timedelta(days=32)  # next month
    start_month = start_month.replace(day=1)

    month_list = []
    for i in range(24):  # next 24 months
        target = (start_month.replace(day=1) + timedelta(days=32 * i)).replace(day=1)
        month_list.append(target)

    return month_list

month_options = generate_month_options()

month_display = [m.strftime("%b %Y") for m in month_options]

default_index = 0  # always next month

selected = st.selectbox("Select Month", month_display, index=default_index)

selected_date = month_options[month_display.index(selected)]
year = selected_date.year
month = selected_date.month

st.markdown("---")

st.subheader("Step 2 - Select schedule option for each day")

TIME_SETS = {
    "Time-1": ["10:30", "14:00", "17:30"],
    "Time-2": ["10:00", "13:00", "16:30", "19:30"],
    "Time-3": ["11:00", "14:30", "18:00"],
}

OPTION_LABELS = ["None", "Dayoff", "Time-1", "Time-2", "Time-3"]
WEEKDAY_NAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

days_in_month = calendar.monthrange(int(year), int(month))[1]

st.write(f"Selected Month: **{int(year)} / {int(month):02d}**")

header_cols = st.columns([1, 1, 4])
with header_cols[0]:
    st.markdown("**Date**")
with header_cols[1]:
    st.markdown("**Weekday**")
with header_cols[2]:
    st.markdown("**Option**")

for day in range(1, days_in_month + 1):
    weekday = calendar.weekday(int(year), int(month), day)
    day_name = WEEKDAY_NAMES[weekday]
    date_str = f"{int(month):02d}/{day:02d}"

    c1, c2, c3 = st.columns([1, 1, 4])
    with c1:
        st.write(date_str)
    with c2:
        st.write(day_name)
    with c3:
        key = f"choice_{int(year)}_{int(month)}_{day}"
        st.radio(
            "Option",
            OPTION_LABELS,
            key=key,
            label_visibility="collapsed",
            horizontal=True,
        )

st.markdown("---")

def generate_schedule_from_choices(year: int, month: int):
    lines = []
    all_times = [t for times in TIME_SETS.values() for t in times]
    max_time_length = max(len(t) for t in all_times)
    time_format = f"{{:<{max_time_length}}}"

    for day in range(1, days_in_month + 1):
        weekday = calendar.weekday(year, month, day)
        day_name = WEEKDAY_NAMES[weekday]
        day_str = f"{day:02d}"
        key = f"choice_{year}_{month}_{day}"
        choice = st.session_state.get(key, "None")

        if choice == "None":
            line = f"{month}/{day_str} ({day_name})"
        elif choice == "Dayoff":
            line = f"{month}/{day_str} ({day_name}) Dayoff"
        else:
            times = TIME_SETS.get(choice, [])
            formatted_times = " ".join(time_format.format(t) for t in times)
            line = f"{month}/{day_str} ({day_name}) {formatted_times}"

        lines.append(line)

        if weekday == 6:
            lines.append("")

    return "\n".join(lines)

if st.button("Generate"):
    schedule_text = generate_schedule_from_choices(int(year), int(month))
    st.subheader("Preview")
    st.code(schedule_text, language="text")
