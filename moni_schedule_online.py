import streamlit as st
import calendar
from datetime import datetime
import base64

def get_base64_img(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# 讀 logo
if "logo_img" not in st.session_state:
    st.session_state.logo_img = get_base64_img("moni_nail.jpg")

logo_base64 = st.session_state.logo_img

# 基本樣式設定
st.markdown(
    """
    <style>
    @keyframes scroll-vertical {
        0%   { background-position-y: 0; }
        100% { background-position-y: 1000px; }
    }
    .stApp {
        background-color: black;
    }
    .stApp, .stMarkdown, .stTextInput, .stNumberInput, .stCode {
        color: white !important;
    }
    button div[data-testid="baseButton-body"] span {
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# logo
st.markdown(
    f"""
    <div style='text-align:center; margin-bottom:10px;'>
        <img src='data:image/jpeg;base64,{logo_base64}'
             style='width:120px; height:120px; border-radius:50%; object-fit:cover;
             box-shadow: 0 0 10px rgba(255,255,255,0.4);' />
    </div>
    """,
    unsafe_allow_html=True
)

st.title("MoniGlow._Nail Schedule")

# 預設顯示「下個月」
if "current_year" not in st.session_state:
    today = datetime.now()
    next_month = today.month % 12 + 1
    next_year = today.year + (1 if today.month == 12 else 0)
    st.session_state.current_year = next_year
    st.session_state.current_month = next_month

col_prev, col_center, col_next = st.columns([1, 3, 1])

with col_prev:
    st.markdown("<div style='text-align:left;'>", unsafe_allow_html=True)
    if st.button("← Prev"):
        if st.session_state.current_month == 1:
            st.session_state.current_month = 12
            st.session_state.current_year -= 1
        else:
            st.session_state.current_month -= 1
    st.markdown("</div>", unsafe_allow_html=True)

with col_center:
    month_label = datetime(
        st.session_state.current_year,
        st.session_state.current_month,
        1
    ).strftime("%B %Y")

    st.markdown(
        f"<h2 style='text-align:center; margin-top:5px;'>{month_label}</h2>",
        unsafe_allow_html=True
    )

with col_next:
    st.markdown("<div style='text-align:right;'>", unsafe_allow_html=True)
    if st.button("Next →"):
        if st.session_state.current_month == 12:
            st.session_state.current_month = 1
            st.session_state.current_year += 1
        else:
            st.session_state.current_month += 1
    st.markdown("</div>", unsafe_allow_html=True)

year = st.session_state.current_year
month = st.session_state.current_month
days_in_month = calendar.monthrange(year, month)[1]

st.markdown("---")

# ---- Time sets 設定區 ----
st.subheader("Customize Time Sets")

if "time_sets" not in st.session_state:
    st.session_state.time_sets = {
        "Time-1": "10:30, 14:00, 17:30",
        "Time-2": "11:00, 14:30, 18:00",
        "Time-3": "10:00, 13:00, 16:30, 19:30",
    }

c1, c2, c3 = st.columns(3)
with c1:
    st.session_state.time_sets["Time-1"] = st.text_input(
        "Time-1 (comma separated)", st.session_state.time_sets["Time-1"]
    )
with c2:
    st.session_state.time_sets["Time-2"] = st.text_input(
        "Time-2 (comma separated)", st.session_state.time_sets["Time-2"]
    )
with c3:
    st.session_state.time_sets["Time-3"] = st.text_input(
        "Time-3 (comma separated)", st.session_state.time_sets["Time-3"]
    )

st.markdown("---")

OPTION_LABELS = ["None", "Dayoff", "Time-1", "Time-2", "Time-3"]
WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# 解析 time_sets 的小工具
def parse_time_sets():
    parsed = {}
    for k, v in st.session_state.time_sets.items():
        parsed[k] = [t.strip() for t in v.split(",") if t.strip()]
    return parsed

# ---- Daily Schedule 設定 ----
st.subheader("Daily Schedule Settings")

with st.expander("Click to expand day settings", expanded=True):
    header = st.columns([1, 1, 4])
    with header[0]:
        st.markdown("**Date**")
    with header[1]:
        st.markdown("**Weekday**")
    with header[2]:
        st.markdown("**Option / Time Buttons**")

    parsed_time_sets = parse_time_sets()

    for day in range(1, days_in_month + 1):
        weekday = calendar.weekday(year, month, day)
        day_name = WEEKDAYS[weekday]
        date_str = f"{month:02d}/{day:02d}"

        r1, r2, r3 = st.columns([1, 1, 4])
        with r1:
            st.write(date_str)
        with r2:
            st.write(day_name)

        with r3:
            # 每天的 Time-組合選擇
            key = f"choice_{year}_{month}_{day}"
            if key not in st.session_state:
                st.session_state[key] = "Time-1"

            choice = st.radio(
                "Option",
                OPTION_LABELS,
                key=key,
                label_visibility="collapsed",
                horizontal=True
            )

            # 根據選到的 Time-? 顯示相對應時間的 BTN (checkbox)
            if choice in parsed_time_sets:
                times = parsed_time_sets.get(choice, [])
                if times:
                    btn_cols = st.columns(len(times))
                    for i, t in enumerate(times):
                        with btn_cols[i]:
                            cb_key = f"cb_{year}_{month}_{day}_{t}"
                            st.checkbox(t, key=cb_key)

        # ▼ 分隔線：每天 ---- ，每週結束（日→下週一）用 ===
        if day != days_in_month:  # 最後一天下方可選擇要不要畫，這裡先畫
            if weekday == 6:      # Sunday
                st.markdown("=*50")
            else:
                st.markdown("----")

st.markdown("---")

# ---- 產生文字版 Schedule ----
def generate_schedule(year, month):
    output = []
    parsed = parse_time_sets()

    # 計算時間欄位對齊用寬度
    all_times = [t for arr in parsed.values() for t in arr]
    max_len = max(len(t) for t in all_times) if all_times else 5
    fmt = f"{{:<{max_len}}}"

    days_in_month_local = calendar.monthrange(year, month)[1]

    for day in range(1, days_in_month_local + 1):
        weekday = calendar.weekday(year, month, day)
        wd = WEEKDAYS[weekday]
        d = f"{day:02d}"
        key = f"choice_{year}_{month}_{day}"
        choice = st.session_state.get(key, "Time-1")

        if choice == "None":
            line = f"{month}/{d} ({wd})"

        elif choice == "Dayoff":
            line = f"{month}/{d} ({wd}) Dayoff"

        else:
            times = parsed.get(choice, [])

            # 根據 checkbox 狀態移除已被勾選（預約）的時間
            remaining_times = []
            for t in times:
                cb_key = f"cb_{year}_{month}_{day}_{t}"
                booked = st.session_state.get(cb_key, False)
                if not booked:
                    remaining_times.append(t)

            if remaining_times:
                formatted = " ".join(fmt.format(t) for t in remaining_times)
                line = f"{month}/{d} ({wd}) {formatted}"
            else:
                # 全部被預約，就只顯示日期 + 星期
                line = f"{month}/{d} ({wd})"

        output.append(line)

        # 每週（日）後面加空行，讓文字表看起來分週
        if weekday == 6:
            output.append("")

    return "\n".join(output)

# ---- 按鈕產生 Preview ----
if st.button("Generate"):
    txt = generate_schedule(year, month)
    st.subheader("Preview")
    st.code(txt, language="text")
