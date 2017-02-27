def baubles_on_tree(baubles, branches):
    if not branches:
        return "Grandma, we will have to buy a Christmas tree first!"
    d,r = divmod(baubles,branches)
    return [d+1]*r+[d]*(branches-r)


#print baubles_on_tree(5,5)#,[1,1,1,1,1])
#print baubles_on_tree(5,0)#,"Grandma, we will have to buy a Christmas tree first!")
#print baubles_on_tree(6,5)#,[2,1,1,1,1])
#print baubles_on_tree(50,9)#,[6,6,6,6,6,5,5,5,5])
#print baubles_on_tree(0,10)#,[0,0,0,0,0,0,0,0,0,0])
#print baubles_on_tree(89,1)
print baubles_on_tree(78,7)
