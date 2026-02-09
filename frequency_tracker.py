from collections import defaultdict
class FrequencyTracker:

    def __init__(self):
        self.count = defaultdict(int)
        self.freq_count = defaultdict(int)
        

    def add(self, number: int) -> None:
        old_freq = self.count[number]
        if old_freq > 0:
            self.freq_count[old_freq] -=1

        new_freq = old_freq + 1
        self.count[number] = new_freq
        self.freq_count[new_freq] +=1

        

    def deleteOne(self, number: int) -> None:
        old_freq = self.count[number]
        if old_freq == 0:
            return

        self.freq_count[old_freq] -=1
        new_freq = old_freq - 1
        self.count[number] = new_freq

        if new_freq > 0:
            self.freq_count[new_freq] +=1


        

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_count[frequency] > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)