import random
import time
from typing import Dict, List, Any
from .rules import RULES_DB, ComplianceRule

class ContractAnalyzer:
    def __init__(self):
        self.rules = RULES_DB

    def analyze_contract(self, contract_text: str) -> Dict[str, Any]:
        """
        Simulates the analysis of a legal contract against the rules DB.
        In a real-world scenario, this would use an LLM/NLP.
        """
        results = {
            "metadata": {
                "contract_length": len(contract_text),
                "timestamp": time.time(),
                "status": "COMPLETED"
            },
            "findings": [],
            "score": 100
        }

        # Simulate processing time for realism in UI
        time.sleep(0.5) 

        for rule in self.rules:
            # Simulation logic: Randomly pass/fail for demo purposes context
            # In production, we'd use regex or LLM extraction here.
            
            # Deterministic simulation based on rule ID char sum for consistency in demo
            has_violation = (sum(ord(c) for c in rule.id) % 5 == 0) 
            
            if has_violation:
                results["findings"].append({
                    "rule_id": rule.id,
                    "status": "FAIL",
                    "severity": rule.severity,
                    "detail": f"Violation detected: {rule.description}"
                })
                # Deduct score
                deduction = {"CRITICAL": 20, "HIGH": 10, "MEDIUM": 5, "LOW": 2}
                results["score"] -= deduction.get(rule.severity, 0)
            else:
                results["findings"].append({
                    "rule_id": rule.id,
                    "status": "PASS",
                    "severity": rule.severity,
                    "detail": "Compliant."
                })
        
        results["score"] = max(0, results["score"])
        return results
