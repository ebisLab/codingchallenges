"""You've a binary tree, create a linked lsist of all the nodes at each depth"""

# * be able to track each depth

# ? Does order matter
# ? Persist Parent/Child relations
# ? Return type

"""
[{level 1}, => {A}      1 {linkedList}
 {level 2} => {B,E}     2 {linkedlist}
  {level 3} => {C,D,F}  3 {linkedlist}
  ]
  """

  # Solutions
  # Traversal (pre/in/post)
  # Need to track each level
  # DFS/BFS
  # Return array/list containing LinkedList of each level as items

"""
List<LinkedList<TreeNode>>
createLinkedListForEachLevel(TreeNode node)
{
    //create arraylist to track elements for each level
    // create the logic,start with level 0
    //return the result
}




#  ! https://www.youtube.com/watch?v=AuBN68-63Zg&feature=youtu.be
