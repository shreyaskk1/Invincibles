from invincibles_quality_service import ReleaseSignal, build_quality_summary, calculate_release_health


def test_release_is_healthy_when_all_tests_pass():
    signal = ReleaseSignal(
        project_key="invincibles-new-project",
        total_tests=12,
        failed_tests=0,
        critical_findings=0,
    )

    assert calculate_release_health(signal) == "healthy"


def test_release_moves_to_watch_when_a_test_fails():
    signal = ReleaseSignal(
        project_key="invincibles-new-project",
        total_tests=12,
        failed_tests=1,
        critical_findings=0,
    )

    assert calculate_release_health(signal) == "watch"


def test_quality_summary_calculates_pass_rate():
    signal = ReleaseSignal(
        project_key="invincibles-new-project",
        total_tests=10,
        failed_tests=2,
        critical_findings=0,
    )

    summary = build_quality_summary(signal)

    assert summary["project_key"] == "invincibles-new-project"
    assert summary["passed_tests"] == 8
    assert summary["pass_rate"] == 80.0

