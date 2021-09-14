let fs=require("fs");
let path=require("path");
let types;
//ORGANISE
function oragniseFn(dirPath){
    //console.log("Organise command implemented for ",dirPath);
    let desPath;
    if(dirPath==undefined){
        /*
        console.log("Please the enter the path\n");
        return;*/
        organiseHelper(process.cwd(),destPath);
    }
    else{
        let doesExist=fs.existsSync(dirPath);
        if(doesExist){
            destPath=path.join(dirPath,"organisedFiles");
            if(fs.existsSync(destPath)==false){
                fs.mkdirSync(destPath);
            }
        }
        else{
            console.log("Please the enter the correct path\n");
            return;
        }
    }
    organiseHelper(dirPath,destPath);

}

function organiseHelper(src,dest){
    let childNames=fs.readdirSync(src);
    //console.log(childNames);
    for(let i=0;i<childNames.length;i++){
        let childAddress=path.join(src,childNames[i]);
        let is_File=fs.lstatSync(childAddress).isFile();
        if(is_File){
            //console.log(childNames[i]);
            let category=getCategory(childNames[i]);
            console.log(childNames[i],"belongs to --->",category);

            sendFiles(childAddress,dest,category);
        }
    }
} 

function getCategory(name){
    let ext=path.extname(name);
    ext=ext.slice(1);
    for(let type in types){
        let currentTypeArray=types[type];
        for(i=0;i<currentTypeArray.length;i++){
            if(ext==currentTypeArray[i])
                return type; 
        }
    }
    return "others";
}

function sendFiles(srcFilePath,dest,category){
    let categoryPath=path.join(dest,category);
    if(fs.existsSync(categoryPath)==false){
        fs.mkdirSync(categoryPath);
    }
    let fileName=path.basename(srcFilePath);
    let destFilePath=path.join(categoryPath,fileName);
    
    fs.copyFileSync(srcFilePath,destFilePath);
    console.log(fileName,"copied to",category);
    //It deletes the unorganised content after its been copied to the organised folder destination.
    fs.unlinkSync(srcFilePath);
    console.log(fileName,"deleted from",srcFilePath);

    
}

module.exports={
    oragniseKey:oragniseFn
}