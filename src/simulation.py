# Simulate agent deliveries
from src.distance import calculate_distance


def simulate_delivery(assignments, warehouses):

    agent_data = {}

    for assignment in assignments:

        package = assignment["package"]
        agent = assignment["agent"]

        agent_id = agent["id"]

        if agent_id not in agent_data:
            agent_data[agent_id] = {
                "packages_delivered": 0,
                "total_distance": 0.0,
                "current_location": agent["location"]
            }

        warehouse = next(
            warehouse
            for warehouse in warehouses
            if warehouse["id"] == package["warehouse_id"]
        )

        current_location = agent_data[agent_id]["current_location"]

        warehouse_location = warehouse["location"]
        destination = package["destination"]

        distance_to_warehouse = calculate_distance(
            current_location,
            warehouse_location
        )

        distance_to_destination = calculate_distance(
            warehouse_location,
            destination
        )

        total_distance = (
            distance_to_warehouse +
            distance_to_destination
        )

        agent_data[agent_id]["total_distance"] += total_distance
        agent_data[agent_id]["packages_delivered"] += 1

        agent_data[agent_id]["current_location"] = destination

    return agent_data