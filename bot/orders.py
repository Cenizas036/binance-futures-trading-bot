import logging

logger = logging.getLogger()

def place_order(client, symbol, side, order_type, quantity, price=None):

    try:

        logger.info(f"Order request -> {symbol} {side} {order_type} qty={quantity} price={price}")

        if order_type == "MARKET":

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logger.info(f"Order response -> {order}")

        return order

    except Exception as e:

        logger.error(f"Order failed -> {str(e)}")
        raise