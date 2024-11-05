class TreeNode() :
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

# 전역변수 부분
memory = []         # memory 리스트 생성
root = None         # root를 None으로 지정
nameAry = ['bp', 'rb', 'mm', 'ap', 'gd', 'tw']

## main code ##

node = TreeNode()       # 신규 node 생성
node.data = nameAry[0]      #nameAry 0번째를 node.data로 지정
root = node                 # 새로 생성한 node를 root로 지정
memory.append(node)         # memory 리스트에 node를 추가

for name in nameAry[1:] :       #nameAry 2번째부터 끝까지 name으로 돌면서
    node = TreeNode()           # 신규 node 생성
    node.data = name            # for 문으로 돌면서 받은 name 값을 node.data에 대입함

    current = root              # root를 현재 위치인 current로 지정
    while True :                # 무한 반복문 열고
        if name < current.data :            # 만약 이름의 데이터가 현재위치의 데이터보다 값이 작을 경우
            if current.left == None :       # 현재위치의 왼쪽값이 없을 경우
                current.left = node         # node값을 현재위치의 왼쪽으로 보냄
                break
            current = current.left          # 현재위치의 왼쪽을 현재위치로 옮김..
        else :
            if current.right == None :      # 위 과정을 오른쪽으로 틀었을 때 if문
                current.right = node
                break
            current = current.right

    memory.append(node)                     # memory 리스트에 node 값을 추가

del_data = "mm"

current = root      # root를 current로 지정
parent = None       # parent를 none으로 지정
while True :        # 무한 반복문
    if del_data == current.data :           # 삭제할 데이터와 현재 데이터가 일치할 경우

        if current.left == None and current.right == None :     # 현재의 왼쪽이 없고 오른쪽도 없을 경우
            if parent.left == current :         # 부모의 왼쪽값이 현재 일 경우
                parent.left = None              # 부모의 왼쪽은 없다.
            else :
                parent.right = None             # 또는 부모의 오른쪽은 없다.
            del(current)                    # 현재 값 삭제

        elif current.left is not None and current.right == None :       # 현재의 왼쪽값이 있고 오른쪽 값이 없을 경우
            if parent.left == current :             # 부모의 왼쪽이 현재값과 같다면
                parent.left = current.left          # 부모의 왼쪽이 현재의 왼쪽과 같다
            else :
                parent.right = current.left         # 부모의 오른쪽이 현재의 왼쪽과 같다.
            del(current)                # current값 삭제

        elif current.left == None and current.right is not None :       #현재값의 왼쪽이 없고 오른쪽이 있을 때
            if parent.left == current :             # 부모의 왼쪽이 현재와 같은 값이라면
                parent.left = current.right         # 부모의 왼쪽이 현재의 오른쪽과 같다.
            else :
                parent.right = current.right        # 부모의 오른쪽은 현재의 오른쪽과 같다
                del(current)                    # current 값 삭제

        print(del_data, '이(가) 삭제 됨')
        break

    elif del_data < current.data :                  # 삭제할 데이터의 값이 현재 데이터보다 작을 경우
        if current.left == None :           # 현재의 왼쪽이 없다면,
            print(del_data, '이(가) 트리에 없음')
            break
        parent = current        # 부모를 현재로 지정
        current = current.left      # 현재는 현재의 왼쪽값으로 설정

    else :                                      #삭제할 데이터의 값이 현재 데이터보다 클 경우
        if current.right == None :
            print(del_data, '이(가) 트리에 없음')
            break
        parent = current
        current = current.right