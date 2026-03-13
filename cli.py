import argparse

from bot.client import get_client
from bot.orders import place_order
from bot.validators import *
from bot.logging_config import setup_logger

logger = setup_logger()

def main():

    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price")

    args = parser.parse_args()

    try:

        symbol = args.symbol.upper()
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)

        price = None

        if order_type == "LIMIT":
            price = validate_price(args.price)

        print("\nOrder Request Summary")
        print("----------------------")
        print("Symbol:", symbol)
        print("Side:", side)
        print("Type:", order_type)
        print("Quantity:", quantity)
        print("Price:", price)

        client = get_client()

        order = place_order(client, symbol, side, order_type, quantity, price)

        print("\nOrder Response")
        print("----------------------")

        if isinstance(order, dict):

            print("Full API Response:")
            print(order)

            if "orderId" in order:
                print("Order ID:", order["orderId"])

            if "status" in order:
                print("Status:", order["status"])

            if "executedQty" in order:
                print("Executed Qty:", order["executedQty"])

            if "avgPrice" in order:
                print("Average Price:", order["avgPrice"])

        print("\n✅ Finished")

    except Exception as e:

        logger.error(str(e))
        print("\n❌ Error:", str(e))


if __name__ == "__main__":
    main()