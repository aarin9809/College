# week05_03_chap04_07.py
class Node:
    def __init__(self):
        self.data = None
        self.link = None


def print_nodes(start):
    current = start

    if current is None:
        return
    print(current.data, end=' ')
    while current.link is not None:
        current = current.link
        print(current.data, end=' ')
    print()


def insert_node(find_data, insert_data):
    global head, current, pre

    if head.data == find_data:  # 첫 번째 노드 삽입
        node = Node()
        node.data = insert_data
        node.link = head
        head = node
        return

    current = head
    while current.link is not None:  # 중간 노드 삽입
        pre = current
        current = current.link
        if current.data == find_data:
            node = Node()
            node.data = insert_data
            node.link = current
            pre.link = node
            return

    node = Node()                   # 마지막 노드 삽입
    node.data = insert_data
    current.link = node


def delete_node(delete_data):
    global head, current, pre

    if head.data == delete_data :         # 첫 번째 노드 삭제
        current = head
        head = head.link  # 헤드 위치 조정
        del current
        return

    current = head                          # 첫 번째  외 노드 삭제
    while current.link is not None:
        pre = current
        current = current.link
        if current.data == delete_data:
            pre.link = current.link  # 삭제될 노드의 link를 이전 노드이게 전달
            del current
            return


head, current, pre = None, None, None
data_array = ["다현", "정연", "쯔위", "사나", "지효"]
#data_array = ["백현", "첸"]

if __name__ == "__main__":
    node = Node()
    node.data = data_array[0]
    head = node

    for i in range(1, len(data_array)):
        pre = node
        node = Node()
        node.data = data_array[i]
        pre.link = node

    print_nodes(head)

    delete_node("다현")
    print_nodes(head)

    delete_node("쯔위")
    print_nodes(head)

    delete_node("지효")
    print_nodes(head)

    delete_node("재남")
    print_nodes(head)


    # insert_node("다현", "화사")
    # print_nodes(head)
    #
    # insert_node("사나", "솔라")
    # print_nodes(head)
    #
    # insert_node("재남", "문별")
    # print_nodes(head)
    #
    # insert_node("쯔위", "휘인")
    # print_nodes(head)
