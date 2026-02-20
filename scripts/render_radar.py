import yaml
import os

OPPORTUNITIES_FILE = "tracking/opportunities.yaml"
OUTPUT_FILE = "tracking/OPPORTUNITY_RADAR.md"

def load_data():
    if not os.path.exists(OPPORTUNITIES_FILE):
        print(f"Error: {OPPORTUNITIES_FILE} not found.")
        return []
        
    with open(OPPORTUNITIES_FILE, 'r') as file:
        try:
            data = yaml.safe_load(file)
            return data.get('opportunity_list', [])
        except yaml.YAMLError as exc:
            print(f"Error parsing YAML: {exc}")
            return []

def filter_active_opportunities(opportunities):
    # Only pick statuses we want on the radar
    active_statuses = [
        "Discovered", "Qualified", "IntelReady", 
        "Drafting", "ReadyToSubmit", "Submitted", 
        "FollowUpSent", "Responded", "Interviewing"
    ]
    return [opp for opp in opportunities if opp.get('status') in active_statuses]

def render_radar(opportunities):
    active_opps = filter_active_opportunities(opportunities)
    
    # Sort active opportunities by priority (P1 -> P3 -> Unknown)
    def priority_val(p):
        if p == 'P1': return 1
        if p == 'P2': return 2
        if p == 'P3': return 3
        return 99
        
    active_opps.sort(key=lambda x: priority_val(x.get('priority', 'Unknown')))
    
    lines = [
        "# Opportunity Radar",
        "**Weekly Goal:** Find 10 -> Shortlist 3 -> Apply.",
        "",
        "## Active Pipeline",
        "",
        "| Status | Priority | Company | Role | Category | Salary Floor | location | Link | Next Action |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |"
    ]
    
    for opp in active_opps:
        status = opp.get('status', 'Unknown')
        priority = opp.get('priority', 'Unknown')
        company = opp.get('company', 'Unknown')
        role = opp.get('role_title', 'Unknown')
        category = opp.get('category', 'Unknown')
        salary = opp.get('salary_range', 'Unknown')
        location = opp.get('location', 'Unknown')
        
        link = opp.get('evidence', {}).get('link', '')
        link_md = f"[Link]({link})" if link and link.startswith('http') else "Search"
        
        next_action = opp.get('actions', {}).get('next_step', 'Unknown')
        
        # Markdown row
        row = f"| **{status}** | **{priority}** | **{company}** | **{role}** | **{category}** | {salary} | {location} | {link_md} | {next_action} |"
        lines.append(row)
        
    lines.extend([
        "",
        "## Categories",
        "- **SUPPORT**: L2/L3 Support, SaaS Support (Speed Mode)",
        "- **IMP**: Implementation, Onboarding, Solution Engineer (Speed Mode)",
        "- **TAM**: Technical Account Manager (Speed Mode)",
        "- **DATA**: Data Engineer, Analytics Engineer (Pivot Mode)",
        "- **OPS**: Platform Ops, localized DevOps (Speed/Pivot)"
    ])
    
    return "\n".join(lines) + "\n"

def main():
    opportunities = load_data()
    if not opportunities:
        return
        
    markdown_content = render_radar(opportunities)
    
    with open(OUTPUT_FILE, 'w') as file:
        file.write(markdown_content)
        
    print(f"Successfully generated {OUTPUT_FILE} with {len(filter_active_opportunities(opportunities))} active opportunities.")

if __name__ == "__main__":
    main()
