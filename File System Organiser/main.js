#!/usr/bin/env node

let inputArr= process.argv.slice(2);
let fs=require("fs");
let path=require("path");
let helpObj=require("./Commands/help");
let organiseObj=require("./Commands/organise");
let treeObj=require("./Commands/tree");

console.log(inputArr);

let types={
    media:["mp4","mkv"],
    archives:["zip","7z","rar","tar","gz","ar","iso","xz"],
    documents:["docx","doc","pdf","xlsx","xls","odt","ods","odp","odg","odf","txt","ps","tex"],
    app:["exe","dmg","pkg","deb"]
}
//node main.js tree "directoryPath"
//node main.js organise "directoryPath"
//node main.js help

let command=inputArr[0];
switch(command){
    case "tree":
        treeObj.treeKey(inputArr[1]);
        break;
    case "organise":
        organiseObj.oragniseKey(inputArr[1]);
        break;
    case "help":
        helpObj.helpKey();
        break;
    default:
        console.log("Please input valid command\n");
        break;
}

