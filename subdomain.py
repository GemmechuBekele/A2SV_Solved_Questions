class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_counter = defaultdict(int)

        for record in cpdomains:
            count_str, full_domain = record.split()
            count = int(count_str)

            parts = full_domain.split('.')

            for i in range(len(parts)):
                subdomain = '.'.join(parts[i:])
                domain_counter[subdomain] += count

        result = [f"{cnt} {dom}" for dom, cnt in domain_counter.items()]
        return result