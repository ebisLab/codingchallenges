const inOrderTraversal =(root)=>{
if (root !==null){
    inOrderTraversal(root.left); //recursive
    visit(root.data) //apply logic
    inOrderTraversal(root.right)
}
}
/*
TODO
def inOrderTraversal(self, root):
    if (root is not None)
        inOrderTraversal(root.left)
        visit(root.data)
        inOrderTraversal(root.right)

*/


const preOrderTraversal =(root)=>{
    if (root !==null){
        visit(root.data) //apply logic
        inOrderTraversal(root.left);
        inOrderTraversal(root.right)
    }
    }

  
const postOrderTraversal =(root)=>{
    if (root !==null){
        //children first then parent
        inOrderTraversal(root.left);
        inOrderTraversal(root.right)
        visit(root.data) //apply logic

        
    }
    }  

    

    // ! https://www.youtube.com/watch?v=a5pg8A2nQXI&feature=youtu.be