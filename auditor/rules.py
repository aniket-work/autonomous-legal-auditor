from dataclasses import dataclass
from typing import List, Optional

@dataclass
class ComplianceRule:
    id: str
    category: str
    description: str
    severity: str  # "CRITICAL", "HIGH", "MEDIUM", "LOW"
    check_logic: str # Description of logic for simulation

RULES_DB = [
    ComplianceRule(
        id="PAY-001",
        category="Payment Terms",
        description="Payment terms must not exceed 45 days upon receipt of invoice.",
        severity="HIGH",
        check_logic="max_days_check"
    ),
    ComplianceRule(
        id="LIAB-001",
        category="Liability",
        description="Liability cap must be present and mutually agreed.",
        severity="CRITICAL",
        check_logic="liability_cap_exists"
    ),
    ComplianceRule(
        id="TERM-001",
        category="Termination",
        description="Termination for convenience requires at least 30 days notice.",
        severity="MEDIUM",
        check_logic="termination_notice_check"
    ),
    ComplianceRule(
        id="GOV-001",
        category="Governing Law",
        description="Governing law must be defined (Preferred: NY, DE, CA).",
        severity="HIGH",
        check_logic="governing_law_check_us"
    ),
    ComplianceRule(
        id="NDA-001",
        category="Confidentiality",
        description="Confidentiality obligations must survive termination for at least 3 years.",
        severity="MEDIUM",
        check_logic="confidentiality_survival_check"
    )
]
