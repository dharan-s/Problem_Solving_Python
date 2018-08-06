MORSE = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]


words = ["tmwsslt","oabhx","mysiuu","hayri","hwpb","hpqs","kswj","nniatj","csttj","tlsj","csittt","nbvm","tleso","khum","chj","ciij","chj","khum","chj","chj","cham","tlsj","chj","csej","chj","ksso","ndho","ndho","qmvmg","qzjg","qzjg","aiojl","lojl","sttuq","vxq","euxq","vxq","vxq","vxq","vdoa","smuq","vxq","djqgi","bmmkgi","jkcu","atqcu","jyav","xnvy","xnsqt","xdunm","npipm","dzuy","xduy","xdimat","nwrmwx","xcqtx","tbaovi","zutzed","skzb","vwxs","vjib","zdkf","glcr","gafnr","ksnw","cuew","cfw","cuim","tasnw","tlrw","cfw","cfw","nbdm","kefw","cfw","hhsr","issif","hssin","shhr","ihhf","mnfaj","ovuj","bpdn","nvkf","qyxv","gqgav","kxmmi","yuod","ktejz","tpjz","yumz","tpjtd","tbaovi","zutzed","smdba","vzdu","vgrv","ekgpwx","aagpju","zpqd"]

#words = ["gin", "zen", "gig", "Msg"]#

#seen = {"".join(MORSE[ord(c) - ord('a')] for c in word) for word in words}
seen = {"".join(MORSE[ord(c) - 97 ] for c in word) for word in words}
print(seen)
print(len(seen))