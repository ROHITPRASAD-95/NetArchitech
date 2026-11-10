
import ipaddress
import math


class VLSMEngine:

    @staticmethod
    def calculate_prefix(hosts):

        if hosts <= 0:
            raise ValueError("Hosts must be positive")

        host_bits = math.ceil(math.log2(hosts + 2))

        prefix = 32 - host_bits

        return prefix

    @staticmethod
    def allocate_vlsm(root_network, requests):

        root = ipaddress.ip_network(root_network)

        # Sort departments by highest host requirement
        sorted_requests = sorted(
            requests.items(),
            key=lambda item: item[1],
            reverse=True
        )

        current = int(root.network_address)
        root_end = int(root.broadcast_address)

        results = []

        for department, hosts in sorted_requests:

            prefix = VLSMEngine.calculate_prefix(hosts)

            block_size = 2 ** (32 - prefix)

            # Align IP to subnet boundary
            current = (
                (current + block_size - 1)
                // block_size
            ) * block_size

            end = current + block_size - 1

            if end > root_end:
                raise ValueError("Address space exhausted")

            subnet = ipaddress.ip_network(
                (current, prefix)
            )

            results.append({

                "department": department,
                "network": str(subnet.network_address),
                "prefix": prefix,
                "subnet_mask": str(subnet.netmask),
                "gateway": str(subnet.network_address + 1),
                "broadcast": str(subnet.broadcast_address),
                "usable_hosts": subnet.num_addresses - 2

            })

            current = end + 1

        return results
