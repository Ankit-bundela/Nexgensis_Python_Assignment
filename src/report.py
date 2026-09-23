#Create the Final report 

def generate_report(agent_data):
    report = {
        "agents": {},
        "best_agent": None
    }

    best_agent = None
    best_efficiency = float("inf")

    for agent_id, data in agent_data.items():

        packages_delivered = data["packages_delivered"]
        total_distance = data["total_distance"]

        if packages_delivered > 0:
            efficiency = total_distance / packages_delivered
        else:
            efficiency = 0

        report["agents"][agent_id] = {
            "packages_delivered": packages_delivered,
            "total_distance": round(total_distance, 2),
            "efficiency": round(efficiency, 2)
        }

        if packages_delivered > 0 and efficiency < best_efficiency:
            best_efficiency = efficiency
            best_agent = agent_id

    report["best_agent"] = best_agent

    return report