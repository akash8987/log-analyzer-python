def analyze_logs(lines):
    summary = {}

    for line in lines:
        level = line.split(":")[0]
        summary[level] = summary.get(level, 0) + 1

    return summary


def run():
    logs = [
        "INFO: Service started",
        "ERROR: Database unavailable",
        "INFO: Request received",
        "WARN: Low memory",
        "ERROR: Timeout"
    ]

    result = analyze_logs(logs)
    for k, v in result.items():
        pass


if __name__ == "__main__":
    run()
