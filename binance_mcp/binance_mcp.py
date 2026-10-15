"""
Binance MCP module.
"""

from mcp.server.mcpserver import MCPServer
import requests


mcp = MCPServer("Binance MCP")


def get_symbol_from_name(name: str) -> str:
    """Get the Binance symbol for a given cryptocurrency name.

    Args:
        name (str): The name of the cryptocurrency (e.g., "bitcoin" or "btc").

    Returns:
        str: The corresponding Binance trading symbol (e.g., "BTCUSDT").
    """

    if name.lower() in ["bitcoin", "btc"]:
        return "BTCUSDT"
    elif name.lower() in ["ethereum", "eth"]:
        return "ETHUSDT"
    else:
        return name.upper()


@mcp.tool()
def get_price(symbol: str) -> float:
    """Get the current price of a cryptocurrency from Binance.

    Args:
        symbol (str): The Binance trading symbol of the cryptocurrency (e.g., "BTCUSDT").

    Returns:
        float: The current price of the cryptocurrency.
    """
    symbol = get_symbol_from_name(symbol)
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url, timeout=10)
    data = response.json()
    response.raise_for_status()

    return float(data["price"])


if __name__ == "__main__":
    mcp.run()
