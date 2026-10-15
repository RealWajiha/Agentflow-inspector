import json
import html
import pandas as pd
import streamlit as st
import plotly.express as px

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="AgentFlow Inspector",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# PREMIUM NEON DARK THEME
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --pink: #ff3d9a;
    --purple: #a855f7;
    --cyan: #20d9f2;
    --bg: #080611;
    --panel: #100b20;
    --muted: #b5a9d2;
}

.stApp {
    background:
        radial-gradient(ellipse at 85% 0%, #36102f 0%, transparent 35%),
        radial-gradient(ellipse at 0% 100%, #210b2d 0%, transparent 35%),
        var(--bg);
    color: #f7f2ff;
    font-family: 'Inter', sans-serif;
}

[data-testid="stHeader"] {
    background: rgba(8, 6, 17, 0.96);
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #10091e, #0b0815 75%, #19081d);
    border-right: 1px solid #48204f;
}

[data-testid="stSidebar"] * {
    color: #eee3ff;
}

.block-container {
    padding-top: 1.8rem;
    padding-bottom: 3rem;
    max-width: 1600px;
}

h1, h2, h3, p, label {
    color: #f7f2ff;
}

.hero {
    position: relative;
    overflow: hidden;
    padding: 29px 30px;
    border: 1px solid #702154;
    border-radius: 22px;
    background:
        radial-gradient(ellipse at 80% 0%, #55113f 0%, transparent 50%),
        linear-gradient(110deg, #200b25, #100b20 70%, #210d2d);
    box-shadow: 0 0 32px #ff248b12, inset 0 1px #ffffff0b;
    margin-bottom: 25px;
}

.hero:after {
    content: "";
    position: absolute;
    width: 360px;
    height: 150px;
    right: -55px;
    top: -70px;
    border: 2px solid #ff3d9a38;
    border-radius: 50%;
    transform: rotate(-17deg);
    box-shadow: 0 20px 0 #a855f718, 0 40px 0 #ff3d9a15;
    pointer-events: none;
}

.brand-icon {
    display: inline-flex;
    width: 65px;
    height: 65px;
    align-items: center;
    justify-content: center;
    border-radius: 18px;
    font-size: 35px;
    background: linear-gradient(135deg, #ff3d9a, #7628d9);
    box-shadow: 0 0 28px #ff3d9a40;
    flex-shrink: 0;
}

.hero-title {
    font-size: clamp(25px, 3vw, 36px);
    font-weight: 800;
    letter-spacing: -1.2px;
    margin: 0;
}

.gradient-text {
    background: linear-gradient(90deg, #ff4b9b, #c084fc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtext {
    color: #c2b4dc;
    margin-top: 8px;
    font-size: 14px;
}

.metric-card {
    position: relative;
    overflow: hidden;
    min-height: 132px;
    border-radius: 19px;
    padding: 21px;
    border: 1px solid #572044;
    background: linear-gradient(135deg, #260c27, #120b20 78%);
}

.metric-card.purple {
    border-color: #48246f;
    background: linear-gradient(135deg, #1d123a, #100b20);
}

.metric-card.cyan {
    border-color: #075269;
    background: linear-gradient(135deg, #082739, #0b1020);
}

.metric-label {
    color: #d6c9e8;
    font-size: 13px;
}

.metric-number {
    font-size: clamp(22px, 2.2vw, 32px);
    font-weight: 800;
    margin-top: 10px;
    letter-spacing: -1px;
    overflow-wrap: anywhere;
}

.metric-icon {
    float: right;
    width: 43px;
    height: 43px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 13px;
    font-size: 22px;
    background: linear-gradient(135deg, #8b1769, #42134c);
}

.metric-card.purple .metric-icon {
    background: linear-gradient(135deg, #7133d9, #2b1a62);
}

.metric-card.cyan .metric-icon {
    background: linear-gradient(135deg, #087c98, #103550);
}

.panel {
    padding: 22px;
    border: 1px solid #392044;
    border-radius: 20px;
    background: linear-gradient(145deg, #130d23, #0c0918);
    margin-top: 22px;
    box-shadow: 0 12px 40px #00000016;
}

.panel-heading {
    font-size: 20px;
    font-weight: 700;
}

.panel-subtitle {
    font-size: 12px;
    color: #aa9bc5;
    margin-top: 4px;
}

.finding {
    padding: 16px 18px;
    border-radius: 14px;
    background: linear-gradient(100deg, #103a40, #0c202e);
    border: 1px solid #15515b;
    color: #d9faff;
    margin: 14px 0;
}

.finding.warning {
    background: linear-gradient(100deg, #45142e, #24132e);
    border-color: #87305e;
}

.stButton > button,
.stDownloadButton > button {
    border: 1px solid #ed3c9b;
    border-radius: 12px;
    color: white !important;
    font-weight: 600;
    background: linear-gradient(105deg, #e52e87, #7727c9);
    transition: 0.2s ease;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    border-color: #ff8bc7;
    color: white !important;
    box-shadow: 0 0 22px #ed3c9b40;
    transform: translateY(-1px);
}

/* SEARCH INPUT */
.stTextInput input,
.stTextArea textarea {
    background: linear-gradient(110deg, #1b102b, #100b20) !important;
    color: #f8edff !important;
    border: 1px solid #a52a85 !important;
    border-radius: 12px !important;
    caret-color: #ff3d9a !important;
}

.stTextInput input:focus,
.stTextArea textarea:focus {
    border-color: #ff3d9a !important;
    box-shadow: 0 0 14px #ff3d9a35 !important;
}

.stTextInput input::placeholder {
    color: #9d8bb9 !important;
}

/* FILE UPLOADER */
[data-testid="stFileUploader"] {
    background: linear-gradient(120deg, #1b102b, #100b20) !important;
    border: 1px dashed #c23891 !important;
    border-radius: 14px !important;
    padding: 12px;
}

[data-testid="stFileUploader"] section {
    background: transparent !important;
}

[data-testid="stFileUploader"] button {
    background: linear-gradient(100deg, #d92c88, #7627c9) !important;
    color: white !important;
    border: 1px solid #ff59b0 !important;
}

/* DARK TABLE CONTAINER */
[data-testid="stDataFrame"],
[data-testid="stTable"] {
    background: #100b20 !important;
    border: 1px solid #64245e !important;
    border-radius: 14px !important;
    overflow: hidden !important;
}

[data-testid="stDataFrame"] iframe {
    background: #100b20 !important;
}

/* EXPANDER AND RAW JSON */
[data-testid="stExpander"] {
    background: linear-gradient(120deg, #160e27, #100b20) !important;
    border: 1px solid #57245e !important;
    border-radius: 13px !important;
}

[data-testid="stExpander"] summary {
    color: #f3dfff !important;
}

[data-testid="stCode"],
[data-testid="stCodeBlock"] {
    background: #0b0815 !important;
    border: 1px solid #422052 !important;
    border-radius: 10px !important;
}

/* ALERTS */
[data-testid="stAlert"] {
    background: linear-gradient(110deg, #171027, #10202b) !important;
    border: 1px solid #59305f !important;
    border-radius: 12px !important;
    color: #f5eaff !important;
}

/* SELECT BOXES */
[data-baseweb="select"] > div {
    background-color: #171026 !important;
    color: white !important;
    border-color: #49305c !important;
}

/* RADIO NAVIGATION */
[data-testid="stSidebar"] [data-testid="stRadio"] label {
    color: #e9dafa !important;
}

/* METRIC TEXT */
[data-testid="stMetric"] {
    background: linear-gradient(130deg, #1b102b, #100b20);
    border: 1px solid #48244f;
    border-radius: 12px;
    padding: 14px;
}

hr {
    border-color: #382044;
}

footer, #MainMenu {
    visibility: hidden;
}

@media (max-width: 700px) {
    .hero { padding: 20px 16px; }
    .panel { padding: 14px; }
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    st.markdown("""
    <div style="padding:10px 0 22px;">
      <div style="font-size:36px;">🔍</div>
      <div style="font-size:20px;font-weight:800;">
        AgentFlow <span style="color:#ff4b9b;">Inspector</span>
      </div>
      <div style="font-size:11px;color:#b5a5cc;margin-top:5px;">
        AI Workflow Debugger & Analyzer
      </div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "NAVIGATION",
        [
            "Dashboard",
            "Upload Traces",
            "Analysis",
            "Visualizations",
            "Reports",
        ],
        label_visibility="collapsed",
    )

    st.markdown("""
    <div style="
      margin-top:35px;padding:20px 15px;border-radius:18px;
      border:1px solid #71205c;
      background:linear-gradient(145deg,#310c32,#150b24);">
      <div style="font-size:25px;">🚀</div>
      <b>Better Insights<br>for Smarter AI Agents</b>
      <p style="color:#c0afd5;font-size:12px;line-height:1.7;margin-top:12px;">
      Inspect traces, identify failures and understand workflow performance.
      </p>
      <span style="font-size:10px;color:#ff75bc;">● LOCAL ANALYSIS</span>
    </div>
    """, unsafe_allow_html=True)

    st.caption("AgentFlow Inspector · Offline Edition")


# ============================================================
# HERO BANNER
# ============================================================
st.markdown("""
<div class="hero">
  <div style="display:flex;align-items:center;flex-wrap:wrap;gap:16px;">
    <div class="brand-icon">⌁</div>
    <div>
      <div class="hero-title">
        AgentFlow <span class="gradient-text">Inspector</span>
      </div>
      <div class="subtext">
        Offline AI workflow trace analysis — no API key required
      </div>
    </div>
  </div>
  <div style="text-align:right;color:#e9c8ef;font-size:13px;margin-top:18px;">
    <span class="gradient-text">Inspect</span> &nbsp;→&nbsp;
    <span class="gradient-text">Analyze</span> &nbsp;→&nbsp;
    <span class="gradient-text">Improve</span> ✦
  </div>
</div>
""", unsafe_allow_html=True)


# ============================================================
# SAMPLE TRACE
# ============================================================
SAMPLE_TRACE = [
    {
        "span_id": "1",
        "name": "load_input",
        "status": "success",
        "duration_ms": 120,
        "error": "",
    },
    {
        "span_id": "2",
        "name": "retrieve_documents",
        "status": "success",
        "duration_ms": 480,
        "error": "",
    },
    {
        "span_id": "3",
        "name": "generate_answer",
        "status": "failed",
        "duration_ms": 2100,
        "error": "Model execution failed",
    },
    {
        "span_id": "4",
        "name": "format_output",
        "status": "success",
        "duration_ms": 90,
        "error": "",
    },
]


# ============================================================
# SESSION STATE
# ============================================================
if "trace_df" not in st.session_state:
    st.session_state.trace_df = pd.DataFrame()

if "loaded_name" not in st.session_state:
    st.session_state.loaded_name = ""


def parse_trace(file):
    """Read a JSON or JSONL trace file."""
    content = file.getvalue().decode("utf-8-sig")

    if file.name.lower().endswith(".jsonl"):
        records = [
            json.loads(line)
            for line in content.splitlines()
            if line.strip()
        ]
    else:
        data = json.loads(content)

        if isinstance(data, dict):
            records = data.get(
                "spans",
                data.get("traces", [data]),
            )
        else:
            records = data

    if isinstance(records, dict):
        records = [records]

    if not isinstance(records, list):
        raise ValueError(
            "Expected a JSON list or an object containing spans."
        )

    return pd.DataFrame(records)


# ============================================================
# UPLOAD PAGE
# ============================================================
if page == "Upload Traces":
    st.markdown(
        '<div class="panel-heading">📤 Upload Workflow Traces</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="panel-subtitle">'
        'Import JSON or JSONL execution traces for local analysis.'
        '</div>',
        unsafe_allow_html=True,
    )

    uploaded = st.file_uploader(
        "Choose trace file",
        type=["json", "jsonl"],
        key="trace_upload",
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✨ Analyze Trace", use_container_width=True):
            if uploaded is None:
                st.warning("Please choose a JSON or JSONL file first.")
            else:
                try:
                    st.session_state.trace_df = parse_trace(uploaded)
                    st.session_state.loaded_name = uploaded.name
                    st.success(
                        f"Loaded {len(st.session_state.trace_df)} record(s)."
                    )
                except Exception as exc:
                    st.error(f"Could not read file: {exc}")

    with col2:
        if st.button("🧪 Load Demo Trace", use_container_width=True):
            st.session_state.trace_df = pd.DataFrame(SAMPLE_TRACE)
            st.session_state.loaded_name = "Built-in demo"
            st.success("Demo trace loaded.")

    st.markdown("""
    <div class="panel">
      <div class="panel-heading">📌 Supported Input</div>
      <div class="panel-subtitle">
      JSON arrays, JSONL records and objects containing a spans or traces list.
      </div>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# CURRENT DATA
# ============================================================
if not st.session_state.trace_df.empty:
    df = st.session_state.trace_df.copy()
else:
    df = pd.DataFrame()


# ============================================================
# DETECT COLUMNS AND CALCULATE METRICS
# ============================================================
duration_col = next(
    (
        col for col in ["duration_ms", "latency_ms", "duration"]
        if col in df.columns
    ),
    None,
)

status_col = next(
    (
        col for col in ["status", "state", "outcome"]
        if col in df.columns
    ),
    None,
)

error_col = next(
    (
        col for col in ["error", "error_message", "exception"]
        if col in df.columns
    ),
    None,
)

total = len(df)
failed_count = 0
average_duration = None

if status_col:
    failed_statuses = df[status_col].astype(str).str.lower().isin(
        ["error", "failed", "failure", "exception"]
    )
    failed_count = int(failed_statuses.sum())

if error_col:
    error_values = df[error_col]
    has_error = (
        error_values.notna()
        & error_values.astype(str).str.strip().ne("")
        & error_values.astype(str).str.lower().ne("none")
        & error_values.astype(str).str.lower().ne("nan")
    )
    failed_count = max(failed_count, int(has_error.sum()))

if duration_col:
    numeric_durations = pd.to_numeric(
        df[duration_col], errors="coerce"
    )
    if numeric_durations.notna().any():
        average_duration = numeric_durations.mean()


def metric_card(icon, label, value, theme=""):
    return f"""
    <div class="metric-card {theme}">
      <div class="metric-icon">{icon}</div>
      <div class="metric-label">{label}</div>
      <div class="metric-number">{value}</div>
    </div>
    """


# ============================================================
# METRIC CARDS
# ============================================================
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(
        metric_card("▶", "Total Operations", total),
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        metric_card("⚠", "Detected Failures", failed_count, "purple"),
        unsafe_allow_html=True,
    )

with c3:
    duration_text = (
        f"{average_duration:,.2f} ms"
        if average_duration is not None
        else "Not available"
    )

    st.markdown(
        metric_card("◷", "Average Duration", duration_text, "cyan"),
        unsafe_allow_html=True,
    )


# ============================================================
# DASHBOARD AND TRACE RECORDS
# ============================================================
if page in ["Dashboard", "Upload Traces"]:
    st.markdown("""
    <div class="panel">
      <div class="panel-heading">▤ &nbsp; Trace Records</div>
      <div class="panel-subtitle">
        Execution details from your workflow
      </div>
    </div>
    """, unsafe_allow_html=True)

    if df.empty:
        st.info(
            "No trace loaded yet. Open Upload Traces or load the demo."
        )

        if st.button("🧪 Load Demo Trace", key="demo_dashboard"):
            st.session_state.trace_df = pd.DataFrame(SAMPLE_TRACE)
            st.session_state.loaded_name = "Built-in demo"
            st.rerun()

    else:
        search = st.text_input(
            "⌕ Search records",
            placeholder="Search by operation, status or error...",
        )

        view = df.copy()

        if search:
            mask = view.astype(str).apply(
                lambda col: col.str.contains(
                    search,
                    case=False,
                    na=False,
                    regex=False,
                )
            ).any(axis=1)

            view = view[mask]

        # JSON objects/lists display as readable strings in the table.
        display_df = view.copy()

        for col in display_df.columns:
            display_df[col] = display_df[col].map(
                lambda value: json.dumps(value, ensure_ascii=False)
                if isinstance(value, (dict, list))
                else value
            )

        # Styled HTML table avoids the bright white default dataframe.
        if len(display_df.columns) <= 12:
            header_cells = "".join(
                f"<th>{html.escape(str(col))}</th>"
                for col in display_df.columns
            )

            rows_html = ""

            for index, (_, row) in enumerate(display_df.iterrows()):
                cells = "".join(
                    f"<td>{html.escape(str(value))}</td>"
                    for value in row
                )

                rows_html += (
                    f'<tr><td class="row-index">{index}</td>'
                    f'{cells}</tr>'
                )

            table_html = f"""
            <div style="
                overflow-x:auto;
                border:1px solid #64245e;
                border-radius:14px;
                background:#100b20;
                margin:12px 0 20px;
            ">
            <table style="
                width:100%;
                border-collapse:collapse;
                background:#100b20;
                color:#eadfff;
                font-family:Inter,sans-serif;
                font-size:12px;
            ">
            <thead>
              <tr>
                <th style="min-width:45px;">#</th>
                {header_cells}
              </tr>
            </thead>
            <tbody>{rows_html}</tbody>
            </table>
            </div>
            """

            st.markdown("""
            <style>
            table thead th {
                background: linear-gradient(100deg,#29113a,#1b1030);
                color: #f36ac0;
                font-weight: 700;
                text-align: left;
                padding: 14px 12px;
                border-bottom: 1px solid #63305f;
                white-space: nowrap;
            }
            table tbody td {
                padding: 14px 12px;
                border-bottom: 1px solid #30203f;
                background: #100b20;
                color: #e8dcfa;
                max-width: 320px;
                overflow-wrap: anywhere;
                vertical-align: top;
            }
            table tbody tr:nth-child(even) td {
                background: #171026;
            }
            table tbody tr:hover td {
                background: #261232;
            }
            table tbody td.row-index {
                color: #ff69b5;
                font-weight: 700;
            }
            </style>
            """, unsafe_allow_html=True)

            st.markdown(table_html, unsafe_allow_html=True)

        else:
            st.dataframe(
                display_df,
                use_container_width=True,
                hide_index=True,
            )

        with st.expander("⌘ View Raw Trace as JSON"):
            st.code(
                json.dumps(
                    df.to_dict(orient="records"),
                    indent=2,
                    default=str,
                ),
                language="json",
            )


# ============================================================
# ANALYSIS
# ============================================================
if page in ["Dashboard", "Analysis"]:
    st.markdown("""
    <div class="panel">
      <div class="panel-heading">💡 &nbsp; Initial Findings</div>
      <div class="panel-subtitle">
        Rule-based checks on your imported trace
      </div>
    """, unsafe_allow_html=True)

    if df.empty:
        st.markdown(
            '<div class="finding">'
            'ℹ️ Load a trace to generate findings.'
            '</div>',
            unsafe_allow_html=True,
        )

    elif failed_count:
        st.markdown(
            f'<div class="finding warning">'
            f'⚠️ Found {failed_count} record(s) with failure indicators. '
            f'Review the records for details.'
            f'</div>',
            unsafe_allow_html=True,
        )

    else:
        st.markdown(
            '<div class="finding">'
            '✓ No explicit failures detected in the available fields. '
            'This does not guarantee the workflow is error-free.'
            '</div>',
            unsafe_allow_html=True,
        )

    if not df.empty and "span_id" in df.columns:
        duplicate_count = int(
            df["span_id"].dropna().duplicated().sum()
        )

        if duplicate_count:
            st.warning(f"Duplicate span IDs detected: {duplicate_count}")

    if not df.empty and duration_col:
        durations = pd.to_numeric(df[duration_col], errors="coerce")
        slow_count = int((durations > 1000).sum())

        if slow_count:
            st.warning(
                f"Slow operations over 1000 ms: {slow_count}"
            )

    st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# VISUALIZATIONS
# ============================================================
if page in ["Dashboard", "Visualizations"]:
    if not df.empty:
        st.markdown("""
        <div class="panel">
          <div class="panel-heading">✧ &nbsp; Workflow Visualizations</div>
          <div class="panel-subtitle">
            Explore status distribution and operation timings
          </div>
        """, unsafe_allow_html=True)

        if status_col:
            status_df = (
                df[status_col]
                .fillna("unknown")
                .astype(str)
                .value_counts()
                .rename_axis("Status")
                .reset_index(name="Count")
            )

            fig = px.bar(
                status_df,
                x="Status",
                y="Count",
                color="Status",
                color_discrete_sequence=[
                    "#ff3d9a",
                    "#a855f7",
                    "#20d9f2",
                ],
            )

            fig.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font_color="#eee3ff",
                margin=dict(l=10, r=10, t=20, b=10),
            )

            st.plotly_chart(fig, use_container_width=True)

        if duration_col:
            chart_df = df.copy()

            chart_df["Duration (ms)"] = pd.to_numeric(
                chart_df[duration_col],
                errors="coerce",
            )

            chart_df["Operation"] = (
                chart_df["name"].astype(str)
                if "name" in chart_df.columns
                else [
                    f"Operation {i + 1}"
                    for i in range(len(chart_df))
                ]
            )

            fig = px.bar(
                chart_df,
                x="Operation",
                y="Duration (ms)",
                color="Duration (ms)",
                color_continuous_scale=[
                    "#6527b8",
                    "#ff3d9a",
                    "#20d9f2",
                ],
            )

            fig.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font_color="#eee3ff",
                margin=dict(l=10, r=10, t=20, b=10),
                coloraxis_showscale=False,
            )

            st.plotly_chart(fig, use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# REPORTS
# ============================================================
if page == "Reports":
    st.markdown(
        '<div class="panel-heading">📄 Export Analysis Report</div>',
        unsafe_allow_html=True,
    )

    if df.empty:
        st.info("Load a trace first using Upload Traces.")

    else:
        report = {
            "file": st.session_state.loaded_name,
            "total_operations": total,
            "detected_failures": failed_count,
            "average_duration_ms": (
                float(average_duration)
                if average_duration is not None
                else None
            ),
            "records": df.to_dict(orient="records"),
        }

        st.markdown("""
        <div class="panel">
          <div class="panel-heading">📦 Export Options</div>
          <div class="panel-subtitle">
            Download the currently loaded trace and analysis summary.
          </div>
        </div>
        """, unsafe_allow_html=True)

        st.download_button(
            "⬇ Download CSV",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name="agentflow_analysis.csv",
            mime="text/csv",
            use_container_width=True,
        )

        st.download_button(
            "⬇ Download JSON Report",
            data=json.dumps(
                report,
                indent=2,
                default=str,
            ),
            file_name="agentflow_report.json",
            mime="application/json",
            use_container_width=True,
        )


# ============================================================
# FOOTER
# ============================================================
st.markdown("""
<div style="
    text-align:center;
    padding:30px 0 5px;
    color:#88749f;
    font-size:11px;
    letter-spacing:1px;
">
AGENTFLOW INSPECTOR · OFFLINE TRACE ANALYTICS · NO API KEY
</div>
""", unsafe_allow_html=True)
