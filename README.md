# Autonomous Legal Contract Auditor

![Title](https://raw.githubusercontent.com/aniket-work/autonomous-legal-auditor/main/images/title-animation.gif)

## Overview
The **Autonomous Legal Contract Auditor** is an experimental AI agent designed to review legal service agreements against corporate compliance policies. By simulating the reasoning capabilities of a legal associate, it identifies critical risks (e.g., missing liability caps, extended payment terms) in real-time.

> [!NOTE]
> This project is a Proof of Concept (PoC) demonstrating the potential of agentic workflows in the legal tech domain. It is not intended for production legal advice.

## Key Features
- **Policy-Driven Analysis**: Checks contracts against a configurable rule engine.
- **Risk Scoring**: specific severity weights (CRITICAL, HIGH, MEDIUM).
- **Audit Trails**: Generates detailed, flagged reports for human review.

## Architecture
![Architecture](https://raw.githubusercontent.com/aniket-work/autonomous-legal-auditor/main/images/architecture_diagram.png)

## Installation

```bash
git clone https://github.com/aniket-work/autonomous-legal-auditor.git
cd autonomous-legal-auditor
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## How It Works
1. **Ingestion**: The agent reads the raw contract text.
2. **Rule Matching**: Each clause is evaluated against `auditor/rules.py`.
3. **Scoring**: A composite risk score is calculated based on violations.
4. **Reporting**: A terminal-based UI presents the findings.

## Disclaimer
The views and opinions expressed here are solely my own and do not represent the views, positions, or opinions of my employer or any organization I am affiliated with. The content is based on my personal experience and experimentation.
