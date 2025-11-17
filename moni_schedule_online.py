import streamlit as st
import calendar
from datetime import datetime, timedelta
import base64

def get_base64_img(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# 載入背景與 logo 圖片（只載一次）
if "bg_left" not in st.session_state:
    st.session_state.bg_left = get_base64_img("cat.jpg")
if "bg_right" not in st.session_state:
    st.session_state.bg_right = get_base64_img("shao.jpg")
if "logo_img" not in st.session_state:
    st.session_state.logo_img = get_base64_img("moni_nail.jpg")

left_side_image_base64 = st.session_state.bg_left
right_side_image_base64 = st.session_state.bg_right
logo_base64 = st.session_state.logo_img

# 全域樣式 + 手機版優化
st.markdown(
    f"""
    <style>
    @keyframes scroll-vertical {{
        0%   {{ background-position-y: 0; }}
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
    }}
    .stApp, .stMarkdown, .stTextInput, .stNumberInput, .stCode {{
        color: white !important;
    }}
    button div[data-testid="baseButton-body"] span {{
        color: black !important;
    }}

    /* ------- 手機版樣式 ------- */
    @media (max-width: 768px) {{

        /* 只留一側背景、縮小一點，避免太花 */
        .stApp {{
            background-image:
                url("data:image/png;base64,{left_side_image_base64}");
            background-size: 60px auto;
            animation: none; /* 手機上關掉背景動畫 */
        }}

        /* 讓所有 columns 直向堆疊，避免擠一排 */
        div[data-testid="column"] {{
            flex: 1 1 100% !important;
        }}

        /* 讓所有 st.radio 的選項改成直向排列 */
        div[data-testid="stRadio"] > div {{
            flex-direction: column !important;
        }}

        /* 字體稍微縮小 */
        h1, h2, h3 {{
            font-size: 1.1rem !important;
        }}
        code {{
            font-size: 0.8rem !important;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Logo
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

# 目前顯示月份（預設下一個月）
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

# 時間組合設定
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

st.subheader("Daily Schedule Settings")

# 手機簡化版切換：用 selectbox 取代橫向 radio（比較不擠）
mobile_mode = st.toggle("📱 手機簡化版（建議手機開啟）", value=False)

with st.expander("Click to expand day settings", expanded=True):
    header = st.columns([1, 1, 4])
    with header[0]:
        st.markdown("**Date**")
    with header[1]:
        st.markdown("**Weekday**")
    with header[2]:
        st.markdown("**Option**")

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
            key = f"choice_{year}_{month}_{day}"
            if key not in st.session_state:
                st.session_state[key] = "Time-1"

            if mobile_mode:
                # 手機簡化版：用 selectbox，比較省空間
                st.selectbox(
                    "Option",
                    OPTION_LABELS,
                    key=key,
                    label_visibility="collapsed",
                )
            else:
                # 桌機版：維持原本橫向 radio
                st.radio(
                    "Option",
                    OPTION_LABELS,
                    key=key,
                    label_visibility="collapsed",
                    horizontal=True
                )

        # 每週結尾畫一條線，比較好讀
        if weekday == 6:
            st.markdown(
                "<hr style='border: 0; border-top: 1px solid #555;'>",
                unsafe_allow_html=True
            )

st.markdown("---")

def generate_schedule(year, month):
    output = []
    parsed = {}

    # 解析時間組合
    for k, v in st.session_state.time_sets.items():
        parsed[k] = [t.strip() for t in v.split(",") if t.strip()]

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
            formatted = " ".join(fmt.format(t) for t in times)
            line = f"{month}/{d} ({wd}) {formatted}"

        output.append(line)
        if weekday == 6:
            # 每週空一行
            output.append("")

    return "\n".join(output)

if st.button("Generate"):
    txt = generate_schedule(year, month)
    st.subheader("Preview")
    st.code(txt, language="text")
