let fs=require("fs");
let path=require("path");
//TREE
function treeFn(dirPath){
    //console.log("Tree command implemented for ",dirPath);
    if(dirPath==undefined){
        /*
        console.log("Please the enter the path\n");
        return:*/
        treeHelper(process.cwd(), "");
    }
    else{
        let doesExist=fs.existsSync(dirPath);
        if(doesExist){
            treeHelper(dirPath, "");
        } else{
            console.log("Please the enter the correct path\n");
            return;
        }
    }
}

function treeHelper(dirPath, indent){
    //identify whether it's file or folder
    let isFile=fs.lstatSync(dirPath).isFile();
    if(isFile==true){
        let fileName=path.basename(dirPath);
        console.log(indent+ "├───" +fileName); 
    }else{
        let dirName=path.basename(dirPath);
        console.log(indent+ "└───" +dirName);

        let childrens=fs.readdirSync(dirPath);
        
        for(let i=0;i<childrens.length;i++){
            let childPath=path.join(dirPath,childrens[i]);
            treeHelper(childPath,indent+"\t");
        }
    } 
}
module.exports={
    treeKey:treeFn
}