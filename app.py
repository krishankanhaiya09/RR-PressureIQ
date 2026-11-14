
import streamlit as st
import pandas as pd

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="RR PressureIQ | Cricket Analytics",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =====================================================
# RAJASTHAN ROYALS PINK & WHITE THEME
# =====================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #fff7fa;
    color: #25213b;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1450px;
}

[data-testid="stHeader"] {
    background: #fff7fa;
}

h1, h2, h3, h4, p, label {
    color: #25213b;
}

.hero {
    background: linear-gradient(120deg, #e91e63, #9c174d);
    border-radius: 20px;
    padding: 35px;
    margin-bottom: 25px;
    box-shadow: 0 8px 25px rgba(233,30,99,0.18);
}

.hero h1 {
    font-size: 42px;
    font-weight: 800;
    color: white !important;
}

.hero p {
    color: #ffe5ef !important;
}

.hero-tag {
    color: #ffffff;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 2px;
}

.section-title {
    font-size: 23px;
    font-weight: 800;
    color: #9c174d;
    margin-top: 20px;
    margin-bottom: 15px;
}

.metric-card {
    background: white;
    border: 1px solid #f5c5d7;
    border-radius: 15px;
    padding: 20px;
    min-height: 115px;
    box-shadow: 0 4px 15px rgba(156,23,77,0.06);
}

.metric-label {
    color: #777085;
    font-size: 13px;
    font-weight: 600;
}

.metric-value {
    color: #9c174d;
    font-size: 29px;
    font-weight: 800;
    margin-top: 8px;
}

.metric-sub {
    color: #e91e63;
    font-size: 11px;
    margin-top: 4px;
}

.player-card, .info-card {
    background: white;
    border: 1px solid #f3c3d5;
    border-radius: 14px;
    padding: 18px;
    margin-bottom: 12px;
    box-shadow: 0 4px 15px rgba(156,23,77,0.05);
}

.player-rank {
    color: #e91e63;
    font-size: 13px;
    font-weight: 800;
}

.player-name {
    color: #25213b;
    font-size: 17px;
    font-weight: 700;
    margin-top: 5px;
}

.player-score {
    color: #9c174d;
    font-size: 24px;
    font-weight: 800;
}

.info-card h3 {
    color: #c2185b;
    font-size: 17px;
}

.info-card p, .info-card li {
    color: #5c566b;
    font-size: 14px;
    line-height: 1.8;
}

[data-testid="stMetric"] {
    background: white;
    border: 1px solid #f3c3d5;
    border-radius: 14px;
}

[data-testid="stMetricLabel"] {
    color: #777085;
}

[data-testid="stMetricValue"] {
    color: #9c174d;
}

[data-testid="stSidebar"] {
    background: #fff0f5;
    border-right: 1px solid #f3c3d5;
}

.stTabs [data-baseweb="tab"] {
    color: #5c566b;
    font-weight: 700;
}

.stTabs [aria-selected="true"] {
    color: #e91e63 !important;
}

.stButton button, .stDownloadButton button {
    background: #e91e63;
    color: white;
    border: none;
    border-radius: 9px;
    font-weight: 700;
}

.stButton button:hover, .stDownloadButton button:hover {
    background: #ad1457;
    color: white;
    border: none;
}

[data-testid="stDataFrame"] {
    border: 1px solid #f3c3d5;
    border-radius: 12px;
}

.stAlert {
    border-radius: 12px;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


# =====================================================
# DATA LOADING
# =====================================================
@st.cache_data
def load_data():
    batters = pd.read_csv("outputs/final_top10_batters.csv")
    bowlers = pd.read_csv("outputs/final_top10_bowlers.csv")
    pressure = pd.read_csv("outputs/combined_pressure.csv")
    normal = pd.read_csv("outputs/normal_deliveries.csv")
    return batters, bowlers, pressure, normal


# =====================================================
# REUSABLE FUNCTIONS
# =====================================================
def metric_card(label, value, subtitle):
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
        <div class="metric-sub">{subtitle}</div>
    </div>
    """, unsafe_allow_html=True)


def player_cards(data, name_column):
    for _, player in data.iterrows():
        score = float(player["final_score"])
        rank = int(player["rank"])

        st.markdown(f"""
        <div class="player-card">
            <div style="display:flex;justify-content:space-between;align-items:center;">
                <div>
                    <div class="player-rank">RANK #{rank}</div>
                    <div class="player-name">{player[name_column]}</div>
                </div>
                <div class="player-score">{score:.2f}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)


def ranking_chart(data, name_column):
    chart = data.sort_values("final_score", ascending=True)
    st.bar_chart(
        chart.set_index(name_column)["final_score"],
        horizontal=True
    )


# =====================================================
# HERO SECTION
# =====================================================
st.markdown("""
<div class="hero">
    <div class="hero-tag">RAJASTHAN ROYALS • DATA ANALYTICS PROJECT</div>
    <h1>🏏 RR PressureIQ</h1>
    <p>
        Identifying the most reliable batters and bowlers
        under high-pressure cricket situations.
    </p>
    <div style="margin-top:20px;color:#ff7581;font-weight:700;">
        DATA-DRIVEN PLAYER EVALUATION | SUPERR SELECTOR SEASON 2
    </div>
</div>
""", unsafe_allow_html=True)


# =====================================================
# MAIN APPLICATION
# =====================================================
try:
    batters, bowlers, pressure, normal = load_data()

    # Basic validation
    required_batter = {"rank", "striker_name", "final_score"}
    required_bowler = {"rank", "bowler_name", "final_score"}

    if not required_batter.issubset(batters.columns):
        st.error("Batter ranking CSV is missing required columns.")
        st.stop()

    if not required_bowler.issubset(bowlers.columns):
        st.error("Bowler ranking CSV is missing required columns.")
        st.stop()

    # =================================================
    # SIDEBAR
    # =================================================
    st.sidebar.title("🏏 PressureIQ")
    st.sidebar.caption("Cricket Intelligence Dashboard")
    st.sidebar.divider()

    page = st.sidebar.radio(
        "NAVIGATION",
        [
            "Overview",
            "Top Batters",
            "Top Bowlers",
            "Methodology",
            "Data & Limitations"
        ]
    )

    st.sidebar.divider()
    st.sidebar.markdown("### Project Information")
    st.sidebar.write("**Project:** RR PressureIQ")
    st.sidebar.write("**Sport:** Cricket / T20")
    st.sidebar.write("**Analysis:** Pressure vs Normal")
    st.sidebar.write("**Technology:** Python, Pandas, Streamlit")

    # =================================================
    # OVERVIEW
    # =================================================
    if page == "Overview":

        st.markdown('<div class="section-title">📊 Performance Overview</div>',
                    unsafe_allow_html=True)

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            metric_card("Pressure Deliveries", f"{len(pressure):,}",
                        "High-pressure dataset")

        with c2:
            metric_card("Normal Deliveries", f"{len(normal):,}",
                        "Baseline dataset")

        with c3:
            metric_card("Top Batters", str(len(batters)),
                        "Qualified players")

        with c4:
            metric_card("Top Bowlers", str(len(bowlers)),
                        "Qualified players")

        st.markdown('<div class="section-title">🏆 Leading Performers</div>',
                    unsafe_allow_html=True)

        left, right = st.columns(2)

        with left:
            st.markdown("### 🏏 Top Pressure Batter")
            top = batters.iloc[0]
            st.markdown(f"""
            <div class="info-card">
                <div style="color:#ff6372;font-weight:800;">RANK #1 BATTER</div>
                <h2 style="color:white;">{top['striker_name']}</h2>
                <div style="font-size:32px;font-weight:800;color:#ff6372;">
                    {float(top['final_score']):.2f}
                </div>
                <p>Final Pressure Performance Score</p>
            </div>
            """, unsafe_allow_html=True)

        with right:
            st.markdown("### 🎯 Top Pressure Bowler")
            top = bowlers.iloc[0]
            st.markdown(f"""
            <div class="info-card">
                <div style="color:#ff6372;font-weight:800;">RANK #1 BOWLER</div>
                <h2 style="color:white;">{top['bowler_name']}</h2>
                <div style="font-size:32px;font-weight:800;color:#ff6372;">
                    {float(top['final_score']):.2f}
                </div>
                <p>Final Pressure Performance Score</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<div class="section-title">📈 Top 10 Performance Comparison</div>',
                    unsafe_allow_html=True)

        t1, t2 = st.tabs(["Batters", "Bowlers"])

        with t1:
            ranking_chart(batters, "striker_name")

        with t2:
            ranking_chart(bowlers, "bowler_name")

        st.caption(
            "Scores are comparative ranking scores generated by the project's "
            "pressure-performance methodology."
        )

    # =================================================
    # BATTERS
    # =================================================
    elif page == "Top Batters":

        st.markdown('<div class="section-title">🏏 Top 10 Batters Under Pressure</div>',
                    unsafe_allow_html=True)

        st.write(
            "Players ranked using pressure performance, improvement over "
            "normal conditions, consistency and sample size."
        )

        player_cards(batters, "striker_name")

        st.markdown("### Complete Batter Ranking")

        st.dataframe(
            batters.rename(columns={
                "rank": "Rank",
                "striker_name": "Player",
                "final_score": "Final Score"
            }),
            use_container_width=True,
            hide_index=True
        )

        st.markdown("### Performance Score Chart")
        ranking_chart(batters, "striker_name")

        st.download_button(
            "⬇️ Download Batter Rankings",
            batters.to_csv(index=False),
            "RR_PressureIQ_Top_Batters.csv",
            "text/csv"
        )

    # =================================================
    # BOWLERS
    # =================================================
    elif page == "Top Bowlers":

        st.markdown('<div class="section-title">🎯 Top 10 Bowlers Under Pressure</div>',
                    unsafe_allow_html=True)

        st.write(
            "Bowlers evaluated using economy rate, wicket rate, dot-ball "
            "percentage, improvement and consistency."
        )

        player_cards(bowlers, "bowler_name")

        st.markdown("### Complete Bowler Ranking")

        st.dataframe(
            bowlers.rename(columns={
                "rank": "Rank",
                "bowler_name": "Player",
                "final_score": "Final Score"
            }),
            use_container_width=True,
            hide_index=True
        )

        st.markdown("### Performance Score Chart")
        ranking_chart(bowlers, "bowler_name")

        st.download_button(
            "⬇️ Download Bowler Rankings",
            bowlers.to_csv(index=False),
            "RR_PressureIQ_Top_Bowlers.csv",
            "text/csv"
        )

    # =================================================
    # METHODOLOGY
    # =================================================
    elif page == "Methodology":

        st.markdown('<div class="section-title">🧠 Research Methodology</div>',
                    unsafe_allow_html=True)

        st.markdown("""
        <div class="info-card">
            <h3>1. Objective</h3>
            <p>
            The objective of RR PressureIQ is to identify cricketers who
            maintain reliable performance in difficult match situations.
            Instead of evaluating players only through overall statistics,
            the system compares their pressure performance against their
            normal performance.
            </p>
        </div>

        <div class="info-card">
            <h3>2. Dataset and Scope</h3>
            <p>
            The analysis uses the supplied ball-by-ball cricket dataset,
            along with match and competition information. The competition
            scope includes IPL seasons from 2022 to 2026 and available T20I
            matches in the supplied data. Only the first two innings are
            considered; Super Overs are excluded.
            </p>
        </div>

        <div class="info-card">
            <h3>3. Defining Pressure Situations</h3>
            <p>A delivery is classified as a pressure delivery if either condition is met:</p>
            <ul>
                <li><b>Death Overs:</b> Overs 16 to 20.</li>
                <li><b>High-Pressure Chase:</b> Second-innings delivery with required run rate of at least 10.</li>
            </ul>
            <p>
            The two conditions are combined and duplicate deliveries are
            counted only once. Super Overs are excluded.
            </p>
        </div>

        <div class="info-card">
            <h3>4. Normal Performance Baseline</h3>
            <p>
            Deliveries not classified as pressure deliveries are used as
            the normal-performance baseline. Player statistics under
            pressure are compared with these baseline statistics to
            estimate performance improvement or decline.
            </p>
        </div>

        <div class="info-card">
            <h3>5. Batter Evaluation Metrics</h3>
            <ul>
                <li><b>Strike Rate:</b> Runs scored per 100 balls faced.</li>
                <li><b>Batting Average:</b> Runs scored per dismissal.</li>
                <li><b>Boundary Percentage:</b> Contribution from boundaries.</li>
                <li><b>Pressure Improvement:</b> Change in batting metrics compared with normal conditions.</li>
            </ul>
        </div>

        <div class="info-card">
            <h3>6. Bowler Evaluation Metrics</h3>
            <ul>
                <li><b>Economy Rate:</b> Runs conceded per over.</li>
                <li><b>Wicket Rate:</b> Wickets taken relative to legal balls.</li>
                <li><b>Dot Ball Percentage:</b> Share of dot balls among legal deliveries.</li>
                <li><b>Pressure Improvement:</b> Change in bowling metrics compared with normal conditions.</li>
            </ul>
        </div>

        <div class="info-card">
            <h3>7. Scoring Model</h3>
            <p>
            Metrics are converted into comparable percentile-based scores.
            The final score combines four components:
            </p>
            <ul>
                <li>Pressure Performance — <b>40%</b></li>
                <li>Pressure Improvement — <b>35%</b></li>
                <li>Consistency — <b>15%</b></li>
                <li>Sample Size — <b>10%</b></li>
            </ul>
            <p>
            Batting pressure performance combines strike rate (35%),
            average (30%), boundary contribution (20%) and pressure balls
            (15%). Bowling pressure performance combines economy (30%),
            wicket rate (30%), dot-ball percentage (25%) and pressure
            legal balls (15%).
            </p>
            <p>
            Batting improvement combines strike-rate gain (50%), average
            gain (30%) and boundary-percentage gain (20%). Bowling
            improvement combines economy improvement (50%), wicket-rate
            improvement (30%) and dot-ball improvement (20%).
            </p>
        </div>

        <div class="info-card">
            <h3>8. Eligibility and Fairness</h3>
            <p>
            To reduce unreliable rankings from very small samples, batters
            must have at least 60 pressure balls, 60 normal balls and
            3 pressure matches. Bowlers follow the corresponding legal-ball
            requirements. Player results across formats are combined using
            square-root pressure-sample weights.
            </p>
        </div>

        <div class="info-card">
            <h3>9. Consistency Measurement</h3>
            <p>
            Consistency is based on the variation in match-level
            performance. Players with lower match-to-match standard
            deviation receive better consistency rankings.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Final Score Formula")

        st.latex(
            r"FinalScore = 0.40P + 0.35I + 0.15C + 0.10S"
        )

        st.caption(
            "P = Pressure Performance, I = Improvement, "
            "C = Consistency, S = Sample Size."
        )

    # =================================================
    # DATA & LIMITATIONS
    # =================================================
    elif page == "Data & Limitations":

        st.markdown('<div class="section-title">📁 Dataset & Reliability</div>',
                    unsafe_allow_html=True)

        st.markdown("### Dataset Summary")

        summary = pd.DataFrame({
            "Dataset": [
                "Combined Pressure Deliveries",
                "Normal Deliveries",
                "Top 10 Batter Rankings",
                "Top 10 Bowler Rankings"
            ],
            "Records": [
                f"{len(pressure):,}",
                f"{len(normal):,}",
                len(batters),
                len(bowlers)
            ]
        })

        st.dataframe(summary, use_container_width=True, hide_index=True)

        st.markdown("### Important Limitations")

        st.markdown("""
        <div class="info-card">
            <h3>1. Pressure Definition</h3>
            <p>
            The required-run-rate threshold of 10 is a simplified
            definition. It may classify some early chase situations as
            pressure even when the match context is not necessarily tense.
            </p>
        </div>

        <div class="info-card">
            <h3>2. Match Context</h3>
            <p>
            The model does not fully account for pitch conditions,
            opposition strength, venue, player role, or exact match
            importance.
            </p>
        </div>

        <div class="info-card">
            <h3>3. Data Coverage</h3>
            <p>
            Pressure and normal datasets do not have identical match
            coverage. Therefore, comparisons may be influenced by
            differences in available matches and player opportunities.
            </p>
        </div>

        <div class="info-card">
            <h3>4. Revised Matches</h3>
            <p>
            DLS or revised-overs matches are excluded from the
            high-pressure chase calculation to avoid applying a standard
            20-over assumption to revised targets.
            </p>
        </div>

        <div class="info-card">
            <h3>5. Interpretation</h3>
            <p>
            The final score is a comparative analytical score, not a
            guarantee of future performance. Rankings should support
            scouting decisions rather than replace cricket expertise.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Technology Stack")

        st.write(
            "**Python** · **Pandas** · **NumPy** · "
            "**Streamlit** · **Matplotlib**"
        )

    # =================================================
    # FOOTER
    # =================================================
    st.divider()

    st.markdown("""
    <div style="text-align:center;padding:20px;color:#8290aa;">
        <b style="color:#ff6372;">RR PressureIQ</b><br>
        Data-Driven Cricket Performance Intelligence<br>
        <small>SupeRR Selector Season 2 | Built with Python & Streamlit</small>
    </div>
    """, unsafe_allow_html=True)


except FileNotFoundError as e:
    st.error(f"Required dataset not found: {e}")
    st.info(
        "Ensure the outputs folder contains all four required CSV files."
    )

except Exception as e:
    st.error(f"Dashboard error: {e}")
