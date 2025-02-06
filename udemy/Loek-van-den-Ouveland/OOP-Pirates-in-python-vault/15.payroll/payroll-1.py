class Payroll:
    def calculate_shares(self, crew, ducats):
        sum_of_ranks = sum(pirat.role.rank for pirat in crew)
        return [pirate.role.rank / sum_of_ranks * ducats for pirate in crew]
        