class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
      
        mapz = {}
        timeS = []
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            mapz[position[i]] = time

        sorted_mapz = dict(sorted(mapz.items(), key=lambda item: item[0], reverse=True))

        for pos, time in sorted_mapz.items():
            if timeS and time <= timeS[-1]:
                continue 
            timeS.append(time)
        return len(timeS)


    # car 2, in 3 hours it will reach 10th mile
    # car 1 in 3 hours it will reach 10th mile
    # (target - position) / speed = hours

    # if car 2 catches up to car 1 with different speeds then both of them would have to match their speed      

    #         timeS.append(time)
    #     print(timeS)
    #     return ( len(set(timeS))) 
    # 7:3, 4:3, 1:10
    #     position=[ 4, 1   ,  0]
    #     time =   [ 3, 4.5, 10]
    #     stack  = [4.5, 3]

