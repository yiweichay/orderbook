# Order book Project

Aim of this project is to build an orderbook for me to further understand the financial markets.

## Tech stack
Backend: Python

Visualisation: React (potentially, or just matplotlib)

## Description

- Limit Order: trading firms/banks [Add to binary tree]
- Market Order: Freetrade/Trading 212 [Execute Order]

### Architecture

There will be 2 binary trees: buy tree and sell tree. An order is added into the book (binary trees) recursively.

For each node in the binary tree, if there is more than 1 limit order, the limit order will be appended to the doubly linked list.

![image](https://github.com/user-attachments/assets/9e3f2da3-d7a9-4901-9aff-8a6d6497ee35)

1. limit orders: buy/sell at a certain price, the buyer/seller sets the price 
- add limit order to tree [done]
    - update the highestBuy/lowestSell in the order book
- delete limit order from tree: if buyer sets price that's higher than the current price, the buyer will buy the stock at the best 'selling' price (lowest sell price)
    - update the highestBuy/lowestSell in the order book


2. market orders: buy/sell at the best price, buyers wants to buy at lowest price, sellers want to sell at highest price
- when someone buys at market price: remove units from the deepest bottom left of the buy tree 
- when someone sells at market price: remove units from the deepest bottom right of the sell tree

**When deleting from buy tree**
- if the buyer sets a limit at 30 for 50 units, and the buy tree only has 20 @ 5 units, 30 @ 5 units.. the seller will buy the 10 units, and keep the rest of the 30 @ 40 units in the sell tree

