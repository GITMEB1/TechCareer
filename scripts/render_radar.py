import os
import yaml

OPPORTUNITIES_FILE = "tracking/opportunities.yaml"
OUTPUT_FILE = "tracking/OPPORTUNITY_RADAR.md"
TRACK_ORDER = ["Velocity", "Pivot", "Unknown"]


def load_data():
    if not os.path.exists(OPPORTUNITIES_FILE):
        print(f"Error: {OPPORTUNITIES_FILE} not found.")
        return []

    with open(OPPORTUNITIES_FILE, "r") as file:
        try:
            data = yaml.safe_load(file) or {}
            return data.get("opportunity_list", [])
        except yaml.YAMLError as exc:
            print(f"Error parsing YAML: {exc}")
            return []


def filter_active_opportunities(opportunities):
    active_statuses = [
        "Discovered",
        "Qualified",
        "IntelReady",
        "Drafting",
        "ReadyToSubmit",
        "Submitted",
        "FollowUpSent",
        "Responded",
        "Interviewing",
    ]
    return [opp for opp in opportunities if opp.get("status") in active_statuses]


def _track_val(track):
    try:
        return TRACK_ORDER.index(track)
    except ValueError:
        return len(TRACK_ORDER)


def _life_fit_val(opp):
    score = opp.get("life_fit_score", opp.get("fit_score", 0))
    try:
        return int(score)
    except Exception:
        return 0


def render_radar(opportunities):
    active_opps = filter_active_opportunities(opportunities)

    # Group by deployment track; within each group sort by life_fit_score descending.
    active_opps.sort(
        key=lambda x: (
            _track_val(x.get("deployment_track", "Unknown")),
            -_life_fit_val(x),
            x.get("priority", "Unknown"),
        )
    )

    lines = [
        "# Opportunity Radar",
        "**Weekly Goal:** Find 10 -> Shortlist 3 -> Apply.",
        "",
        "## Active Pipeline",
        "",
        "| Track | Status | Life Fit | Priority | Company | Role | Category | Salary | Location | Link | Next Action |",
        "| :--- | :--- | :---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
    ]

    for opp in active_opps:
        track = opp.get("deployment_track", "Unknown")
        status = opp.get("status", "Unknown")
        life_fit = _life_fit_val(opp)
        priority = opp.get("priority", "Unknown")
        company = opp.get("company", "Unknown")
        role = opp.get("role_title", "Unknown")
        category = opp.get("category", "Unknown")
        salary = opp.get("salary_range", "Unknown")
        location = opp.get("location", "Unknown")

        link = opp.get("evidence", {}).get("link", "")
        link_md = f"[Link]({link})" if link and str(link).startswith("http") else "Search"

        next_action = opp.get("actions", {}).get("next_step", "Unknown")

        row = (
            f"| **{track}** | **{status}** | **{life_fit}** | **{priority}** | **{company}** | "
            f"**{role}** | **{category}** | {salary} | {location} | {link_md} | {next_action} |"
        )
        lines.append(row)

    lines.extend(
        [
            "",
            "## Categories",
            "- **SUPPORT**: L2/L3 Support, SaaS Support (Velocity Track)",
            "- **IMP**: Implementation, Onboarding, Solution Engineer (Velocity Track)",
            "- **TAM**: Technical Account Manager (Velocity Track)",
            "- **DATA**: Data Engineer, Analytics Engineer (Pivot Track)",
            "- **OPS**: Platform Ops, localized DevOps (Velocity Track/Pivot Track)",
        ]
    )

    return "\n".join(lines) + "\n"


def main():
    opportunities = load_data()
    if not opportunities:
        return

    markdown_content = render_radar(opportunities)

    with open(OUTPUT_FILE, "w") as file:
        file.write(markdown_content)

    print(
        f"Successfully generated {OUTPUT_FILE} with {len(filter_active_opportunities(opportunities))} active opportunities."
    )


if __name__ == "__main__":
    main()
