# 🔍 AgentFlow Inspector

**An Interactive Dashboard for AI Agent Trace Inspection and Analysis**

AgentFlow Inspector is a Python-based, offline Streamlit application designed to help developers inspect and analyze structured workflow trace data.

It allows users to upload JSON or JSONL trace files, explore execution records, identify potential issues using rule-based checks, visualize status and timing information, and export reports for further analysis.

## ✨ Features

- 📂 **JSON/JSONL Upload:** Load trace data from local files.
- 🧪 **Demo Trace:** Explore the dashboard using sample trace data.
- 🔎 **Search:** Find relevant information within trace records.
- 📋 **Trace Inspection:** View structured records and raw JSON data.
- ⚠️ **Failure Detection:** Identify records marked as failures using rule-based checks.
- 🔁 **Duplicate Detection:** Flag duplicate records based on the implemented detection rules.
- ⏱️ **Slow Operation Detection:** Identify potentially slow operations using timing rules.
- 📊 **Interactive Visualizations:** Explore status and execution timing through Plotly charts.
- 📥 **Report Export:** Download analysis results in CSV and JSON formats.
- 🖥️ **Offline Dashboard:** Inspect uploaded data locally without requiring an external AI API connection.

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- Plotly
- JSON / JSONL

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/RealWajiha/AgentFlow-Inspector.git
cd AgentFlow-Inspector
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to access the dashboard.

## 📖 How to Use

1. Launch the Streamlit application.
2. Upload a JSON or JSONL trace file, or use the available demo trace.
3. Search and inspect the available trace records.
4. Review the rule-based checks for failures, duplicates, and slow operations.
5. Explore the status and timing charts.
6. Download the available reports in CSV or JSON format.

## 🎯 Project Objective

The goal of AgentFlow Inspector is to make structured trace data easier to explore and analyze through a simple, interactive interface.

This project demonstrates practical skills in Python application development, data processing, rule-based analysis, visualization, and report generation.

## 🔮 Future Improvements

- Integration with real AI agent tracing frameworks.
- Live trace ingestion and monitoring.
- More configurable detection rules.
- Advanced execution timelines and trace relationships.
- Additional performance metrics and reporting options.

*These are potential future enhancements, not claims about currently implemented features.*

## 👩‍💻 Author

**Wajiha Fareed**

Aspiring AI Engineer | Python | Machine Learning | Generative AI

- GitHub: https://github.com/RealWajiha
- LinkedIn: https://www.linkedin.com/in/wajiha-fareed/

## 📄 License

No license is specified here. Add a `LICENSE` file if you decide to publish the project under a particular open-source license.
