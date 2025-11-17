import streamlit as st
import calendar
from datetime import datetime, timedelta
import base64

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

def generate_month_options():
    today = datetime.now().replace(day=1)
    start_month = today + timedelta(days=32)
    start_month = start_month.replace(day=1)
    month_list = []
    for i in range(24):
        target = (start_month + timedelta(days=32 * i)).replace(day=1)
        month_list.append(target)
    return month_list

month_options = generate_month_options()
month_display = [m.strftime("%b %Y") for m in month_options]
selected = st.selectbox("Select Month", month_display, index=0)
selected_date = month_options[month_display.index(selected)]
year = selected_date.year
month = selected_date.month

st.markdown("---")

st.subheader("Customize Time Sets")

if "time_sets" not in st.session_state:
    st.session_state.time_sets = {
        "Time-1": ["10:30", "14:00", "17:30"],
        "Time-2": ["10:00", "13:00", "16:30", "19:30"],
        "Time-3": ["11:00", "14:30", "18:00"]
    }

for label in ["Time-1", "Time-2", "Time-3"]:
    st.markdown(f"**{label}**")
    current_list = st.session_state.time_sets[label]

    remove_indices = []
    cols = st.columns(4)

    for idx, t in enumerate(current_list):
        col = cols[idx % 4]
        with col:
            new_value = st.text_input(f"{label}_{idx}", value=t, label_visibility="collapsed")
            if new_value != t:
                current_list[idx] = new_value
            remove = st.button("Remove", key=f"rm_{label}_{idx}")
            if remove:
                remove_indices.append(idx)

    for idx in sorted(remove_indices, reverse=True):
        current_list.pop(idx)

    add_time = st.text_input(f"add_{label}", placeholder="HH:MM")
    if st.button(f"Add time to {label}"):
        if add_time:
            current_list.append(add_time)

    st.markdown("---")

TIME_SETS = st.session_state.time_sets

st.subheader("Select schedule option for each day")

OPTION_LABELS = ["None", "Dayoff", "Time-1", "Time-2", "Time-3"]
WEEKDAY_NAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

days_in_month = calendar.monthrange(year, month)[1]

header_cols = st.columns([1, 1, 4])
with header_cols[0]:
    st.markdown("**Date**")
with header_cols[1]:
    st.markdown("**Weekday**")
with header_cols[2]:
    st.markdown("**Option**")

for day in range(1, days_in_month + 1):
    weekday = calendar.weekday(year, month, day)
    day_name = WEEKDAY_NAMES[weekday]
    date_str = f"{month:02d}/{day:02d}"

    c1, c2, c3 = st.columns([1, 1, 4])
    with c1:
        st.write(date_str)
    with c2:
        st.write(day_name)
    with c3:
        key = f"choice_{year}_{month}_{day}"
        st.radio("Option", OPTION_LABELS, key=key, label_visibility="collapsed", horizontal=True)

st.markdown("---")

def generate_schedule(year, month):
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
    txt = generate_schedule(year, month)
    st.subheader("Preview")
    st.code(txt, language="text")
