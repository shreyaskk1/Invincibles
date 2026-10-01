from dataclasses import dataclass


@dataclass(frozen=True)
class ReleaseSignal:
    project_key: str
    total_tests: int
    failed_tests: int
    critical_findings: int


def calculate_release_health(signal: ReleaseSignal) -> str:
    if signal.critical_findings > 0 or signal.failed_tests > 2:
        return "at_risk"
    if signal.failed_tests > 0:
        return "watch"
    return "healthy"


def build_quality_summary(signal: ReleaseSignal) -> dict:
    passed_tests = max(signal.total_tests - signal.failed_tests, 0)
    pass_rate = round((passed_tests / signal.total_tests) * 100, 1) if signal.total_tests else 0
    return {
        "project_key": signal.project_key,
        "health": calculate_release_health(signal),
        "total_tests": signal.total_tests,
        "passed_tests": passed_tests,
        "failed_tests": signal.failed_tests,
        "pass_rate": pass_rate,
    }

