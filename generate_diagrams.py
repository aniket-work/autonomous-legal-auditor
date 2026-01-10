import base64
import requests
import os
import matplotlib.pyplot as plt
import numpy as np

# Ensure images directory exists
os.makedirs("images", exist_ok=True)

# 1. Generate Mermaid Diagrams
diagrams = {
    "architecture": """
    graph TB
        User[Legal Associate] -->|Uploads Contract| CLI[CLI Interface]
        CLI --> Agent[Audit Agent]
        subgraph Engine [Compliance Engine]
            Agent --> Rules[Rule DB]
            Agent --> NLP[Logic Simulator]
            Rules --> Logic[Scoring Model]
        end
        Logic -->|Risk Score| Report[Audit Report]
        Report --> CLI
    """,
    "sequence": """
    sequenceDiagram
        participant U as User
        participant A as Auditor Agent
        participant R as Rule Engine
        
        U->>A: Submit Contract
        A->>A: Parse Text
        loop Check Rules
            A->>R: Fetch Rule (ID)
            R-->>A: Rule Criteria
            A->>A: Evaluate Compliance
        end
        A->>U: Return Findings Table
    """,
    "flow": """
    flowchart LR
        A[Input Document] --> B{Parseable?}
        B -- Yes --> C[Extract Clauses]
        B -- No --> D[Error / OCR]
        C --> E[Compliance Check]
        E --> F[Generate Score]
        F --> G[Output Report]
    """
}

print("Generating Mermaid diagrams...")
for name, code in diagrams.items():
    try:
        encoded = base64.b64encode(code.encode("utf8")).decode("ascii")
        url = f"https://mermaid.ink/img/{encoded}"
        response = requests.get(url)
        if response.status_code == 200:
            with open(f"images/{name}_diagram.png", 'wb') as f:
                f.write(response.content)
            print(f" - Saved images/{name}_diagram.png")
        else:
            print(f" - Failed to generate {name}: {response.status_code}")
    except Exception as e:
        print(f" - Error generating {name}: {e}")

# 2. Generate Statistical Chart (Matplotlib)
print("Generating statistical charts...")
try:
    # Example: Risk Distribution Chart
    categories = ['Payment', 'Liability', 'Valid.', 'Gov. Law', 'Data Privacy']
    scores = [85, 40, 95, 100, 60]
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(categories, scores, color=['#4caf50', '#f44336', '#4caf50', '#4caf50', '#ffeb3b'])
    
    plt.axhline(y=50, color='gray', linestyle='--', alpha=0.5)
    plt.title('Compliance Score by Category (Last Run)', fontsize=14, fontweight='bold')
    plt.ylabel('Score (0-100)', fontsize=12)
    plt.ylim(0, 110)
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 2,
                f'{height}',
                ha='center', va='bottom')
    
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('images/stats_chart.png', dpi=100)
    print(" - Saved images/stats_chart.png")

except Exception as e:
    print(f" - Error generating chart: {e}")
