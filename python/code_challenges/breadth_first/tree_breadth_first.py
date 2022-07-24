from .queue import Queue


def breadth_first(tree):
    tree_queue = Queue()

    tree_list = []


    # if tree.root is None:
    #     return tree_list
    # This is not working for some reason


    tree_queue.enqueue(tree.root)

    while tree_queue.front:
        front_node = tree_queue.dequeue()
        tree_list.append(front_node.value)

        if front_node.left:
            tree_queue.enqueue(front_node.left)
        if front_node.right:
            tree_queue.enqueue(front_node.right)
    print(tree_list)
    return tree_list
