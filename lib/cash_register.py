#!/usr/bin/env python3

class CashRegister:
  '''A cash register'''
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.previous = []
  
  def add_item(self, item, price, quantity=1):
    
    self.total += price * quantity
    for _ in range(quantity):
      self.items.append(item)
    self.previous.append({"item": item, "quantity": quantity, "price": price})
  
  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      self.total -= self.total * (self.discount / 100)
      print("After the discount, the total comes to ${:d}.".format(int(self.total)))
  def void_last_transaction(self):
    if not self.previous:
      return "There are no transactions to void."
    
    self.total -= (self.previous[-1]["price"] * self.previous[-1]["quantity"])
      
    for _ in range(self.previous[-1]["quantity"]):
      self.items.pop()
    self.previous.pop()