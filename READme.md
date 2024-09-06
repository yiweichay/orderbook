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

![architecture](attachments\6260407385520717107.jpg)
