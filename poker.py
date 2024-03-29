def straight(ranks):					#ranks are compared in straight suits may be different
    if len(set(ranks))==5 and (max(ranks)-min(ranks)==4):
        return True
    return False
        
        
def flush(suits):					#suits should be same for a flush
    if len(set(suits))==1:
        return True
    return False


def kind(n,ranks):					#to check two or three or four of a kind 'n' represents here the kind to be checked
    for r in ranks:
        if ranks.count(r)==n:
            return r
    return None
	
              
def two_pair(ranks):					#to check for pairs 
    highcard=kind(2,ranks)
    lowcard=kind(2,tuple(reversed(ranks)))		#tuple(reversed(ranks)) to sort in reversed order
    if highcard != lowcard:
        return (highcard,lowcard)
    return None		


def card_ranks(hand):					#to seperate the ranks in hand							
    ranks=['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    return ranks


def card_suits(hand):					#to seperate the suits in hand
    return [s for r,s in hand]


def poker(hands):					#to compare the different ranks
    return max(hands,key=hand_rank)


def hand_rank(hand):					#comparison key for the different ranks				
    ranks=[]
    ranks=card_ranks(hand)
    suits=card_ranks(hand)

    if straight(ranks) and flush(suits):
        return (8,max(ranks))

    elif kind(4,ranks):
        return (7,kind(4,ranks),kind(1,ranks))

    elif kind(3,ranks) and kind(2,ranks):
        return (6,kind(3,ranks),kind(2,ranks))

    elif flush(suits):
        return (5,sorted(ranks))

    elif straight(ranks):
        return (4,max(ranks))

    elif kind(3,ranks):
        return(3,kind(3,ranks),ranks.remove(kind(3,ranks)))

    elif two_pair(ranks):
        return (2,two_pair(ranks),kind(1,ranks))

    elif kind(2,ranks):
        return (1,kind(2,ranks),ranks.remove(kind(2,ranks)))

    else:
        return ranks
    



#multiline comment
...
if __name__=="__main__":
    assert(straight([6,5,4,3,2])==True)			#for unit testing
    assert(straight([6,5,5,3,2])==False)
    assert(flush(['D','D','D','D','D'])==True)			
    assert(kind(2,[6,5,5,3,2])==5)
    assert(two_pair([6,5,5,3,3])==(5,3))
...



if __name__=="__main__":
    list=[]
    n = int(input("Enter number of players : "))
    for i in range(0, n):
        lst=[] 
        for j in range(0, 5): 
            ele = str(input()) 
            lst.append(ele)
        list.append(lst)
    print(poker(list))