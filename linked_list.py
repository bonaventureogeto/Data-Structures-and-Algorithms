prev = None
current = head

while current != None:
    next = current.next  # save the next node
    current.next = prev  # reversing the current node's pointer
    prev = current  # moving prev forward
    current = next  # move current forward

head = prev  # update the head to the new first node
