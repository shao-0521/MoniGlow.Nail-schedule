import streamlit as st
import calendar
from datetime import datetime
import base64

def get_base64_img(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

if "bg_left" not in st.session_state:
    st.session_state.bg_left = get_base64_img("cat.jpg")
if "bg_right" not in st.session_state:
    st.session_state.bg_right = get_base64_img("shao.jpg")
if "logo_img" not in st.session_state:
    st.session_state.logo_img = get_base64_img("moni_nail.jpg")

left_side_image_base64 = st.session_state.bg_left
right_side_image_base64 = st.session_state.bg_right
logo_base64 = st.session_state.logo_img

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
    </style>
    """,
    unsafe_allow_html=True
)

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

st.markdown("""
<div style="
    overflow: hidden;
    white-space: nowrap;
    width: 100%;
    box-sizing: border-box;
    margin-top: -5px;
">
    <div style="
        display: inline-block;
        padding-left: 100%;
        animation: marquee-multi 159s linear infinite;
        font-size: 18px;
        font-weight: 600;
    ">
        <span style="color:#ff99cc;">Who is the best nail artist? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (English)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#ffe066;">誰是最棒的美甲師？Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (繁體中文)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#66ffff;">邊個係最勁嘅美甲師？Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (粵語)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#ffb366;">誰是尚讚的美甲師？Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (台語)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#b3ff66;">誰係最好个美甲師？Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (客家話)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#ff66ff;">一番すごいネイリストは誰？Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (日文)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#66ccff;">Wer ist die beste Nagelkünstlerin? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (德文)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#ff6666;">가장 최고의 네일 아티스트는 누구? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (韓文)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#99ffcc;">Ai là thợ làm móng giỏi nhất? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (越南文)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#ffd1a9;">ช่างทำเล็บที่เก่งที่สุดคือใคร? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (泰文)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#ffeb3b;">¿Quién es la mejor artista de uñas? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (西班牙文)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#c39eff;">Siapakah artis kuku yang terbaik? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (馬來文/印尼文)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#80ff80;">Ποια είναι η καλύτερη τεχνίτρια νυχιών; Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (希臘文)</span>
        <span style="color:#ffccff;">Qui est la meilleure artiste des ongles ? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (法文)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#ffdd99;">Quem é a melhor artista de unhas? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (葡萄牙文)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#ccffcc;">Chi è la migliore artista delle unghie? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (義大利文)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#ff9999;">من هي أفضل فنانة أظافر؟ Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (阿拉伯文)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#99ddff;">En iyi tırnak sanatçısı kim? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (土耳其文)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#dd99ff;">Wie is de beste nagelartieste? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (荷蘭文)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#ffee99;">Kto jest najlepszą stylistką paznokci? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (波蘭文)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#ccffff;">Hvem er den bedste neglekunstner? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (丹麥文)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#ffcc99;">Hvem er den beste neglekunstneren? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (挪威文)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#ccff99;">Hver er besti neglalistamaðurinn? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (冰島文)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#99ffdd;">Kdo je nejlepší nehtová umělkyně? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (捷克文)</span>
        <span style="color:#ffcccc;">ʻO wai ka mea pena kuiʻī ʻoi loa? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (夏威夷語)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#ccffdd;">Kto je najlepšia nechtová umelkyňa? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (斯洛伐克文)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#ffccdd;">Katera je najboljša umetnica za nohte? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (斯洛維尼亞文)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#ddffcc;">Kuka on paras kynsitaiteilija? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (芬蘭文)</span>
        <span style="color:#ffccaa;">Cé hí an ealaíontóir ingne is fearr? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (愛爾蘭蓋爾語)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#ccddff;">Wien ass déi bescht Nagelkënschtlerin? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (盧森堡語)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#ffeecc;">Min hi l-aqwa arti tal-imsiemer? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (馬爾他語)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#ddccff;">Tko je najbolja umjetnica za nokte? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (克羅埃西亞語)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#ccffee;">Ko je najbolja umjetnica za nokte? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (波斯尼亞語)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#ffdddd;">সেরা নেইল আর্টিস্ট কে? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (孟加拉語)</span>
        <span style="color:#ffccb3;">Vem är den bästa nagelkonstnären? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (瑞典語)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#cce5ff;">Kas yra geriausia nagų meistrė? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (立陶宛語)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#ffccff;">Kes on parim küünekunstnik? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (愛沙尼亞語)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#e6ffcc;">Cine este cea mai bună artistă de unghii? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (羅馬尼亞語)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#ffd9cc;">Ко је најбоља уметница за нокте? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (塞爾維亞語)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#d9ccff;">Nor da eskuetako artista onena? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (巴斯克語)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#cce6ff;">Cò e an t-ealantaiche ìnean as fheàrr? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (蘇格蘭蓋爾語)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#ffcccc;">ນາງຊ່າງເຮັດເລັບທີ່ເກັ່ງທີ່ສຸດແມ່ນໃຜ? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (老撾語)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#e6ccff;">מי אמנית הציפורניים הטובה ביותר? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (希伯來語)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#ccffee;">بهترین هنرمند ناخن چه کسی است؟ Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (波斯語)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#ffebcc;">Iza mpanakanto tsara indrindra amin'ny hoho? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (馬達加斯加語)</span>&nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color:#d1ffc6;">Ubani umculi wezikhonkwane ohamba phambili? Moniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii (祖魯語)</span>
    </div>
</div>

<style>
@keyframes marquee-multi {
    0%   { transform: translate(0, 0); }
    100% { transform: translate(-100%, 0); }
}
</style>
""", unsafe_allow_html=True)

st.markdown("---")

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

with col_next:
    st.markdown("<div style='text-align:right;'>", unsafe_allow_html=True)
    if st.button("Next →"):
        if st.session_state.current_month == 12:
            st.session_state.current_month = 1
            st.session_state.current_year += 1
        else:
            st.session_state.current_month += 1
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

year = st.session_state.current_year
month = st.session_state.current_month
days_in_month = calendar.monthrange(year, month)[1]

st.markdown("---")

st.subheader("Customize Time Sets")
st.markdown(
    "<p style='font-size: 13px; color: #bbb; margin-top: -10px;'>The time can be changed manually, must comma &lt; , &gt; separated</p>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='font-size: 13px; color: #bbb; margin-top: -10px;'>Page refresh will clear the records</p>",
    unsafe_allow_html=True
)

if "time_sets" not in st.session_state:
    st.session_state.time_sets = {
        "Time-1": "10:30, 14:00, 17:30",
        "Time-2": "11:00, 14:30, 18:00",
        "Time-3": "10:00, 13:00, 16:30, 19:30",
    }

c1, c2, c3 = st.columns(3)
with c1:
    st.session_state.time_sets["Time-1"] = st.text_input("Time-1", st.session_state.time_sets["Time-1"])
with c2:
    st.session_state.time_sets["Time-2"] = st.text_input("Time-2", st.session_state.time_sets["Time-2"])
with c3:
    st.session_state.time_sets["Time-3"] = st.text_input("Time-3", st.session_state.time_sets["Time-3"])

st.markdown("---")

OPTION_LABELS = ["None", "Dayoff", "Time-1", "Time-2", "Time-3"]
WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def parse_time_sets():
    parsed = {}
    for k, v in st.session_state.time_sets.items():
        parsed[k] = [t.strip() for t in v.split(",") if t.strip()]
    return parsed

st.subheader("Daily Schedule Settings")

st.markdown(
    "<p style='font-size: 13px; color: #bbb; margin-top: -10px;'>Note:</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Selecting None displays nothing | Selecting Dayoff displays Dayoff</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Clicking the time button below, the time won't be displayed in the schedule</p>",
    unsafe_allow_html=True
)

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
            key = f"choice_{year}_{month}_{day}"
            if key not in st.session_state:
                st.session_state[key] = "Time-1"

            choice = st.radio("Option", OPTION_LABELS, key=key, label_visibility="collapsed", horizontal=True)
            
            if choice in parsed_time_sets:
                times = parsed_time_sets.get(choice, [])
                if times:
                    btn_cols = st.columns(len(times))
                    for i, t in enumerate(times):
                        with btn_cols[i]:
                            cb_key = f"cb_{year}_{month}_{day}_{t}"
                            st.checkbox(t, key=cb_key)

        if day != days_in_month:
            if weekday == 6:
                st.markdown(
                    """
                    <hr style='border: 1px solid #777; margin: 5px 0;'>
                    <hr style='border: 1px solid #777; margin: 5px 0;'>
                    <hr style='border: 1px solid #777; margin: 5px 0;'>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.markdown("----")

st.markdown("---")

def generate_schedule(year, month):
    output = []
    parsed = parse_time_sets()
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

        if choice == "Dayoff":
            if weekday == 6:  # Sunday
                output.append("")
            continue

        if choice == "None":
            line = f"{month}/{d} ({wd})"
        else:
            times = parsed.get(choice, [])
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
                line = f"{month}/{d} ({wd})"

        output.append(line)

        if weekday == 6:
            output.append("")

    return "\n".join(output)


if st.button("Generate"):
    txt = generate_schedule(year, month)
    st.subheader("Preview")
    st.code(txt, language="text")
