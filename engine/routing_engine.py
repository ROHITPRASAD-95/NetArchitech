class RoutingEngine:

    @staticmethod
    def recommend_routing(site_count, subnet_count, cloud_required=False):

        if site_count <= 0:
            raise ValueError("Site count must be positive")

        if subnet_count <= 0:
            raise ValueError("Subnet count must be positive")

        if not isinstance(cloud_required, bool):
            raise TypeError("cloud_required must be True or False")

        if site_count == 1 and subnet_count < 50 and not cloud_required:
            return {
                "protocol": "OSPF Area 0",
                "reason": "Single autonomous system with fewer than 50 subnets. OSPF link-state routing supports fast convergence."
            }

        else:
            return {
                "protocol": "Multi-Area OSPF or eBGP",
                "reason": "Multiple sites or cloud connectivity require routing-domain separation and scalable inter-network routing."
            }