// import express JS module into app 
// and creates its variable. 
var express = require('express'); 
var bodyParser = require('body-parser');
 
var app = express(); 
app.use(bodyParser.json({ limit: '50mb' }));
app.use(bodyParser.urlencoded({ limit: '50mb', extended: true, parameterLimit: 50000 }));
// app.use(bodyParser.urlencoded({ extended: true }));
// app.use(bodyParser.json()); 
app.use(bodyParser.text());

app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Headers");
    res.header("Access-Control-Allow-Credentials");
    res.header("Access-Control-Allow-Origin","*");
    res.header("Content-Type", "application/json");
    res.header("Access-Control-Allow-Methods", "GET, PUT, POST, DELETE, OPTIONS");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
  });

  // Creates a server
app.listen(5000,bodyParser.json(), function() { 
    console.log('server running on port 5000'); 
}) 

app.get('/name',bodyParser.json(), callName); 
var ddta; 

function callName(req, res,next) { 
    var roadname=req.query.raodname;


var datetime=req.query.datetime ;

  //res.setHeader('Content-Type', 'application/json');
    // child_process 
 var spawn = require("child_process").spawn; 
// E.g : http://localhost:5000/name?raodname=Liberty Avenue&datetime=10/7/2019,3:38 pm 


var process = spawn('python',["./prediction_connect.py", roadname, 
datetime]); 
console.log(req.query.raodname,req.query.datetime);

var ddata;
    // Takes stdout data from script which executed 
    // with arguments and send this data to res object 
process.stdout.on('data',(data)=> { 

var result=[{},{}]
 
ddata=data.toString();
//    result = ddta.map(a =>({start_node:start_node,end_node:end_node,level:level}));
//    console.log(result[1]);


// merge on the basis of common value/ factor.
//var congestion_response = roadobjt.map((r, i) =>  { r.properties = Object.assign(r.properties, ddta[i]);return r;});

console.log(ddata);
res.send(ddata);   
 
    });
   

} 
// app.post("/postdata", (req, res) => {
//     for (var i=0; i<req.body.length;i++){
//           var level = req.body[i].level;
//           var speed = req.body[i].predicted_speed;
//           var start_node=req.body[i].start_node;
//           var end_node=req.body[i].end_node;
//       }
 
//   //console.log(req.body);
//  //res.send();
//   });