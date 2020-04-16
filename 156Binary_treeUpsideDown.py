class TreeNode():
  def __init__(self,root):
    self.val = root
    self.left = None
    self.right = None
class UpsideDown():
  def solution(self,root):
    if root is None:
      return root
    curr = root
    prev = prevRight = None
    while curr:
      next = curr.left
      curr.left = prevRight
      prevRight = curr.right
      curr.right = prev
      
      prev = curr
      curr = next
    return prev
      
