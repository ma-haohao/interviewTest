
def validateStackSequences(pushed,popped):
    push_index = 0
    pop_index = 0
    tryStack = []
    # 条件循环
    while True:
        print(tryStack)
        if tryStack == []:
            if push_index == len(pushed) and pop_index == len(popped):
                return True
            if push_index == len(pushed) and pop_index < len(popped):
                return False
            tryStack.append(pushed[push_index])
            push_index += 1
        if tryStack[-1] != popped[pop_index]:
            # 先判断是否已经到最后的push_index了
            if push_index == len(pushed):
                return False
            tryStack.append(pushed[push_index])
            push_index += 1
        else:
            tryStack.pop()
            pop_index += 1

test=validateStackSequences([1,2,3,4,5,6],[6,5,4,3,2,1])
print(test)