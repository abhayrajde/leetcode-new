class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        allParams = []
        for i in range(len(positions)):
            allParams.append([positions[i], healths[i], directions[i], i])
        allParams = sorted(allParams, key = lambda x:x[0])

        stack = []
        for i in allParams:
            if i[2] == 'R':
                stack.append(i)
            else:
                while(stack and stack[-1][2] == "R" and i[1]):
                    i2 = stack.pop()

                    if(i2[1] < i[1]):
                        i2[1] = 0
                        i[1] -= 1
                    
                    elif(i2[1] > i[1]):
                        i2[1] -= 1
                        i[1] = 0 
                        stack.append(i2)

                    else:
                        i2[1] = 0
                        i[1] = 0
                if(i[1]):
                    stack.append(i)

        allParams = sorted(allParams, key = lambda x:x[-1])
        result = []
        for i in range(len(allParams)):
            result.append(allParams[i][1])
        return [h for h in result if h > 0]




        # allParamsML = []
        # allParamsMR = []
        # for item in allParams:
        #     # print(item[2])
        #     if(item[2] == "R"):
        #         allParamsMR.append(item)
        #     else:
        #         allParamsML.append(item)

        # print(allParamsML)
        # print(allParamsMR)
        # if(allParamsMR):
        #     r = len(allParamsMR)
        # if(allParamsML):
        #     l = len(allParamsML)

        # rmove = lmove = 0
        # while(r != 0 and l != 0 and rmove<r and lmove<l and allParamsMR[-1][0] < allParamsML[0][0]):
        #     if(allParamsMR[-1][1] == allParamsML[0][1]):
        #         allParamsMR.pop()
        #         allParamsML.pop(0)

        #     elif(allParamsMR[-1][1] > allParamsML[0][1]):
        #         allParamsML.pop(0)
        #         allParamsMR[-1][1] -= 1
            
        #     else:
        #         allParamsMR.pop()
        #         allParamsML[0][1] -= 1

        # allParams2 = allParamsML
        # allParams2.extend(allParamsMR)
        # allParams2 = sorted(allParams2, key = lambda x:x[-1])
        # # print(allParams2)
        # result = []
        # for i in range(len(allParams2)):
        #     result.append(allParams2[i][1])
        # return result


        """
        :type positions: List[int]
        :type healths: List[int]
        :type directions: str
        :rtype: List[int]
        """
        
