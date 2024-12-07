def compute_stats(uses, plans, products):
    total_uses = sum(uses)
    total_plans = len(plans)
    total_products = len(products)

    return total_uses, total_plans, total_products


def main() -> None:
    uses = [1, 2, 3]
    plans = ["plan1", "plan2", "plan3"]
    products = ["product1", "product2", "product3"]

    total_uses, total_plans, total_products = compute_stats(uses, plans, products)

    print(f"Total uses: {total_uses}")
    print(f"Total plans: {total_plans}")
    print(f"Total products: {total_products}")


if __name__ == "__main__":
    main()
