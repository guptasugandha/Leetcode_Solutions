class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        n = len(username)
        name_list = list(set(username))
        index_dict = {}
        for i in range(len(name_list)):
            index_dict[name_list[i]] = [] 

        for i in range(n):
            index_dict[username[i]].append(i)

        for times in index_dict.values():
            times.sort(key=lambda x: timestamp[x])
        possible_sequence = {}
        max_tuple = []
        max_count = 0    
        for times in index_dict.values():

            # has 3-sequence
            if len(times) >= 3:
                seen = set()
                for i in range(0, len(times)-2):
                    for j in range(i+1, len(times)-1):
                        for k in range(j+1, len(times)):

                            current_sequence = (website[times[i]], website[times[j]], website[times[k]])

                            if current_sequence not in seen:
                                seen.add(current_sequence)
                                # update possible_sequence only when we haven't seen the current_sequence for this user

                                if current_sequence not in possible_sequence:
                                    possible_sequence[current_sequence] = 1
                                else:
                                    possible_sequence[current_sequence] += 1

                                if possible_sequence[current_sequence] == max_count:
                                    max_tuple.append(current_sequence)
                                elif possible_sequence[current_sequence] > max_count:
                                    max_tuple = [current_sequence]
                                    max_count = possible_sequence[current_sequence]
                                    
        max_tuple.sort()
        return list(max_tuple[0])