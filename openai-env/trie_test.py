from Trie import Trie

trie = Trie()

words = ["AMBER", "ALICE", "AMPLE", "BALLOON", "BALL", "BLAST", "BAND", "DENSE", "DUTCH", "DECK", "DANCE", "DRAMA", "MESS", "MAVERICK", "MAVEN", "PHYSICS", "PHONE", "PHANTOM", "PASS", "PEAK", "PACK", "ZEST", "ZEAL", "ZAP", "ZIP", "ZIPPER"]

for w in words:
  trie.add_string(w)

more_words = ["APPLE", "AMPLIFIER", "AMPLE", "BALLOON", "BALL", "DART", "DUTCH", "DECK", "DRAM", "FLAG", "MOP", "MAVERICK", "MANSION", "PHYSICS", "PHONE", "PHANTOM", "PASS", "PECK", "PAIN", "ZAM", "ZEST", "ZAP", "ZIP", "ZEBRA"]

for w in more_words:
  if trie.search_string(w):
    print(w)

prefix = ["A", "AM", "B", "BALL", "BA", "C", "CA", "DUTCH", "DECK", "GA", "J", "MA", "P", "PH", "PE", "Z", "ZIP"]

for p in prefix:
  print(f"frequency of prefix \"{p}\" is {trie.count_prefix(p)}")